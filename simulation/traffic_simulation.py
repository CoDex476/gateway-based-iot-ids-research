import csv
import random
import time
from datetime import datetime


OUTPUT_FILE = "week2_day3_gateway_traffic.csv"

# Device definitions
DEVICES = ["Temperature Sensor","Motion Sensor","Smart Plug",
           "Lighting Controller","Low-Cost IP Camera"]


def generate_normal_packet(device):
    """Generate normal traffic behavior"""

    packet_sizes = {
        "Temperature Sensor": random.randint(50, 100),
        "Motion Sensor": random.randint(60, 120),
        "Smart Plug": random.randint(70, 150),
        "Lighting Controller": random.randint(80, 200),
        "Low-Cost IP Camera": random.randint(500, 1500)}

    protocols = {
        "Temperature Sensor": "MQTT",
        "Motion Sensor": "MQTT",
        "Smart Plug": "CoAP / MQTT",
        "Lighting Controller": "CoAP",
        "Low-Cost IP Camera": "RTSP / TCP"}

    directions = {
        "Temperature Sensor": "Device -> Gateway",
        "Motion Sensor": "Device -> Gateway",
        "Smart Plug": "Device <-> Gateway",
        "Lighting Controller": "Device <-> Gateway",
        "Low-Cost IP Camera": "Device -> Gateway -> Cloud"}

    bursts = {
        "Temperature Sensor": "None",
        "Motion Sensor": "Small bursts",
        "Smart Plug": "Short bursts on toggle",
        "Lighting Controller": "Small bursts on state change",
        "Low-Cost IP Camera": "Continuous during streaming"}

    return {
        "timestamp": datetime.now().isoformat(),
        "device": device,
        "size": packet_sizes[device],
        "direction": directions[device],
        "protocol": protocols[device],
        "burst": bursts[device],
        "label": "normal",
        "attack_type": "none"}


# ------------------ Attack Simulations ------------------

def flooding_attack(device):
    """High-rate flooding / botnet traffic"""
    return {
        "timestamp": datetime.now().isoformat(),
        "device": device,
        "size": random.randint(200, 600),
        "direction": "Device -> Gateway -> External",
        "protocol": "MQTT",
        "burst": "High-rate flooding",
        "label": "attack",
        "attack_type": "flooding"}


def scan_attack(device):
    """Scanning / probing behavior"""
    return {
        "timestamp": datetime.now().isoformat(),
        "device": device,
        "size": random.randint(40, 80),
        "direction": "Device -> Gateway -> Multiple External",
        "protocol": "TCP",
        "burst": "Rapid probing",
        "label": "attack",
        "attack_type": "scan"}


def replay_attack(device):
    """Event replay / spoofing"""
    return {
        "timestamp": datetime.now().isoformat(),
        "device": device,
        "size": random.randint(60, 120),
        "direction": "Device -> Gateway",
        "protocol": "MQTT",
        "burst": "Repeated events",
        "label": "attack",
        "attack_type": "replay"}


# ------------------ MAIN SIMULATION ------------------

def main():
    with open(OUTPUT_FILE, mode="w", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["timestamp","device","size","direction","protocol",
                              "burst","label","attack_type"])

        writer.writeheader()
        print("[*] Generating traffic...")

        for _ in range(20):
            # Normal traffic
            for device in DEVICES:
                writer.writerow(generate_normal_packet(device))

            # Simulated attacks
            writer.writerow(flooding_attack("Temperature Sensor"))
            writer.writerow(scan_attack("Smart Plug"))
            writer.writerow(replay_attack("Motion Sensor"))

            time.sleep(1)

        print("[**] Traffic generation completed.")


if __name__ == "__main__":
    main()
