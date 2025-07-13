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

### NOTES
- The time to solve can vary from a few seconds to a few minutes or not finish in a reasonable amount of time, so please wait if things take longer than expected.
- If the program crashes due to running too long (more than an hour, for example), please close it and choose another algorithm. This means that the algorithm cannot be used on this map, not just whether it can be solved or not.

## 3. DIRECTORY ORGANIZATION 

This root folder is the source code folder of this project. We separate our implementation into two subfolders: `core` and `gui`. 
- `core` contains implementation of search algorithms and solvers.
- `gui` contains GUI implementation, divided into multiple submodules to enhance organization. The main module in this subfolder is `main`, used to start the GUI application.

## 4. MAP FORMAT AND MAP DESCRIPTION
Maps are saved in `gui/map.txt`. The map description and steps in solution follow the same format as board description and solution description in [this article](https://www.michaelfogleman.com/rush/). Still, I want to repeat the format of each map as follow:
- The map format is a 36-character string represent the state of the unsolved map. 
- Each string is a 6x6 2D array in row-major order.
- Meaning of the characters in the format:
   + `o` or `.` (not used in our designed map): empty cell.
   + `A`: primary piece/vehicle (red car in our GUI).
   + `B - Z`: other pieces (blue car in our GUI).

To construct the map from these string, rewrite them as a 6x6 2D array, then merge cells with identical characters into pieces. The piece with character `A` is the primary piece/vehicle, otherwise it is another piece/vehicle (obstacles of primary piece/vehicle). For example, given the string `oGBBBooGHoooAAHoIoCCCoIoFDDEEEFooooo`, one can write it as: 

<center>

|  |  |  |  |  |  |
|---|---|---|---|---|---|
| o | G | B | B | B | o |
| o | G | H | o | o | o |
| A | A | H | o | I | o |
| C | C | C | o | I | o |
| F | D | D | E | E | E |
| F | o | o | o | o | o |

</center>

Using that table, we now have this [map](map_demo.png). 

In `gui/map.txt`, each line has a string that is a map description and a number that is the size of that map's cluster (cluster in this case is all reachable states started from this inital state). In case the map in unsolvable, its cluster size is assigned to -1. 

There are 13 lines in the map file, and the reasons we choosed these maps, start from the first to the last line, are:
- Map #1 - #3: they have the biggest cluster size.
- Map #4 - #6: they are 3 hardest maps in terms of number of moves (multiple steps is allowed, not the same as our definition of a move in this project).
- Map #7 - #8: they are unsolvable.
- Map #9: all algorithms run on this map have large number of expanded nodes, and a particular case where **Backtracking** is very fast.
- Map #10: a map where **A start** is as twice as slower than **Weighted A start** and **Weighted A start** find a suboptimal solution.
- Map #11 - #13: maps where **UCS** perform as good as **BFS**.

## 5. HOW TO RUN THE PROGRAM 

1. Open a terminal or command prompt.

2. Navigate to the root folder of the project:
   ```bash
    cd Rush-Hour

3. Run the program using the following command:
   ```bash
    python -m gui.main

## 6. INSTALLATION

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

## 7. BACKLOG FILE FORMAT

When the program starts, it will automatically generate a **backlog file**. It will record all accessed maps and the execution results of the algorithms, including performance metrics and solution data.\
This feature is used for debugging, storing solution history, and additional analysis beyond the built-in animations of the program. 

### GENERAL INFORMATION

At the beginning of the file, it will contain general information including:
- `Number of read maps`: Total number of maps in the program  
- ``List of read maps``: includes strings representing each map

### DETAIL INFORMATION

In each program run, after the user finishes selecting the map and algorithm and starts the search process, the file will display the following information:
- ``Map index``: the order number of the selected map in the list of maps (e.g., #0,... #12)  
- ``Map description``: the string representing the selected map  
- ``Algorithm``: the selected algorithm

After the search process is completed, the file will display additional information depending on the result:
- **If the algorithm finds a solution**:
  - ``Result``: Success  
  - ``Number of steps``: total number of moves to reach the solution  
  - ``Time required(s)``: time spent on the search  
  - ``List of steps``: list of moves, written in the format [Vehicle symbol][+ (move down/right) or - (move up/left)][number of steps (default is 1)], e.g., `A+1`: vehicle A moves forward 1 step

- **If the algorithm does not find a solution**:
  - ``Result``: Failure  
  - And there will be no information such as number of steps, search time, or list of steps

There may be multiple runs in one program session; each run will be recorded in the file and clearly separated.

## 8. LINK DEMO GUI VIDEO

Link: [Demo GUI Video](https://www.youtube.com/watch?v=ZA5tRyl9Jf4)