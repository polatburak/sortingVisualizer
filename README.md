# Sorting Algorithms Visualizer


![sortingVisualizer](https://github.com/polatburak/sortingVisualizer/assets/100538337/5bff9df9-5f0d-423f-ada2-2d920c0f6b70)

This project is a Sorting Algorithms Visualizer implemented in Python using the Pygame module. It allows you to interactively visualize and compare the performance of three different sorting algorithms: Bubble Sort, Iteration Sort, and Merge Sort. Sorting process can be visualized in both iterative and recursive forms using different algorithms.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Sorting Algorithms](#sorting-algorithms)
- [Time Complexity](#time-complexity)
- [References](#references)

## Features
- Interactive visualization of sorting algorithms.
- Choose from three different sorting algorithms.
- Toggle between iterative and recursive implementations.
- Random array size between 2-50 elements.
- Color-coded bars for better visualization.

## Installation

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/polatburak/sortingVisualizer.git
2. Navigate to the project directory.
   ```bash
   cd sortingVisualizer
4. Install the required dependencies using pip.
   ```bash
   pip install pygame

## Usage

1. Run the Python script
    ```bash
   python main.py
3. Use the following keys to interact with the visualizer:
-  Press 'N' to get a new list with random numbers.
-  Press 'R' to reset to the unsorted list.
-  Press 'SPACE' to start the sorting with chosing algorithm and style.
-  Press 'A' to select if algorithm should give the numbers in an ascending order.
-  Press 'D' to select if algorithm should give the numbers in a descending order.
-  Press 'I' to select Insertion Sort as the sorting algorithm.
-  Press 'B' to select Bubble Sort as the sorting algorithm.
-  Press 'M' to select Merge Sort as the sorting algorithm.
-  You can cancel the sorting process by pressing 'N' or 'R'

## Time Complexity

Here are the time complexities of the sorting algorithms:

Algorithm | Average Case | Best Case | Worst Case
| :---: | :---: | :---: | :---:
**Bubble Sort**  | *O(n^2)* | *O(n)* | *O(n^2)*
**Iteration Sort**  | *O(n^2)* | *O(n)* | *O(n^2)*
**Merge Sort** | *O(n log n)* | *O(n log n)* | *O(n log n)*

## References

- [YouTube](https://youtu.be/pFXYym4Wbkc?si=jbUI5e1VJF3BNznC")
- [GitHub](https://github.com/techwithtim/Sorting-Algorithm-Visualizer")
