import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Class Groups", page_icon="👥")

# Header
st.title("Class Groups")

# Function to load and display the image
def display_class_group_image():
    # Define the path to the image file
    image_path = r"C:\Users\DAMBAZAU\Desktop\Christ\Fakers\fakers\utilities\group.png"
    
    # Display the image
    st.image(image_path, caption="Group Image")

# Call the function to display the class group image
display_class_group_image()
