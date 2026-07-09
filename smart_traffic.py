import heapq
import tkinter as tk
from tkinter import messagebox


graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5, 'E': 10},
    'C': {'B': 1, 'D': 8},
    'D': {'E': 2},
    'E': {}
}


heuristic = {
    'A': 7,
    'B': 3,
    'C': 4,
    'D': 2,
    'E': 0
}


def a_star(start, goal):
    pq = []
    heapq.heappush(pq, (0, start))

    cost = {start: 0}
    parent = {}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            break

        for neighbor in graph[current]:
            new_cost = cost[current] + graph[current][neighbor]

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(pq, (priority, neighbor))
                parent[neighbor] = current

    
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = parent.get(node)
        if node is None:
            return None, None
    path.append(start)
    path.reverse()

    return path, cost[goal]

def find_path():
    start = entry_start.get().upper()
    goal = entry_goal.get().upper()

    if start not in graph or goal not in graph:
        messagebox.showerror("Error", "Invalid nodes!")
        return

    path, cost = a_star(start, goal)

    if path:
        result_label.config(text=f"Path: {' → '.join(path)}\nCost: {cost}")
    else:
        result_label.config(text="No path found!")


root = tk.Tk()
root.title("Smart Traffic Navigation System")
root.geometry("400x300")

tk.Label(root, text="Enter Start Node:").pack()
entry_start = tk.Entry(root)
entry_start.pack()

tk.Label(root, text="Enter Goal Node:").pack()
entry_goal = tk.Entry(root)
entry_goal.pack()

tk.Button(root, text="Find Path", command=find_path).pack(pady=10)

result_label = tk.Label(root, text="", fg="blue")
result_label.pack()

root.mainloop()
