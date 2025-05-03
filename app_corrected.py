
import streamlit as st
import requests

# Title
st.title("AI Model API Generator")

# Model Selection
st.header("Select a Model")
model_name = st.selectbox(
    "Choose a model:",
    ["distilbert-sentiment", "summarization", "emotion-detection"]
)

# Text Input
st.header("Enter Text for Prediction")
user_input = st.text_area("Input your text here:")

# Prediction Button
if st.button("Get Prediction"):
    if user_input and model_name:
        with st.spinner("Getting prediction from API..."):
            url = "https://ai-api-generator-1.onrender.com/predict-text"
            payload = {
                "model_name": model_name,
                "text": user_input
            }
            try:
                response = requests.post(url, json=payload)
                if response.status_code == 200:
                    result = response.json()
                    if "model_used" in result and "task" in result and "result" in result:
                        st.success("Prediction received successfully!")
                        st.write("**Model Used:**", result["model_used"])
                        st.write("**Task:**", result["task"])
                        st.write("**Result:**")
                        st.json(result["result"])
                    else:
                        st.error("Unexpected API response format.")
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Request failed: {e}")
    else:
        st.warning("Please select a model and enter some text to continue.")
