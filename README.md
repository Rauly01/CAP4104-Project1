CAP4104 Usability Testing Tool – Setup Instructions and Overview

Project Overview

This project is a usability testing tool built with Python’s Streamlit framework. It allows users to go through a structured process to evaluate a product or interface. The app collects consent, demographic details, task performance metrics, and post-task feedback. It then generates a simple report with summarized results.

Features

Consent Form – Users agree to participate and share their data.
Demographic Questionnaire – Captures name, age, occupation, and tool familiarity.
Task Module – Users complete a mock task. Time taken, success level, and notes are recorded.
Exit Questionnaire – Gathers satisfaction and difficulty ratings using a Likert scale, plus optional feedback.
Report Page – Displays all collected responses and calculates averages for satisfaction and difficulty.

How to Set Up and Run the App

Step 1 – Install Requirements
Make sure you have the following installed on your system:
Python 3.8 or later
pip (Python package installer)
Open your terminal or Git Bash, and install Streamlit and Pandas:
pip install streamlit pandas

Step 2 – Navigate to the App Folder

Step 3 – Run the App
Once inside the folder, run the following command:
streamlit run Project_1.py
Your default web browser will open automatically, and you will see the app running locally.
