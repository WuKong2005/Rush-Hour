# Rush-Hour

## Project Introduction

This project implements a program that automatically solves the **Rush Hour puzzle** using various **search algorithms**.  
It is the first project for the **Introduction to Artificial Intelligence** course of class **23CLC05**, with contributions from the following members:

- Trần Công Minh (23127007)  
- Nguyễn Hoàng Minh Tâm (23127017)  
- Lê Hồng Ngọc (23127236)  

## Features and GUI User Guide

### RUSH HOUR SEARCH ALGORITHM SIMULATOR - USER GUIDE

### OVERVIEW 
This application simulates various search algorithms on Rush Hour puzzles.  
Navigate through different maps and algorithms to compare their performance.

### BASIC CONTROLS 

- Press `Enter` key or click on the black arrow icons (you can also scroll the mouse wheel) – Switch to the next map  
- Press `Space` bar key or click on the **Solve** button – Start the algorithm  
- Press `=` key or click on the black arrow icons (you can also scroll the mouse wheel) – Switch between algorithms  
- Press `Esc` key or click on the **Finish** button – Return to map selection  

### GETTING STARTED 

1. Launch the application  
2. Browse available maps using the `Enter` key  
3. When you find a map you want to test:  
   - Use the `=` key or the black arrow icons (or scroll the mouse wheel) to cycle through available algorithms  
   - Press `Space` or click the **Solve** button to start the search  

### ALGORITHM EXECUTION 

- After pressing `Space` or clicking the **Solve** button, the program starts finding a solution  
- Wait for the algorithm to complete (execution time depends on puzzle complexity)  
- The results will show:  
  * Whether a solution exists  
  * Number of steps required (if solved)  
  * Time elapsed during the search  

### SOLUTION REVIEW 

When the algorithm completes:

- Press `S` key or click on the **Start** button – Start solution animation  
- Press `Esc` key or click on the **Finish** button – Return to map/algorithm selection  

If no solution is found:

- Press `Esc` key or click on the **Finish** button – Return to map/algorithm selection  

### ANIMATION CONTROLS 

- **Default**: Automatic playback of solution steps  
- Press `P` key or click on the **Pause** button – Pause animation and enter manual control mode  

**Manual Control Mode:**

- Press `→` (Right Arrow) or click on the black right arrow icons (or scroll the mouse wheel) – Next step  
- Press `←` (Left Arrow) or click on the black left arrow icons (or scroll the mouse wheel) – Previous step  
- Press `R` key or click on the **Reset** button – Restart to the original puzzle state  
- Press `Esc` key or click on the **Finish** button – Exit animation  

### TIPS 

- Compare different algorithms on the same map  
- Observe performance differences between BFS, DFS, A*, etc.  
- Use manual animation control to understand solution steps more clearly  

## How to Run the Program

1. Open a terminal or command prompt.

2. Navigate to the root folder `Rush-Hour` of the project:
   ```bash
    cd Rush-Hour

3. Run the program using the following command:
   ```bash
    python -m gui.gui

## Link video demo GUI

Link: []()