import streamlit as st
from datetime import datetime

# Create a class for tasks
class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority

    def __str__(self):
        return f"{self.description} (Due: {self.due_date}, Priority: {self.priority.capitalize()})"

# Create an empty list to store tasks
tasks = []

# Streamlit app
st.title("To-Do List")

# Get the number of tasks from the user
num_tasks = st.number_input("Enter the number of tasks:", min_value=1, step=1)

# Prompt the user to input task details
for i in range(1, num_tasks + 1):
    st.subheader(f"Task {i}:")
    description = st.text_input(f"Enter the task description for Task {i}:", key=f"description_{i}")
    due_date = st.text_input(f"Enter the due date for Task {i} (YYYY-MM-DD):", key=f"date_{i}")
    priority = st.selectbox(f"Select the priority for Task {i}:", ["important", "not important"], key=f"priority_{i}")
    tasks.append(Task(description, due_date, priority))

# Function to convert the date string to datetime
def convert_to_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None

# Filter out tasks with invalid dates
valid_tasks = [task for task in tasks if convert_to_date(task.due_date) is not None]

# Sort tasks by due date and priority
sorted_tasks = sorted(valid_tasks, key=lambda x: (convert_to_date(x.due_date), x.priority == "not important"), reverse=False)

# Display the sorted tasks
st.subheader("Sorted Tasks:")
for task in sorted_tasks:
    st.write(str(task))

def main():
    menu = ["Create","Read","Update","Delete","About"]
    choice = st.sidebar.selectbox("Menu",menu)
    create_table()
