# Rush-Hour

## 1. PROJECT INTRODUCTION

This project implements a program that automatically solves the **Rush Hour puzzle** using various **search algorithms**.  
It is the first project for the **Introduction to Artificial Intelligence** course of class **23CLC05**, with contributions from the following members:

- Trần Công Minh (23127007)  
- Nguyễn Hoàng Minh Tâm (23127017)  
- Lê Hồng Ngọc (23127236)  

## 2. FEATURES AND GUI GUIDE

### OVERVIEW 
This application simulates various search algorithms on Rush Hour puzzles.  
Navigate through different maps and algorithms to compare their performance.

### BASIC CONTROLS 

- Press `Enter` key or click on the black triangle icons (you can also scroll the mouse wheel) – Switch to the next map  
- Press `Space` bar key or click on the **Solve** button – Start the algorithm  
- Press `=` key or click on the black triangle icons (you can also scroll the mouse wheel) – Switch between algorithms  
- Press `Esc` key or click on the **Finish** button – Return to map selection  

### GETTING STARTED 

1. Launch the application  
2. Browse available maps using the `Enter` key or the black triangle icons (or scroll the mouse wheel)
3. When you find a map you want to test:  
   - Use the `=` key or the black triangle icons (or scroll the mouse wheel) to cycle through available algorithms  
   - Press `Space` or click the **Solve** button to start the search  

### ALGORITHM EXECUTION 

- After pressing `Space` or clicking the **Solve** button, the program starts finding a solution  
- Wait for the algorithm to complete (execution time depends on the map complexity, the chosen algorithm, and the specifications of the machine running the program)  
- The results will show:  
  * Whether a solution exists  
  * Number of steps required (if solved)  
  * Time elapsed during the search  

### SOLUTION REVIEW 

**When the algorithm completes:**

- Press `S` key or click on the **Start** button – Start solution animation  
- Press `Esc` key or click on the **Finish** button – Return to map/algorithm selection  

**If no solution is found:**

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

## 3. HOW TO RUN THE PROGRAM 

1. Open a terminal or command prompt.

2. Navigate to the root folder `Rush-Hour` of the project:
   ```bash
    cd Rush-Hour

3. Run the program using the following command:
   ```bash
    python -m gui.gui

## 4. INSTALLATION

Before running the program, make sure you have Python installed.\
We use **Python version 3.12.7**, so for best compatibility, it is recommended that you use the same version.
1. Open a terminal or command prompt.

2. Navigate to the root folder `Rush-Hour` of the project:
   ```bash
    cd Rush-Hour

3. Install the required packages using `pip`:
   ```bash
    pip install -r requirements.txt
   ```
   This will install the following libraries:
   - `numpy==2.3.1`
   - `pygame==2.6.1`

4. After installation, you can run the program as described above.

## 5. BACKLOG FILE FORMAT

When the program starts, it will automatically generate a **backlog file**. It will record all accessed maps and the execution results of the algorithms, including performance metrics and solution data.\
This feature is used for debugging, storing solution history, and additional analysis beyond the built-in animations of the program.

### GENERAL INFORMATION

At the beginning of the file, it will contain general information including:
- **Number of read maps**: Total number of maps in the program  
- **List of read maps**: includes strings representing each map

### DETAIL INFORMATION

In each program run, after the user finishes selecting the map and algorithm and starts the search process, the file will display the following information:
- **Map index**: the order number of the selected map in the list of maps (e.g., #0,... #12)  
- **Map description**: the string representing the selected map  
- **Algorithm**: the selected algorithm

After the search process is completed, the file will display additional information depending on the result:
- **If the algorithm finds a solution**:
  - **Result**: Success  
  - **Number of steps**: total number of moves to reach the solution  
  - **Time required(s)**: time spent on the search  
  - **List of steps**: list of moves, written in the format [Vehicle symbol][+ (forward) or - (backward)][number of steps (default is 1)], e.g., `A+1`: vehicle A moves forward 1 step
  
- **If the algorithm does not find a solution**:
  - **Result**: Failure  
  - And there will be no information such as number of steps, search time, or list of steps

There may be multiple runs in one program session; each run will be recorded in the file and clearly separated.

## 6. LINK DEMO GUI VIDEO

Link: [Demo GUI Video](https://www.youtube.com/watch?v=ZA5tRyl9Jf4)