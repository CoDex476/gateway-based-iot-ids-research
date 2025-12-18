# AI-Driven Lightweight Intrusion Detection System for Resource-Constrained IoT Networks

## Overview
This project investigates the design of a lightweight, gateway-based intrusion detection system (IDS) for resource-constrained IoT environments, with a focus on smart home deployments common in Ghana and similar regions.

Rather than deploying security mechanisms directly on low-cost IoT devices or relying on cloud-based analysis, the proposed system performs traffic-based anomaly detection at the network gateway using minimal flow-level features. This approach reduces computational overhead, preserves device resources, and aligns with real-world deployment constraints.

## Motivation
Consumer IoT devices are increasingly adopted in homes and small organizations, yet they often lack adequate built-in security due to limited memory, processing power, and energy constraints. Traditional security solutions are impractical in such environments.

This project explores whether abnormal or malicious behavior can be reliably detected by observing lightweight network traffic patterns at the gateway, without inspecting payloads or modifying device firmware.

## Key Characteristics
- Gateway-level intrusion detection
- Lightweight, flow-based traffic features
- Simulation-based dataset generation
- Focus on realistic smart home IoT environments
- Context-aware design for Ghanaian deployments

## Project Status
- ✅ System understanding and threat modeling completed
- ✅ Device behavior and attack patterns defined
- ✅ Gateway-level feature selection finalized
- 🔄 Simulation and dataset generation (in progress)

## Repository Structure
- `docs/` – Research notes, system design, and documentation
- `simulation/` – Traffic generation and attack simulation scripts
- `data/` – Generated datasets and labels
- `notebooks/` – Exploratory analysis and experiments

## Research Direction
The project aims to evaluate whether AI-based anomaly detection models trained on simulated gateway-level traffic can generalize to realistic smart home IoT scenarios while remaining computationally efficient.

