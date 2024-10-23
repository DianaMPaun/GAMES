
# Sudoku Game

A simple Sudoku game built with Python and Streamlit. This interactive app allows users to solve Sudoku puzzles using numbers or letters, with features to track completion time and verify the solution.

## Features

- **Play with Numbers or Letters**: Choose between traditional numbers or letters (A-I) to fill the Sudoku grid.
- **Time Tracking**: The game displays the time taken to complete the puzzle in seconds.
- **Check Solution**: After filling the grid, use the "Check Solution" button to verify your answer.
  - **Correct Solution**: Displays a congratulatory message— "Congratulations! You solved the Sudoku."
  - **Incorrect Solution**: Displays an error message— "There are some mistakes in your solution. Try again!"

## Getting Started

### Prerequisites

- **Python 3.x** installed on your machine
- **Streamlit** library installed

You can install Streamlit using the following command:

```bash
pip install streamlit
```

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/sudoku-game.git
   cd sudoku-game
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run sudoku_app.py
   ```

### How to Play

1. Open the app using the `streamlit run` command mentioned above.
2. Select whether you want to play with **numbers** or **letters**.
3. Fill in the grid following standard Sudoku rules.
4. Click on **Check Solution** when you are done.
5. If the solution is correct, you will see "Congratulations! You solved the Sudoku." Otherwise, you’ll be prompted to correct any errors.

## Screenshot

![image](https://github.com/user-attachments/assets/091705bf-60af-49e8-9790-6b4ab49ecc51)


## Technologies Used

- **Python** 
- **Streamlit**

## Contributing

If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.
