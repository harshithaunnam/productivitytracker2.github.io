import tkinter as tk
import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root = tk.Tk()
root.geometry("500x500+450+150")
root.title("Productivity Tracker")

font_style = ("Times", 9)

# Start Time Label
start_time_label = tk.Label(root, text="Start Time:", font= font_style)
start_time_label.place(x=20, y=20)

# Start Time Entry Box
start_time_entry = tk.Entry(root, font= font_style)
start_time_entry.place(x=100, y=20)

# End Time Label
end_time_label = tk.Label(root, text="End Time:", font= font_style)
end_time_label.place(x=20, y=50)

# End Time Entry Box
end_time_entry = tk.Entry(root, font= font_style)
end_time_entry.place(x=100, y=50)

# Pie Chart Label
chart_label = tk.Label(root, text="Pie Chart", font= font_style)
chart_label.place(x=250, y=20)

def create_chart():
    # Get the time difference
    start_time = datetime.datetime.strptime(start_time_entry.get(), "%H:%M:%S")
    end_time = datetime.datetime.strptime(end_time_entry.get(), "%H:%M:%S")
    time_difference = end_time - start_time
    time_difference_seconds = time_difference.seconds

    # Create the labels and values for the pie chart
    labels = ["Productive Time", "Non-Productive Time"]
    productive_time = time_difference_seconds // 2
    non_productive_time = time_difference_seconds - productive_time
    values = [productive_time, non_productive_time]

    # Create the pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    plt.show()




# Create Chart Button
chart_button = tk.Button(root, text="Create Chart", command=create_chart, font= font_style)
chart_button.place(x=20, y=100)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=root.quit, font= font_style)
exit_button.place(x=100, y=100)

# Goals Label
goals_label = tk.Label(root, text="Goals:", font= font_style)
goals_label.place(x=20, y=150)

# Goals Entry Box
goals_entry = tk.Entry(root)
goals_entry.place(x=100, y=150)

# Reminder Label
reminder_label = tk.Label(root, text="Reminder:", font= font_style)
reminder_label.place(x=20, y=200)

# Reminder Entry Box
reminder_entry = tk.Entry(root, font= font_style)
reminder_entry.place(x=100, y=200)

# Add Colors
root.config(bg="#1F2833")

# Start Time Label Color
start_time_label.config(bg="#1F2833", fg="#C5C6C7")

# Start Time Entry Box Color
start_time_entry.config(bg="#C5C6C7", fg="#1F2833")

# End Time Label Color
end_time_label.config(bg="#1F2833", fg="#C5C6C7")

# End Time Entry Box Color
end_time_entry.config(bg="#C5C6C7", fg="#1F2833")

# Pie Chart Label Color
chart_label.config(bg="#1F2833", fg="#C5C6C7")

# Create Chart Button Color
chart_button.config(bg="#C5C6C7", fg="#1F2833")

# Exit Button Color
exit_button.config(bg="#C5C6C7", fg="#1F2833")

# Goals Label Color
goals_label.config(bg="#1F2833", fg="#C5C6C7")

# Goals Entry Box Color
goals_entry.config(bg="#C5C6C7", fg="#1F2833")

# Reminder Label Color
reminder_label.config(bg="#1F2833", fg="#C5C6C7")

# Reminder Entry Box Color
reminder_entry.config(bg="#C5C6C7", fg="#1F2833")


def add_goal():
    goal = goals_entry.get()
    if goal:
        goal_box = tk.Label(root, text=f"Goal: {goal}", font= font_style)
        goal_box.place(x=20, y=250+len(goals_list)*25)
        goals_list.append(goal)

def add_reminder():
    reminder = reminder_entry.get()
    if reminder:
        reminder_box = tk.Label(root, text=f"Reminder: {reminder}", font= font_style)
        reminder_box.place(x=200, y=250+len(reminders_list)*25)
        reminders_list.append(reminder)

# Goals Add Button
add_goal_button = tk.Button(root, text="Add", command=add_goal, font= font_style)
add_goal_button.place(x=250, y=150)

# Reminder Add Button
add_reminder_button = tk.Button(root, text="Add", command=add_reminder, font= font_style)
add_reminder_button.place(x=250, y=200)

# Lists to store goals and reminders
goals_list = []
reminders_list = []


# Run the application
root.mainloop()