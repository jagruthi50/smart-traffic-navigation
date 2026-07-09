# Smart Traffic Navigation System using A* Search Algorithm

## Overview

The Smart Traffic Navigation System is a Python-based desktop application that finds the shortest path between a source and destination using the A* Search Algorithm. The application provides a simple graphical user interface (GUI) built with Tkinter, allowing users to enter start and destination nodes and view the optimal route along with its total cost.

## Features

- Shortest path calculation using the A* Search Algorithm
- Graph-based route planning
- Heuristic-based path optimization
- Interactive Tkinter GUI
- Displays optimal path and total travel cost
- Simple and easy-to-use interface

## Technologies Used

- Python
- Tkinter
- Heapq
- A* Search Algorithm

## Project Structure

```
smart-traffic-navigation/
│── smart_traffic.py
│── README.md
│── requirements.txt
│── screenshots/
```

## Algorithm

The project uses the A* Search Algorithm to determine the shortest path.

The evaluation function is:

```
f(n) = g(n) + h(n)
```

where:

- g(n) = Actual cost from the start node
- h(n) = Estimated cost to the goal (heuristic)

The algorithm expands the node with the lowest evaluation value until the destination is reached.

## Graph Used

```
A → B (4)
A → C (2)
C → B (1)
C → D (8)
B → D (5)
B → E (10)
D → E (2)
```

## Heuristic Values

| Node | Heuristic |
|------|-----------|
| A | 7 |
| B | 3 |
| C | 4 |
| D | 2 |
| E | 0 |

## How to Run

Clone the repository

```bash
git clone https://github.com/jagruthi50/smart-traffic-navigation.git
```

Navigate to the project folder

```bash
cd smart-traffic-navigation
```

Run the application

```bash
python smart_traffic.py
```

## Sample Output

Input

Start Node: A

Goal Node: E

Output

Path:
A → C → B → D → E

Cost:
10

## Future Enhancements

- Interactive map visualization
- Real-time traffic updates
- Dynamic graph generation
- GPS integration
- Multiple route suggestions
- Better GUI design

## Author

Jagruthi Suneel Mundlapati

B.Tech Computing Technologies

SRM Institute of Science and Technology
