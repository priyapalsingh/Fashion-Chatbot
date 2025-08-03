import streamlit as st
import google.generativeai as genai

# ✅ Gemini API Key config
genai.configure(api_key="AIzaSyAMV9qbRi7RpCrp9XNzMAYY3J6-AWbxSmE")

# 🔧 Gemini model instance
model = genai.GenerativeModel("gemini-1.5-pro")

# 🌐 Streamlit Web App
st.set_page_config(page_title="Fashion Advice Chatbot")
st.title("👗 Fashion Advisor Chatbot")

user_input = st.text_input("Ask me something about fashion:")

if user_input:
    try:
        with st.spinner("Thinking..."):
            response = model.generate_content(
                f"You are a helpful fashion advisor. Answer this: {user_input}"
            )
            st.success("Here's your fashion advice:")
            st.write(response.text.strip())
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
