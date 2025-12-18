import time
from devices import devices
from gateway import Gateway
# import random

gateway = Gateway()

# Simulation loop (Day 1)
for _ in range(10):
    for device in devices:
        packet = device.generate_packet()
        gateway.log_packet(packet)
        print(f"Logged packet from {device.name}: {packet}")
        print("---------------------------------------------------------")
    time.sleep(1)
