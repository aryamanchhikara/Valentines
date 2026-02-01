import streamlit as st
import random

st.set_page_config(page_title="Important Question 💌", page_icon="💖")

st.title("To My Baby Ally")
st.subheader("I have a very important question...")

st.write("Before you answer I want you to know:")
st.write("• You are the love of my life")
st.write("• You are my precious and My Love")
st.write("• This question determines my happiness level 📈")

st.divider()

st.header("Will you please be my Valentine?")

# Session state to track 
if "answer" not in st.session_state:
    st.session_state.answer = None

col1, col2 = st.columns(2)

with col1:
    if st.button("YES 🥰"):
        st.session_state.answer = "yes"

with col2:
    if st.button("No 🙄"):
        responses = [
            "Wrong answer please say yes Bruh ",
            "The 'No' button is broken say yes ",
            "system will say error babe ",
            "Are you sureeee? No, come on baby girl",
            
        ]
        st.warning(random.choice(responses))

# okay so say yes 
if st.session_state.answer == "yes":
    st.balloons()
    st.success("YAYYYYYY hell yeah  Best decision ever babay girl")
    st.write("Date secureddddddddddd")

    st.write("This is me to you baby girlll:")
    st.image("https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif", caption="Us fr")

st.divider()
st.caption("Made with love by your Love Cookie")
