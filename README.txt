# README.txt

---

## Input Datasets
The first four datasets (located in the Input folder) are used to answer the following “What-if” scenarios:

1. Dataset 1: What if high temperatures and low soil moisture?
2. Dataset 2: What if low temperatures and high soil moisture?
3. Dataset 3: What if mild temperatures and high soil moisture?
4. Dataset 4: What if mild temperatures and low soil moisture?

You can add more datasets to explore additional scenarios. The app can then be run in simulation mode, allowing you to select any new dataset to test different conditions.

---

## Micro:Bit Directory Overview
This directory (Micro:Bit) stores the code used by the Micro:Bit.

It contains:
- A Python sample script
- Two ready-to-use `.hex` files for uploading to the Micro:Bit

---

## Hex File Differences
The two `.hex` files differ in the threshold used to detect moisture:

1. microbit-test-at-home.hex
   - A moisture level higher than 30 is enough to detect moisture.

2. microbit-Wildfire-Risk-Detection.hex
   - A moisture level higher than 300 is enough to detect moisture.

---
