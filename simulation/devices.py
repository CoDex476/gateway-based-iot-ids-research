import random
# import time


class Device:
    def __init__(self, name, packet_size_range, frequency, direction,protocol,
        burst, idle_period):
        self.name = name
        self.packet_size_range = packet_size_range
        self.frequency = frequency
        self.direction = direction
        self.protocol = protocol
        self.burst = burst
        self.idle_period = idle_period

    def generate_packet(self):
        size = random.randint(self.packet_size_range[0], self.packet_size_range[1])
        return {"device": self.name, "size": size, "direction": self.direction,
            "protocol": self.protocol, "burst": self.burst,
        }


# Defining my devices
temperature_sensor = Device("Temperature Sensor", (50, 100), 30, "Device -> Gateway", 
                            "MQTT", "None", 30)

motion_sensor = Device("Motion Sensor", (60, 120),"event", "Device -> Gateway",
                       "MQTT", "Small bursts", "Idle until motion")

smart_plug = Device("Smart Plug", (70, 150), "event", "Device <-> Gateway", 
                    "CoAP / MQTT", "Short bursts on toggle", "Idle otherwise")

lighting_controller = Device("Lighting Controller", (80, 200), "periodic+event", 
                             "Device <-> Gateway", "CoAP", "Small bursts on state change", "Idle otherwise")

ip_camera = Device("Low-Cost IP Camera", (500, 1500), "event-triggered streaming",
                   "Device -> Gateway -> Cloud","RTSP / TCP","Continuous during streaming","Idle when inactive")

devices = [temperature_sensor,motion_sensor,smart_plug,lighting_controller,ip_camera,]
