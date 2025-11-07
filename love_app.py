import streamlit as st
import random

# 💜 Page setup
st.set_page_config(page_title="Love Compatibility App 💖", page_icon="💘", layout="centered")

# 🌸 Custom CSS Styling
st.markdown("""
    <style>
    /* Background gradient */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #a4508b, #5f0a87);
        color: white;
        font-family: 'Poppins', sans-serif;
    }

    /* Label color */
    label, .stTextInput label {
        color: #ffe6ff !important;
        font-weight: 600;
        font-size: 1.05rem;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
    }

    /* Input boxes */
    .stTextInput>div>div>input {
        background-color: #ffffff !important;
        color: #5f0a87 !important;
        border-radius: 12px !important;
        border: 2px solid #fff !important;
        box-shadow: 0 0 10px rgba(255,255,255,0.4);
        font-weight: 500;
        text-align: center;
    }

    ::placeholder {
        color: #7a1fa2 !important;
        opacity: 0.8;
    }

    /* Button styling */
    div.stButton > button {
        background: linear-gradient(90deg, #d16ba5, #c777b9, #8e54e9);
        color: white;
        border-radius: 25px;
        border: none;
        font-weight: 600;
        padding: 0.6rem 1.5rem;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
    }

    div.stButton > button:hover {
        transform: scale(1.07);
        box-shadow: 0px 6px 15px rgba(255,255,255,0.4);
    }

    /* Custom result message boxes */
    .success-box, .info-box, .warning-box, .error-box {
        padding: 1rem;
        border-radius: 15px;
        text-align: center;
        font-weight: 600;
        color: white;
        margin-top: 1rem;
        box-shadow: 0px 0px 15px rgba(255,255,255,0.2);
    }

    .success-box {
        background: linear-gradient(90deg, #ff9a9e, #fad0c4);
    }
    .info-box {
        background: linear-gradient(90deg, #a18cd1, #fbc2eb);
    }
    .warning-box {
        background: linear-gradient(90deg, #f6d365, #fda085);
        color: #4b0082;
    }
    .error-box {
        background: linear-gradient(90deg, #ff758c, #ff7eb3);
    }

    /* Titles */
    h1, h2, h3 {
        font-family: 'Pacifico', cursive;
        text-shadow: 2px 2px 6px rgba(255,255,255,0.3);
    }

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

# 💘 Button and results
if st.button("💞 Check Compatibility 💞"):
    if name and crush_name:
        percentage = random.randint(1, 100)
        st.markdown(
            f"<h2 style='text-align:center;'>💖 {name} and {crush_name} have {percentage}% love compatibility 💖</h2>",
            unsafe_allow_html=True,
        )

        if percentage > 70:
            st.markdown("<div class='success-box'>You love each other like Romeo and Juliet! 💞</div>", unsafe_allow_html=True)
        elif percentage > 40:
            st.markdown("<div class='info-box'>You have a good chance together! 💕</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='warning-box'>Not very compatible... but love can grow! 🌱</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='error-box'>Please enter both names to continue 💬</div>", unsafe_allow_html=True)

st.markdown("---")
st.caption("💘 Made with love using Streamlit 💘")
