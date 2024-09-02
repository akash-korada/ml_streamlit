import streamlit as st
from datetime import datetime

# Title of the application
st.title("Age Calculator")

# Input field to enter the birthdate
birth_date = st.date_input("Enter your birthdate:")

# Calculate age
if st.button("Calculate Age"):
    today = datetime.today()
    
    # Calculate the difference between the current date and the birthdate
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    
    # Display the age
    st.success(f"You are {age} years old.")

# Footer
st.write("Powered by Streamlit")
