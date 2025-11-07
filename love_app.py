import streamlit as st
import random

# 💜 Page setup
st.set_page_config(page_title="Love Compatibility App 💖", page_icon="💘", layout="centered")

# 🌸 Custom aesthetic CSS styling
st.markdown("""
    <style>
    /* Background gradient */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #a4508b, #5f0a87);
        color: white;
        font-family: 'Poppins', sans-serif;
    }

    /* Input and button styling */
    input {
        border-radius: 12px !important;
        border: 1px solid #fff !important;
        padding: 10px !important;
        color: #4b0082 !important;
        font-weight: 500;
    }

    button[kind="secondary"] {
        background: #fff;
        color: #4b0082;
        border-radius: 12px;
        border: none;
        font-weight: 600;
    }

    button[kind="secondary"]:hover {
        background: #ffb6f9;
        color: #fff;
        transform: scale(1.05);
        transition: 0.3s ease;
    }

    /* Titles */
    h1, h2, h3 {
        font-family: 'Pacifico', cursive;
        text-shadow: 2px 2px 6px rgba(255,255,255,0.3);
    }

    /* Footer */
    footer, .stCaption {
        color: rgba(255,255,255,0.7);
        text-align: center;
    }

    </style>
""", unsafe_allow_html=True)

# 💖 Title
st.markdown("<h1 style='text-align: center;'>💜 Love Compatibility Calculator 💜</h1>", unsafe_allow_html=True)
st.write("✨ Find out how compatible you are with your crush! ✨")

# 💌 Inputs
name = st.text_input("Enter your name:")
crush_name = st.text_input("Enter your crush's name:")

# 💘 Button
if st.button("💞 Check Compatibility 💞"):
    if name and crush_name:
        percentage = random.randint(1, 100)
        st.markdown(f"<h2 style='text-align:center;'>💖 {name} and {crush_name} have {percentage}% love compatibility 💖</h2>", unsafe_allow_html=True)
        
        if percentage > 70:
            st.success("You love each other like Romeo and Juliet! 💞")
        elif percentage > 40:
            st.info("You have a good chance together! 💕")
        else:
            st.warning("Not very compatible... but love can grow! 🌱")
    else:
        st.error("Please enter both names to continue 💬")

st.markdown("---")
st.caption("💘 Made with love using Streamlit 💘")

