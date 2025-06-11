# 📘 Project Overview — Wisdom Bar Graph

The **Wisdom Bar Graph** project is built around the [RoboCore BlackBoard Wisdom](https://www.robocore.net/placa-robocore/blackboard-wisdom) and focuses on controlling the **Bar Graph component**, a set of 4 LEDs designed to represent visual levels (20%, 50%, 75%, 100%).

This document provides a technical overview of the project’s structure, functionality, and future scope.

---

## 🔧 Hardware Components

- **Bar Graph (4 LEDs)** — 20%, 50%, 75%, 100% indicators
- **ESP32** — Built-in microcontroller
- Optional integrations:
  - Temperature & humidity sensor
  - Proximity sensor
  - Sound sensor
  - Slide potentiometer

---

## 🧠 Functional Goal

Display data from input sources (e.g. analog sensor values) in a bar graph format using the 4 LEDs:
| LED | Value Range       |
|-----|-------------------|
| 1   | 0% - 20%          |
| 2   | 21% - 50%         |
| 3   | 51% - 75%         |
| 4   | 76% - 100%        |

Each LED represents a level of intensity based on the input signal or sensor reading.

---

## 📂 Project Structure

wisdom-bar-graph/
├── docs/
│ └── overview.md ← You are here!
├── src/
│ └── main.py ← Core logic for LED control
├── README.md ← Public-facing intro
├── LICENSE ← MIT license
