import streamlit as st
from datetime import datetime

# Function to get the date from user input
def get_date():
    while True:
        date_str = st.text_input("Enter the due date (YYYY-MM-DD):")
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            return date
        except ValueError:
            st.error("Invalid date format. Please try again.")

# Function to get the priority from user input
def get_priority():
    while True:
        priority = st.selectbox("Select the priority:", ["important", "not important"])
        return priority

# Create a class for tasks
class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority

    def __str__(self):
        return f"{self.description} (Due: {self.due_date.strftime('%Y-%m-%d')}, Priority: {self.priority.capitalize()})"

# Create an empty list to store tasks
tasks = []

# Streamlit app
st.title("To-Do List")

# Get the number of tasks from the user
num_tasks = st.number_input("Enter the number of tasks:", min_value=1, step=1)

# Prompt the user to input task details
for i in range(1, num_tasks + 1):
    st.subheader(f"Task {i}:")
    description = st.text_input("Enter the task description:")
    due_date = get_date()
    priority = get_priority()
    tasks.append(Task(description, due_date, priority))

# Sort tasks by due date and priority
sorted_tasks = sorted(tasks, key=lambda x: (x.due_date, x.priority == "important"), reverse=False)

# Display the sorted tasks
st.subheader("Sorted Tasks:")
for task in sorted_tasks:
    st.write(str(task))
