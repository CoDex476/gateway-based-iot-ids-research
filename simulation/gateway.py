import csv
from datetime import datetime


class Gateway:
    def __init__(self, log_file="gateway_log.csv"):
        self.log_file = log_file

        # Initializing CSV file with headers
        with open(self.log_file, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["timestamp","device","size","direction","protocol","burst",])

            writer.writeheader()

    def log_packet(self, packet):
        packet["timestamp"] = datetime.now().isoformat()
        with open(self.log_file, mode="a", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["timestamp","device","size","direction","protocol","burst"])

            writer.writerow(packet)
