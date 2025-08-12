# Robosuite-G1

**Robosuite-G1** is an adaptation of [Robosuite](https://github.com/ARISE-Initiative/robosuite) for the **Unitree G1 humanoid robot**.
This repository adds G1’s robot model and assets into Robosuite’s modular simulation framework, enabling the use of G1 for a wide variety of manipulation tasks.

---

## Overview

Robosuite-G1 enables:
- Simulation of Unitree G1 in Robosuite tasks
- Add Unitree G1 humanoid robot and Unitree Dex3-1 hand.

---

## Key Changes from Original Robosuite
- Integrated **G1 URDF** and mesh assets into Robosuite’s robot model registry
- Integrated **Dex3-1 Hands** and mesh assets
- Implemented G1-specific controllers and joint limit configurations
- Updated XML scene definitions for G1 + Dex3-1 proportions

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hogunkee/robosuite_g1
   cd robosuite_g1
   pip install -e .

