import streamlit as st
import re

# Set page configuration
st.set_page_config(page_title="Regex App", layout="centered")

# Custom CSS to enhance the visual appeal
st.markdown("""
    <style>
    .stTextInput, .stTextArea {
        background-color: #f9f9f9;
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 10px;
        color: #333;
    }
    .stButton button {
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 8px 16px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #0056b3;
    }
    </style>
""", unsafe_allow_html=True)

# Title and header with some styling
st.title("🔍 Innomatics Research Labs Internship Project")
st.markdown("""
    <div style="text-align: center; font-size: 20px; color: #343a40;">
        <strong>Intern Name:</strong> Mohammad Wasiq &emsp; <strong>Intern ID:</strong> IN9240653
    </div>
""", unsafe_allow_html=True)

# Navigation menu with radio buttons
selected_page = st.sidebar.radio("Navigation", ["🔠 Regex App", "📧 Email Validation"])

# Functionality for Regex App
if selected_page == "🔠 Regex App":
    st.header("Regular Expression Tester")

    # User input fields for regex pattern and test string
    with st.expander("Enter your inputs"):
        pattern = st.text_input("Enter your Regex Pattern:", placeholder="e.g., \b\w+\b")
        text = st.text_area("Enter the Test String:", placeholder="Write the text here...", height=150)

    # Stylish button to search for matches
    if st.button("Search"):
        if pattern and text:
            matches = re.findall(rf"{pattern}", text)
            if matches:
                st.success(f"🎉 Found {len(matches)} matches:")
                st.markdown(", ".join([f"`{match}`" for match in matches]))
            else:
                st.warning("😞 No matches found. Try a different pattern!")
        else:
            st.warning("Please enter both a pattern and a test string.")

# Functionality for Email Validation
if selected_page == "📧 Email Validation":
    st.header("Email Validation Tool")

    # User input for email with a placeholder
    email = st.text_input("Enter your Email:", placeholder="e.g., example@domain.com")

    # Email validation pattern
    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[\w]{2,3}$"

    # Button to validate the email
    if st.button("Check Email"):
        if email:
            if re.match(email_pattern, email):
                st.success("✅ Valid email address.")
            else:
                st.error("❌ Invalid email address. Please try again!")
        else:
            st.warning("Please enter an email address to validate.")
