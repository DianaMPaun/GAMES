import streamlit as st
import numpy as np
import random
import time
import string

# --- Functions ---

# Function to check if the board is valid
def is_valid(board, row, col, num, is_letter=False):
    if is_letter:
        valid_nums = list(string.ascii_uppercase[:9])
    else:
        valid_nums = list(range(1, 10))
    
    for x in range(9):
        if board[row][x] == num:
            return False
    for x in range(9):
        if board[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

# Function to solve the Sudoku board
def solve_sudoku(board, is_letter=False):
    if is_letter:
        valid_nums = list(string.ascii_uppercase[:9])
    else:
        valid_nums = list(range(1, 10))
    
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in valid_nums:
                    if is_valid(board, row, col, num, is_letter):
                        board[row][col] = num
                        if solve_sudoku(board, is_letter):
                            return True
                        board[row][col] = 0
                return False
    return True

# Function to generate a Sudoku puzzle
def generate_sudoku(is_letter=False):
    board = [[0 for _ in range(9)] for _ in range(9)]
    if is_letter:
        valid_nums = list(string.ascii_uppercase[:9])
    else:
        valid_nums = list(range(1, 10))

    for i in range(9):
        num = random.choice(valid_nums)
        row, col = random.randint(0, 8), random.randint(0, 8)
        while not is_valid(board, row, col, num, is_letter) or board[row][col] != 0:
            num = random.choice(valid_nums)
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = num
    solve_sudoku(board, is_letter)
    return board

# Function to remove elements to create a puzzle of a given difficulty
def remove_elements(board, difficulty='easy'):
    num_holes = {'easy': 30, 'medium': 40, 'hard': 50}
    holes = num_holes.get(difficulty, 30)
    while holes > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0
        holes -= 1
    return board

# Function to check if the Sudoku solution is valid and complete
def is_valid_solution(board, is_letter=False):
    def is_valid_block(block):
        block = [num for num in block if num != 0]
        return len(block) == len(set(block))

    for row in board:
        if not is_valid_block(row) or len(row) != 9:
            return False

    for col in zip(*board):
        if not is_valid_block(col) or len(col) != 9:
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_block(block):
                return False

    return all(all(cell != 0 for cell in row) for row in board)

# Function to store and manage the Sudoku puzzle in the session state
def get_puzzle(difficulty, is_letter=False):
    if 'puzzle' not in st.session_state:
        st.session_state['puzzle'] = remove_elements(generate_sudoku(is_letter), difficulty)
    return st.session_state['puzzle']

def get_user_solution(is_letter=False):
    if 'user_solution' not in st.session_state:
        st.session_state['user_solution'] = [[0] * 9 for _ in range(9)]
    return st.session_state['user_solution']

# Function to display emoji in the sidebar based on game outcome
def display_emoji(outcome):
    if outcome == "success":
        st.sidebar.markdown("<h1 style='font-size: 120px;'>😊</h1>", unsafe_allow_html=True)
    elif outcome == "error":
        st.sidebar.markdown("<h1 style='font-size: 120px;'>😢</h1>", unsafe_allow_html=True)



# Function to check the solution
def check_solution(user_solution, puzzle, is_letter):
    solution = [[puzzle[i][j] if puzzle[i][j] != 0 else user_solution[i][j] for j in range(9)] for i in range(9)]
    if is_valid_solution(solution, is_letter):
        st.success("Congratulations! You solved the Sudoku.")
        display_emoji("success")
    else:
        st.error("There are some mistakes in your solution. Try again!")
        display_emoji("error")

# --- Main App ---

def main():
    st.markdown("<h1 style='text-align: center;'>Sudoku Game</h1>", unsafe_allow_html=True)
    
    st.sidebar.markdown("<h2>Choose Difficulty:</h2>", unsafe_allow_html=True)
    difficulty = st.sidebar.radio("", ('easy', 'medium', 'hard'))
    
    st.sidebar.markdown("<h2>Choose Type:</h2>", unsafe_allow_html=True)
    sudoku_type = st.sidebar.radio("", ('number', 'letter'))

    is_letter = sudoku_type == 'letter'

    # "Let's play!" with START button
    col1, col2 = st.columns([3, 1])
    col1.markdown("<h3>Let's play!</h3>", unsafe_allow_html=True)
    
    # Handling the start button click
    if col2.button("START") and not st.session_state.get('game_started', False):
        st.session_state['start_time'] = time.time()
        st.session_state['game_started'] = True
        st.session_state['puzzle'] = remove_elements(generate_sudoku(is_letter), difficulty)  # Reset the puzzle on start
        st.session_state['user_solution'] = [[0] * 9 for _ in range(9)]  # Reset the user's solution
        st.experimental_rerun()

    if 'game_started' not in st.session_state:
        st.session_state['game_started'] = False

    # Timer display
    if st.session_state['game_started']:
        elapsed_time = int(time.time() - st.session_state['start_time'])
        st.write(f"Time elapsed: {elapsed_time} seconds")

    puzzle = get_puzzle(difficulty, is_letter)
    user_solution = get_user_solution(is_letter)

    # Instructions
    st.sidebar.markdown("""
    ### Instructions:
    - Choose a difficulty level
    - Choose a puzzle type (number or letter)
    - Click on 'START' to generate a new puzzle
    - Fill in the grid
    - Click 'Check Solution' to validate your solution
    - Click 'New Puzzle' to generate a new puzzle
    """)

    # Create a container for the Sudoku grid
    grid_container = st.container()

    # Display the Sudoku grid
    for i in range(9):
        cols = grid_container.columns(9)
        for j in range(9):
            if puzzle[i][j] == 0:
                if is_letter:
                    user_solution[i][j] = cols[j].text_input('', key=f'{i}-{j}', value=user_solution[i][j])
                else:
                    user_solution[i][j] = cols[j].number_input('', min_value=0, max_value=9, key=f'{i}-{j}', value=user_solution[i][j])
            else:
                if is_letter:
                    cols[j].text_input('', value=puzzle[i][j], key=f'{i}-{j}', disabled=True)
                else:
                    cols[j].number_input('', min_value=0, max_value=9, value=puzzle[i][j], key=f'{i}-{j}', disabled=True)

    # Add buttons for actions
    if st.button("Check Solution"):
        check_solution(user_solution, puzzle, is_letter)

    if st.button("New Puzzle"):
        st.session_state['puzzle'] = remove_elements(generate_sudoku(is_letter), difficulty)
        st.session_state['user_solution'] = [[0] * 9 for _ in range(9)]
        st.experimental_rerun()

if __name__ == "__main__":
    main()


