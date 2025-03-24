import tkinter as tk
from tkinter import messagebox
from deadlock import DeadlockDetector
from visualizer import show_graph

class DeadlockGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Deadlock Detection Tool")

        self.detector = DeadlockDetector()

        # Labels & Input Fields
        tk.Label(root, text="Process 1:").grid(row=0, column=0)
        tk.Label(root, text="Process 2:").grid(row=1, column=0)

        self.process1_entry = tk.Entry(root)
        self.process2_entry = tk.Entry(root)
        self.process1_entry.grid(row=0, column=1)
        self.process2_entry.grid(row=1, column=1)

        # Buttons
        tk.Button(root, text="Add Dependency", command=self.add_dependency).grid(row=2, column=0, columnspan=2)
        tk.Button(root, text="Detect Deadlock", command=self.detect_deadlock).grid(row=3, column=0, columnspan=2)
        tk.Button(root, text="Show Graph", command=self.show_graph).grid(row=4, column=0, columnspan=2)

    def add_dependency(self):
        p1 = self.process1_entry.get().strip()
        p2 = self.process2_entry.get().strip()

        if p1 and p2:
            self.detector.add_dependency(p1, p2)
            messagebox.showinfo("Success", f"Dependency {p1} → {p2} added!")
        else:
            messagebox.showerror("Error", "Please enter valid process names!")

    def detect_deadlock(self):
        deadlock_cycle = self.detector.detect_deadlock()
        if deadlock_cycle:
            messagebox.showwarning("Deadlock Detected", f"Deadlock found in cycle: {' → '.join(deadlock_cycle)}")
        else:
            messagebox.showinfo("No Deadlock", "No deadlock detected.")

    def show_graph(self):
        show_graph(self.detector.graph)

if __name__ == "__main__":
    root = tk.Tk()
    gui = DeadlockGUI(root)
    root.mainloop()
