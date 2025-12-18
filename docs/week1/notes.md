# AI-Driven Lightweight Intrusion Detection System for Resource-Constrained IoT Networks

I am designing an AI-driven intrusion detection system for resource-constrained IoT environments (smart homes), where heterogeneous consumer devices communicate through a central gateway. Because individual IoT devices lack the computational and energy resources to run complex security mechanisms, my system performs lightweight, traffic-based anomaly detection at the gateway, using minimal flow-level features rather than payload inspection. Normal and malicious traffic patterns will be generated in a simulation environment, logged at the gateway, and used to train and evaluate AI models capable of identifying deviations caused by attacks such as botnet infections, flooding, and device impersonation.

## Why?

With the increasing adoption of low-cost IoT devices in Ghanaian homes and small organizations, this project proposes a lightweight, AI-driven gateway-level intrusion detection system that provides effective network security for resource-constrained devices, eliminating device-level overhead and dependence on cloud-based solutions.

---

## 1. System Understanding

### What problem does IoT solve?

The Internet of Things enables physical devices within everyday environments to sense, communicate, and act autonomously. In smart homes, IoT reduces the need for constant human intervention by enabling remote monitoring, automation, and data-driven decision-making for comfort, safety, and energy efficiency. Applications include home security, environmental monitoring, energy management, and assisted living.

### How does data flow end-to-end in an IoT system?

IoT data follows this pipeline:

Sensor → Embedded Device (Microcontroller Unit) → Home Gateway → Network (Internet) → Cloud/Server → Application/User



Data is generated either periodically or in bursts, transmitted using lightweight protocols, processed at the gateway or cloud, and then used to trigger automated actions or user notifications.

**What assumptions do IoT systems make? (Unrealistic)**  
Most IoT systems implicitly assume that:  
- Devices are trusted once deployed  
- Network communication is benign  
- Firmware and software remain uncompromised  
- Home gateways act honestly as intermediaries  

These assumptions are particularly fragile in smart homes, where devices are often consumer-grade and exposed to the internet.

---

## 2. Security Lens

**Where can IoT systems fail or be attacked?**  
Smart home IoT systems expose multiple attack surfaces:  
- Weak or absent device authentication  
- Unencrypted or poorly secured communication channels  
- Insecure firmware update mechanisms  
- Compromised gateways acting as attack amplifiers  
- Centralized cloud services are becoming single points of failure  

Because smart home devices are deployed in uncontrolled residential environments, both physical access and remote exploitation are realistic threat vectors.

**Which constraints make IoT security difficult?**  
The most critical challenge in smart home IoT security is device resource limitation:  
- Low memory restricts strong cryptographic mechanisms  
- Limited processing power prevents complex security models  
- Energy constraints discourage continuous monitoring  
- Low bandwidth limits frequent security signaling  

These constraints make traditional enterprise security solutions impractical for consumer IoT deployments.

---

## 3. Project Signals (Early Research Direction)

**What does this mean for my project?**  
These observations suggest that IoT security mechanisms must be lightweight, adaptive, and network-aware. Instead of inspecting payloads or deploying heavy models on devices, intrusion detection should rely on traffic patterns, flow-level behavior, and anomalies that can be observed with minimal computational overhead at the gateway.

---

## 4. Open Questions (Research Seeds)

- How can anomalies be reliably identified when smart home IoT traffic is inherently bursty and heterogeneous?  
- What minimal set of traffic features can still provide strong intrusion detection performance?  
- Where is the optimal balance between detection accuracy and computational cost in constrained environments?  
- Can models trained in simulation generalize to real smart home IoT traffic?  

---

# WEEK 1

### Day 1 Note

In many modern homes today, devices such as temperature sensors, motion detectors, smart plugs, lighting controllers, and low-cost IP cameras operate quietly in the background. These devices monitor environmental conditions, control appliances, manage lighting, or stream basic video feeds. They are typically low-cost, resource-constrained, and designed to transmit small amounts of data at regular intervals or in response to events. Rather than communicating directly with cloud services, these devices rely on a home network gateway (router or smart hub), that collects their traffic and forwards it externally. Due to limited memory, processing power, and energy, these devices frequently lack strong built-in security mechanisms and instead depend on the network for protection. Over time, the gateway becomes a critical point of trust, as it observes all inbound and outbound traffic and has greater computational resources than individual devices. This project focuses on such a smart home environment, where multiple heterogeneous devices share a single network, making it a realistic and practical setting for studying lightweight, gateway-based intrusion detection.

---

### Day 2 Note

**IoT Device Behavioral Feature Table (Smart Home)**

