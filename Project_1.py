import streamlit as st
import pandas as pd
import time
import os

# CSV file paths
CONSENT_CSV = "data/consent.csv"
DEMOGRAPHIC_CSV = "data/demographic.csv"
TASK_CSV = "data/task.csv"
EXIT_CSV = "data/exit.csv"

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Initialize CSVs with headers if they don't exist
def initialize_csv(path, headers):
    if not os.path.exists(path):
        pd.DataFrame(columns=headers).to_csv(path, index=False)

initialize_csv(CONSENT_CSV, ["Timestamp", "Consent Given"])
initialize_csv(DEMOGRAPHIC_CSV, ["Timestamp", "Name", "Age", "Occupation", "Familiarity"])
initialize_csv(TASK_CSV, ["Timestamp", "TasK Name", "Success", "Duration Seconds", "Notes"])
initialize_csv(EXIT_CSV, ["Timestamp", "Satisfaction", "Difficulty", "Open Feedback"])

# App layout
st.set_page_config(page_title="Usability Testing Tool", layout="wide")
st.title("Usability Testing Tool")

# Tabs
tabs = st.tabs(["Consent", "Demographic", "Tasks", "Exit Survey", "Report"])

# Consent Tab
with tabs[0]:
    st.header("Consent Form")
    consent = st.checkbox("I agree to participate in this usability study.")
    if st.button("Submit Consent"):
        timestamp = pd.Timestamp.now()
        pd.DataFrame([[timestamp, consent]], columns=["Timestamp", "Consent Given"]).to_csv(CONSENT_CSV, mode="a", header=False, index=False)
        st.success("Consent recorded.")

# Demographic Tab
with tabs[1]:
    st.header("Demographic Questionnaire")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, step=1)
    occupation = st.text_input("Occupation")
    familiarity = st.selectbox("How familiar are you with this type of app?", ["Not Familiar", "Somewhat Familiar", "Very Familiar"])

    if st.button("Submit Demographics"):
        timestamp = pd.Timestamp.now()
        pd.DataFrame([[timestamp, name, age, occupation, familiarity]], columns=["Timestamp", "Name", "Age", "Occupation", "Familiarity"]).to_csv(DEMOGRAPHIC_CSV, mode="a", header=False, index=False)
        st.success("Demographics recorded.")

# Tasks Tab
with tabs[2]:
    st.header("Task Performance")

    task_name = st.text_input("Task Name", value="Task 1: Example Task")
    start = st.button("Start Task")
    stop = st.button("End Task")

    if "start_time" not in st.session_state:
        st.session_state.start_time = None

    if start:
        st.session_state.start_time = time.time()
        st.info("Task started!")

    if stop and st.session_state.start_time:
        end_time = time.time()
        duration = round(end_time - st.session_state.start_time, 4)
        success = st.selectbox("Was the task successful?", ["Yes", "No", "Partial"])
        notes = st.text_area("Notes")
        timestamp = pd.Timestamp.now()
        pd.DataFrame([[timestamp, task_name, success, duration, notes]], columns=["Timestamp", "Task Name", "Success", "Duration Seconds", "Notes"]).to_csv(TASK_CSV, mode="a", header=False, index=False)
        st.success(f"Task completed in {duration} seconds.")
        st.session_state.start_time = None

# Exit Survey Tab
with tabs[3]:
    st.header("Exit Questionnaire")
    satisfaction = st.slider("How satisfied are you with the app?", 1, 5, 3)
    difficulty = st.slider("How difficult was the app to use?", 1, 5, 3)
    feedback = st.text_area("Any other feedback?")

    if st.button("Submit Exit Survey"):
        timestamp = pd.Timestamp.now()
        pd.DataFrame([[timestamp, satisfaction, difficulty, feedback]], columns=["Timestamp", "Satisfaction", "Difficulty", "Open Feedback"]).to_csv(EXIT_CSV, mode="a", header=False, index=False)
        st.success("Exit survey recorded.")

# Report Tab
with tabs[4]:
    st.header("Usability Report - Aggregated Results")

    st.subheader("Consent Data")
    try:
        st.dataframe(pd.read_csv(CONSENT_CSV))
    except Exception as e:
        st.error(f"Error loading consent data: {e}")

    st.subheader("Demographic Data")
    try:
        st.dataframe(pd.read_csv(DEMOGRAPHIC_CSV))
    except Exception as e:
        st.error(f"Error loading demographic data: {e}")

    st.subheader("Task Performance Data")
    try:
        st.dataframe(pd.read_csv(TASK_CSV))
    except Exception as e:
        st.error(f"Error loading task data: {e}")

    st.subheader("Exit Questionnaire Data")
    try:
        st.dataframe(pd.read_csv(EXIT_CSV))
    except Exception as e:
        st.error(f"Error loading exit survey data: {e}")

