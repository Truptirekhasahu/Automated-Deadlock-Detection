"Automated Deadlock Detection Tool"

Overview: The Automated Deadlock Detection Tool is meant to examine process dependency and resource allocation within a system to identify potential deadlocks. The tool uses graph-based analysis to determine circular wait conditions and offers resolution strategies.

Deadlock: A deadlock happens when two or more programs (or processes) are stuck waiting for each other to release resources, and they never move forward. Imagine two people trying to pass through a narrow door at the same time, but both refuse to step back—nobody can move, and they remain stuck.

📂 File Structure

📁 automated-deadlock/ │-- 📄 app.py # Main application GUI │-- 📄 deadlock.py # Deadlock detection logic │-- 📄 visualization.py # Graph visualization of process dependencies │-- 📄 database.py # SQLite database for logging detected deadlocks │-- 📄 requirements.txt # List of required dependencies │-- 📄 README.md # Documentation (this file)

Features:

Dynamic addition of process dependencies through GUI Interface (based on Tkinter).
Deadlock Detection Algorithm implemented using NetworkX library.
Graphical Visualization of process-resource allocation.
Database Logging to record detected deadlocks.
Installation & Setup

1.Clone the Repository:

git clone https://github.com/yourusername/automated-deadlock.git cd automated-deadlock

2.Install Dependencies: pip install -r requirements.txt

3.Run the Application python app.py

Usage Guide: 1.Enter Process Names: For example, P1, P2, etc. 2.Add Dependencies: Choose two processes to create a resource dependency. 3.Detect Deadlock: Click on "Detect Deadlock" to identify circular wait conditions. 4.Show Graph: Display the dependency graph.

Technologies Used: -Python 3.x -Tkinter(GUI Interface) -NetworkX(Graph-based Deadlock Detection) -Matplotlib(Visualization) -SQLite3(Database Logging)
