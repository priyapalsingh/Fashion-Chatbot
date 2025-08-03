import streamlit as st

# Set page config
st.set_page_config(page_title="Fashion Advisor Chatbot", page_icon="👗", layout="centered")

# Style
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 36px;
            color: #F63366;
        }
        .response-box {
            background-color: #ffe6eb;
            padding: 15px;
            border-radius: 10px;
            margin-top: 10px;
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">👗 Fashion Advisor Chatbot</div>', unsafe_allow_html=True)
st.write("Ask me something about fashion:")

# User input
user_input = st.text_input("")

# Rule-based response logic
def get_advice(message):
    message = message.lower()
    if "party" in message:
        return "For a party, consider wearing a stylish dress or a smart shirt with trousers and accessories."
    elif "interview" in message:
        return "Wear something formal like a blazer, shirt, and pants. Keep colors neutral."
    elif "summer" in message:
        return "Opt for light fabrics like cotton or linen. Wear bright colors and sunglasses!"
    elif "wedding" in message:
        return "A traditional dress or a classy formal outfit would be perfect for a wedding."
    elif "winter" in message:
        return "Layer up with warm coats, boots, and scarves. Keep it cozy and fashionable."
    else:
        return "That's a great question! Try being comfortable and confident in whatever you wear."

# Display result
if user_input:
    advice = get_advice(user_input)
    st.markdown(f'<div class="response-box">{advice}</div>', unsafe_allow_html=True)


