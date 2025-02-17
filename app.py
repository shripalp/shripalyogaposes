import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = openai.OpenAI(api_key=openai_api_key)

# Streamlit App UI
st.title("🧘 Shripal's Yoga Pose Guide")
st.write("Select your goal, and I'll suggest the best yoga poses for you!")

# User selects yoga goal
goal = st.selectbox(
    "Choose your goal:",
    ["Flexibility", "Stress Relief", "Weight Loss", "Strength Building", "Back Pain Relief", "knee problems"]
)

# Function to get AI-generated yoga poses
def get_yoga_poses(goal):
    prompt = f"Suggest 5 yoga poses for {goal}. Include pose names and a brief description and images."
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a yoga instructor."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# Display yoga poses
if st.button("Get Yoga Poses"):
    poses = get_yoga_poses(goal)
    st.write(poses)
