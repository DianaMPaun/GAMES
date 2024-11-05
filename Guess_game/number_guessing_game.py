import random
import string
import streamlit as st

# Initialize high scores
high_score = {"guess number": 0, "guess letter": 0}

# Function to select difficulty
def get_difficulty():
    difficulty = st.sidebar.radio("Choose a difficulty level:", ("Easy", "Medium", "Hard"))
    st.sidebar.write("---")
    if difficulty == "Easy":
        return 50, 5  
    elif difficulty == "Medium":
        return 10, 10  
    elif difficulty == "Hard":
        return 5, 20  
    else:
        return 10, 10  

def initialize_number_game():
    # Initialize or reset the number game
    st.session_state.number = random.randint(0, 100)
    st.session_state.guesses = 0
    st.session_state.score = st.session_state.base_points

def play_number_guess():
    global high_score
    max_attempts, base_points = get_difficulty()
    
    # Initialize session state variables if they don't exist
    if "number" not in st.session_state:
        st.session_state.base_points = base_points
        initialize_number_game()

    st.write("**Guess the number! Enter a number between 0 and 100.**")
    st.image("https://github.com/DianaMPaun/GAMES/blob/main/Guess_game/emoji_numbers.png")

    guess = st.number_input("Enter your guess:", min_value=0, max_value=100, key="number_guess")
    
    if st.button("Submit Guess", key="submit_number"):
        st.session_state.guesses += 1
        if guess == st.session_state.number:
            st.success(f"Correct! You guessed the number in {st.session_state.guesses} attempt(s)!")
            st.session_state.score -= st.session_state.guesses  
            if st.session_state.score > high_score["guess number"]:
                st.balloons()
                st.success(f"New high score of {st.session_state.score} points!")
                high_score["guess number"] = st.session_state.score
            else:
                st.write(f"Your score: {st.session_state.score}")
            initialize_number_game() 
        elif guess > st.session_state.number:
            st.warning(f"{guess} is too high!")
        else:
            st.warning(f"{guess} is too low!")

        if st.session_state.guesses >= max_attempts:
            st.error(f"Game over! You've used all {max_attempts} attempts. The number was {st.session_state.number}.")
            initialize_number_game() 

def initialize_letter_game():
    # Initialize or reset the letter game
    st.session_state.letter = random.choice(string.ascii_lowercase)
    st.session_state.guesses = 0
    st.session_state.score = st.session_state.base_points

def play_letter_guess():
    global high_score
    max_attempts, base_points = get_difficulty()
    
    # Initialize session state variables if they don't exist
    if "letter" not in st.session_state:
        st.session_state.base_points = base_points
        initialize_letter_game()

    st.write("**Guess the letter! Enter a letter between 'a' and 'z'.**")
    st.image("https://github.com/DianaMPaun/GAMES/blob/main/Guess_game/abc.png")
    
    guess = st.text_input("Enter your guess:", max_chars=1, key="letter_guess").lower()
    
    if st.button("Submit Guess", key="submit_letter"):
        st.session_state.guesses += 1
        if guess == st.session_state.letter:
            st.success(f"Correct! You guessed the letter in {st.session_state.guesses} attempt(s)!")
            st.session_state.score -= st.session_state.guesses
            if st.session_state.score > high_score["guess letter"]:
                st.balloons()
                st.success(f"New high score of {st.session_state.score} points!")
                high_score["guess letter"] = st.session_state.score
            else:
                st.write(f"Your score: {st.session_state.score}")
            initialize_letter_game()  
        elif guess > st.session_state.letter:
            st.warning(f"{guess} comes later in the alphabet!")
        else:
            st.warning(f"{guess} comes earlier in the alphabet!")

        if st.session_state.guesses >= max_attempts:
            st.error(f"Game over! You've used all {max_attempts} attempts. The letter was '{st.session_state.letter}'.")
            initialize_letter_game()  

# Streamlit UI
st.title("Guess the Number or Letter Game")
st.write("---")
st.sidebar.title("Choose a game mode:")
st.sidebar.write("---")

game_choice = st.sidebar.radio("", ("Guess a Number", "Guess a Letter"))
st.sidebar.write("---")


if game_choice == "Guess a Number":
    play_number_guess()
else:
    play_letter_guess()

# Instructions
st.sidebar.markdown("""
    ### Instructions:
    - Choose a **difficulty level** from the sidebar (Easy, Medium, Hard) to set the maximum number of attempts and base points.
    - Choose a **game type**:
      - **Guess a Number**: Try to guess a randomly selected number between 0 and 100.
      - **Guess a Letter**: Try to guess a randomly selected letter between 'a' and 'z'.
    - Enter your guess in the provided input box:
      - For numbers, enter a whole number (0-100).
      - For letters, enter a lowercase letter (a-z).
    - Click **Submit Guess** each time to see feedback:
      - "Too high" or "Too low" for numbers.
      - "Comes earlier" or "Comes later" for letters.
    - The game ends when:
      - You guess the correct answer, or
      - You use all your attempts.
    - Aim for a **high score** by guessing correctly in the fewest attempts possible!
""")

st.write("## High Scores:")
st.write(f"**Number Guess High Score:** {high_score['guess number']} points")
st.write(f"**Letter Guess High Score:** {high_score['guess letter']} points")
