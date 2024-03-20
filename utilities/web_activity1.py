import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Dynamic Event Planner", page_icon="📅")

# Header
st.title("Group Task: Building a Dynamic Event Planner")

# Objective section
st.header("Objective:")
st.markdown("To apply the concepts learned in HTML, CSS, and JavaScript by creating a dynamic event planner web application.")

# Task Description section
st.header("Event Scheduler - Task Description:")

# Event Scheduler (Student 1)
st.subheader("Domain Expert (Student 1):")
st.markdown("""
- Research and provide a brief explanation of the significance of event scheduling and management in various domains such as business, education, and personal life.
- Propose innovative features or enhancements to improve the event planning process.
- Answer generic questions related to event scheduling, highlighting its importance and application in real-world scenarios.
""")

# Web Developer (Student 2)
st.subheader("Web Developer (Student 2):")
st.markdown("""
- Create an HTML file that serves as the main interface of the event planner.
- Implement CSS styling to design an attractive and user-friendly interface for the event planner.
- Use JavaScript to add dynamic functionality such as adding, editing, and deleting events, as well as displaying event details and notifications.
""")

# Presenter (Student 3)
st.subheader("Presenter (Student 3):")
st.markdown("""
- Prepare a PowerPoint presentation (PPT) that showcases the features and functionalities of the event planner web application.
- Highlight the significance of event planning and management in various contexts.
- Provide demonstrations and examples to illustrate the practical applications of the event planner in different scenarios.
""")

# Submission Requirements section
st.header("Submission Requirements:")
st.markdown("""
- Each group is required to submit one document that includes:
    - Generic questions related to event scheduling and management (submitted by Student 1).
    - HTML, CSS, and JavaScript files of the event planner web application (submitted by Student 2).
    - PowerPoint presentation (PPT) highlighting the significance of the event planner and demonstrating its features (submitted by Student 3).
- Ensure that the submission is cohesive and represents the collaborative effort of all group members.
- Submit the document by the specified deadline.
""")

# Link to view student groups
st.markdown("<a href='https://your_next_page_url'>View Student Groups</a>", unsafe_allow_html=True)