| Device Type               | Packet Size   | Frequency           | Direction       | Protocol     | Burst                  | Idle Period        |
|---------------------------|--------------|------------------|----------------|------------|----------------------|-----------------|
| Temperature Sensor        | 50–100 bytes | Every 30 sec       | Device → Gateway | MQTT        | None                  | 30 sec          |
| Motion Sensor             | 60–120 bytes | Event-driven       | Device → Gateway | MQTT        | Small event bursts    | Idle until motion |
| Smart Plug                | 70–150 bytes | Event-driven       | Device ↔ Gateway | CoAP / MQTT | Short bursts on toggle | Idle otherwise  |
| Smart Lighting Controller | 80–200 bytes | Periodic + event-driven | Device ↔ Gateway | CoAP | Small bursts on state change | Idle otherwise |
| Low-Cost IP Camera        | 500–1500 bytes | Event-triggered streaming | Device → Gateway → Cloud | RTSP / TCP | Continuous during streaming | Idle when inactive |
| Home Gateway              | N/A          | Continuous         | Device ↔ Cloud | All above   | Aggregates device bursts | N/A           |

In a smart home environment, most devices generate small, predictable traffic patterns. Sensors transmit periodic updates, while actuators and cameras generate short bursts when triggered. The home gateway aggregates all traffic before forwarding it externally. Any deviation from these baseline behaviors, such as abnormal packet sizes, unexpected burst frequency, or unusual communication directions, may indicate malicious activity. These observable patterns form the basis for lightweight, gateway-based intrusion detection.

---

### Day 3 Note

**Attack Behavior Table**

| Aspect          | Normal Behavior          | Attack Behavior                |
|----------------|------------------------|-------------------------------|
| Packet Frequency | Periodic/event-driven  | Sudden high-frequency bursts  |
| Packet Size      | Small and consistent   | Irregular or unusually large  |
| Destination      | Fixed cloud servers    | Multiple unknown IPs          |
| Timing           | Predictable            | Random or aggressive          |
| Direction        | Mostly device → gateway | Excessive outbound traffic    |
| Idle Periods     | Present                | Largely absent                |

**Device-Specific Attack Table**

| Device Type           | Normal Behavior           | Attack Behavior                       |
|-----------------------|--------------------------|--------------------------------------|
| Temperature Sensor    | Sends updates every 30 sec | Floods gateway with frequent packets |
| Motion Sensor         | Event-driven             | Repeated fake motion events           |
| Smart Plug            | Event-driven             | Unusually high traffic volume         |
| Lighting Controller   | Periodic + event-driven  | Abnormal command timing               |
| Low-Cost IP Camera    | Streams only on motion   | Continuous high traffic               |
| Gateway               | Aggregates traffic       | Overloaded by abnormal patterns      |

In a typical smart home, these devices communicate in low-volume, predictable patterns. When compromised through botnet infection, impersonation, or misuse, these patterns change noticeably. Such deviations are visible at the gateway without deep packet inspection, making gateway-level monitoring a practical and lightweight solution for detecting malicious activity in home IoT networks.

---

### Day 4 Note

**Gateway-Level Feature Table**

| Device Type               | Feature 1         | Feature 2    | Feature 3       | Feature 4         | Feature 5          |
|---------------------------|-----------------|------------|----------------|-----------------|-----------------|
| Temperature Sensor        | Packet frequency | Packet size | Direction      | Idle period      | MAC/IP consistency |
| Motion Sensor             | Packet frequency | Packet size | Burstiness     | Direction        | Idle period       |
| Smart Plug                | Packet frequency | Packet size | Burstiness     | Direction        | Idle period       |
| Lighting Controller       | Packet frequency | Packet size | Burstiness     | Direction        | Idle period       |
| Low-Cost IP Camera        | Packet frequency | Packet size | Burstiness     | Direction        | Idle period       |
| Gateway                   | Aggregated volume | Burst patterns | Device ID consistency | Direction analysis | Timing deviation |

These lightweight features capture timing, volume, and identity anomalies caused by common IoT attacks, while remaining computationally efficient and suitable for resource-constrained environments.

**Justification**  
- Gateway-level monitoring observes all device traffic  
- Lightweight features are sufficient because attacks disrupt timing and volume patterns  
- No payload inspection preserves device resources  
- Aggregation enables scalable monitoring across heterogeneous smart home devices  

---

### Day 5: Simulation Environment & Traffic Generation

**Devices to Simulate**  
- Temperature sensors  
- Motion sensors  
- Smart plugs  
- Lighting controllers  
- Low-cost IP cameras  
- Home gateway (aggregator)

