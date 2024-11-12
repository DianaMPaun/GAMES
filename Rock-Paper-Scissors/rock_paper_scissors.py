import streamlit as st
import random

# Sidebar instructions
st.sidebar.title("Instructions")
st.sidebar.write("""
1. Choose one of the options below by clicking on a button.
2. The computer will randomly pick an option.
3. Press PLAY. The results will show who won!
4. If both choose the same option, it’s a tie.

The game follows the well-known rules:

- Rock beats Scissors
- Paper beats Rock
- Scissors beats Paper
""")
st.sidebar.image("Rock-Paper-Scissors/rock_paper_scissors.png")

st.title("Rock-Paper-Scissors Game")

# Options for the game
options = ["rock", "paper", "scissors"]

# User input as button selection
you = st.radio("Choose your option:", options)
if st.button("Play"):
    computer = random.choice(options)

    # Display results
    st.write(f"**Computer's option**: {computer}")
    st.write(f"**Your option**: {you}")

    if computer == you:
        st.title("It's a tie!")
        st.image("Rock-Paper-Scissors/confused.png")
    elif (computer == "scissors" and you == "paper") or \
         (computer == "paper" and you == "rock") or \
         (computer == "rock" and you == "scissors"):
        st.title("Computer wins!")
        st.image("Rock-Paper-Scissors/images/nooo.png")
    else:
        st.title("You win!")
        st.image("Rock-Paper-Scissors/images/thumbs_up.png")
