import streamlit as st
import random

st.title("Stone Paper Scissors Game 🎮")

# Score variables stored in session state
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0
if "player_score" not in st.session_state:
    st.session_state.player_score = 0

choices = ["stone", "paper", "scissor"]

player_choice = st.selectbox("Choose your move:", choices)
if st.button("Play"):
    computer_choice = random.choice(choices)
    st.write("**Computer:**", computer_choice)

    if (computer_choice == "stone" and player_choice == "scissor") or \
       (computer_choice == "scissor" and player_choice == "paper") or \
       (computer_choice == "paper" and player_choice == "stone"):
        st.session_state.computer_score += 1
        st.error("Computer won 😈")
    elif (player_choice == "stone" and computer_choice == "scissor") or \
         (player_choice == "scissor" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "stone"):
        st.session_state.player_score += 1
        st.success("Hurrah! You won 🎉")
    else:
        st.info("It's a tie 🤝")

st.subheader("Scoreboard")
st.write(f"**Computer:** {st.session_state.computer_score}")
st.write(f"**Player:** {st.session_state.player_score}")

if st.button("Restart Game"):
    st.session_state.computer_score = 0
    st.session_state.player_score = 0