**Environment Assumptions**  
- Residential smart home network  
- Shared Wi-Fi or Ethernet LAN  
- Single gateway aggregating traffic  
- Resource-constrained consumer devices

**Baseline Healthy Network Table**

| Device Type          | Normal Behavior               |
|---------------------|-------------------------------|
| Temperature Sensor  | Small packets every 30 sec    |
| Motion Sensor       | Sends traffic only on motion  |
| Smart Plug          | Event-driven on/off traffic   |
| Lighting Controller | Periodic + event-driven bursts |
| IP Camera           | Streams only on motion        |

**Attack Simulation Table**

| Attack Type           | Traffic Change                         |
|----------------------|----------------------------------------|
| Botnet Infection      | Bursts + multiple external IPs        |
| Device Impersonation  | Fake device mimics real sensor        |
| Flooding / DoS        | Continuous high-frequency traffic     |

**Simulation Tools**  
- Python  
- Scapy  

**Features to Log**  
- Packet frequency  
- Packet size  
- Traffic direction  
- Burstiness/timing  
- Device identity (MAC/IP)

For this project, a simulated smart home IoT network will be created to generate both normal and attack traffic. Devices communicate through a central home gateway, reflecting real-world deployment. Normal traffic follows predictable patterns, while attack scenarios introduce bursts, flooding, or impersonation. All traffic is logged at the gateway using lightweight features, forming a dataset for anomaly detection. This controlled simulation enables the development and evaluation of a gateway-based IDS suitable for resource-constrained smart home IoT environments.

---

### Day 6: System Architecture and IDS Placement

**Findings** establish that a gateway-based intrusion detection system provides the most practical, cost-effective, and deployable security solution for resource-constrained smart home IoT networks in Ghana.

- **The Gateway Is the Most Effective Observation Point**  
The network gateway provides complete visibility into device communication patterns, as all inbound and outbound traffic from heterogeneous IoT devices passes through a single point.

- **Device-Level Intrusion Detection Is Impractical for Consumer IoT**  
Deploying intrusion detection mechanisms directly on IoT devices is not feasible due to limited computational resources, restricted firmware access, and energy constraints typical of low-cost consumer devices.

- **Cloud-Based IDS Introduces Cost, Latency, and Privacy Concerns**  
Cloud-based approaches increase operational costs, depend on stable internet connectivity, and raise data privacy concerns.

- **Gateway-Based IDS Achieves Security without Device Modification**  
The IDS at the gateway can monitor and detect anomalies without changing device hardware or software.

- **Lightweight Feature Monitoring Is Sufficient at the Gateway**  
The gateway has enough computational capability to extract and analyze lightweight, flow-level traffic features (packet frequency, size, timing) without impacting network performance.

- **Gateway-Based IDS Aligns with Ghanaian IoT Deployment Realities**  
Well-suited to consumer-grade routers, limited cybersecurity expertise, and cost-sensitive infrastructure.

---

### Day 7 – Week 0 Summary, Validation & Next-Step Definition

**1. What Was Achieved This Week**  
- Defined problem space: securing resource-constrained smart home IoT networks in Ghana  
- End-to-end understanding of IoT data flow  
- Identified key security weaknesses in consumer IoT deployments  
- Validated gateway-level intrusion detection as core approach  
- Baseline traffic behavior for common smart home IoT devices defined  
- Realistic attack behavior model mapped to observable traffic changes  
- Minimal lightweight feature set for anomaly detection  
- Complete simulation plan for generating normal and malicious traffic

**2. Key Assumptions Confirmed**  
- IoT devices in Ghanaian smart homes cannot support heavy security mechanisms  
- Most attacks manifest as network-level anomalies, not payload content  
- A single gateway provides sufficient visibility for all devices  
- Lightweight features are adequate for detecting abnormal behavior  
- Simulation-based datasets are practical before real deployment

**3. Key Constraints Identified**  
- Limited device resources (CPU, memory, energy)  
- Consumer-grade network hardware  
- Intermittent or unstable internet connectivity  
- Lack of access to device firmware and internal logs  
- Privacy concerns around payload inspection  

These constraints justify the lightweight, gateway-based approach.

**Research Readiness Statement**  
At the end of Day 7, the project is ready for implementation and experimentation. All foundational elements required for building and evaluating an AI-driven lightweight IDS have been established.

---

### 5. Transition to Week 2

Week 2 will focus on:  
- Implementing the simulation environment  
- Generating labeled normal and attack traffic  
- Extracting defined lightweight features  
- Preparing datasets for AI-based anomaly detection models  

No changes to architecture or feature selection are expected unless justified by experimental results.
