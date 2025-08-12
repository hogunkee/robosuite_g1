# Robosuite-G1

**Robosuite-G1** is an adaptation of [Robosuite](https://github.com/ARISE-Initiative/robosuite) for the **Unitree G1 humanoid robot**.
This repository adds G1’s robot model and assets into Robosuite’s modular simulation framework, enabling the use of G1 for a wide variety of manipulation tasks.

---

## Overview

Robosuite-G1 enables:
- Simulation of Unitree G1 in all Robosuite tasks (single-arm and dual-arm capable)
- Custom G1-specific tabletop and manipulation environments
- Easy integration with RL libraries for policy training

---

## Key Changes from Original Robosuite
- Integrated **G1 URDF** and mesh assets into Robosuite’s robot model registry
- Implemented G1-specific controllers and joint limit configurations
- Added G1-adapted tabletop environments (e.g., LiftG1, StackG1)
- Updated XML scene definitions for G1 proportions

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hogunkee/robosuite_g1
   cd robosuite_g1
   pip install -e .

