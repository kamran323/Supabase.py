import streamlit as st
from supabase import create_client, Client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Supabase client
@st.cache_resource
def init_supabase():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    return create_client(url, key)

# Initialize Streamlit page
st.title("Supabase + Streamlit Demo")

# Add some basic UI elements
st.write("Welcome to the Supabase + Streamlit demo app!")

# Create a sample form
with st.form("sample_form"):
    name = st.text_input("Your Name")
    submit = st.form_submit_button("Submit")
    
    if submit:
        if name:
            st.success(f"Hello {name}!")
        else:
            st.error("Please enter your name")

# Add a section to show Supabase connection status
supabase = init_supabase()
if supabase:
    st.success("Successfully connected to Supabase!")
else:
    st.error("Failed to connect to Supabase")
