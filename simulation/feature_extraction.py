import csv
from collections import defaultdict
from statistics import mean
from datetime import datetime

INPUT_FILE = "week2_day3_gateway_traffic.csv"
OUTPUT_FILE = "week2_day4_features.csv"

TIME_WINDOW_SECONDS = 5


def parse_time(ts):
    return datetime.fromisoformat(ts)


def main():
    print("[*] Extracting gateway-level features...")

    buckets = defaultdict(list)

    # read raw traffic data
    with open(INPUT_FILE, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            timestamp = parse_time(row["timestamp"])
            window = int(timestamp.timestamp()) // TIME_WINDOW_SECONDS

            key = (window, row["device"])
            buckets[key].append(row)

    # write features to output file
    with open(OUTPUT_FILE, mode="w", newline="") as file:
        fieldnames = ["time_window","device","packet_count","avg_packet_size","max_packet_size",
                      "unique_directions","burst_rate","label","attack_type"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for (window, device), packets in buckets.items():
            sizes = [int(p["size"]) for p in packets]
            directions = set(p["direction"] for p in packets)
            bursts = sum(1 for p in packets if p["label"] == "attack")

            writer.writerow(
                {
                    "time_window": window,
                    "device": device,
                    "packet_count": len(packets),
                    "avg_packet_size": round(mean(sizes), 2),
                    "max_packet_size": max(sizes),
                    "unique_directions": len(directions),
                    "burst_rate": bursts / len(packets),
                    "label": packets[0]["label"],
                    "attack_type": packets[0]["attack_type"],
                }
            )

    print("[**] Feature extraction completed.")
    print(f"[**] Output saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
