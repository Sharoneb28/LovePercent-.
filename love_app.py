import streamlit as st
import random

st.set_page_config(page_title="Love Compatibility App 💖", page_icon="💘", layout="centered")

st.title("💖 Love Compatibility Calculator 💖")
st.write("Find out your love compatibility with your crush! 💌")

name = st.text_input("Enter your name:")
crush_name = st.text_input("Enter your crush's name:")

if st.button("Check Compatibility"):
    if name and crush_name:
        percentage = random.randint(1, 100)
        st.subheader(f"❤️ {name} and {crush_name} have {percentage}% love compatibility! ❤️")

        if percentage > 70:
            st.success("You love each other like Romeo and Juliet! 💞")
        elif percentage > 40:
            st.info("You have a good chance! 💕")
        else:
            st.warning("Not very compatible... but love can always grow! 🌱")
    else:
        st.error("Please enter both names to continue 💬")

st.markdown("---")
st.caption("Made with 💖 using Streamlit")
