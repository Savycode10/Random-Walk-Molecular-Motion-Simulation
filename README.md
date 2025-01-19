# Random-Walk-Molecular-Motion-Simulation

## Random Walk Project_ Arewa Data Science Fellowship Projects

This repository contains a series of Python-based implementations for simulating and analyzing random walks. The project explores various modifications and enhancements to the classic random walk algorithm, aimed at simulating and visualizing random motions in a two-dimensional space.

Key Features:
Basic Random Walk Simulation: Implements a simple random walk where an entity moves in discrete steps along the x and y axes. The movement is randomly determined using a set of predefined step sizes and directions.

Visualization: Uses ```matplotlib``` to visualize the path of the random walk in 2D. The walk's progress is plotted, allowing for a clear understanding of the motion dynamics.

Refactored Code for Maintainability: The code has been refactored to improve readability and maintainability by breaking down complex methods. A new method ```get_step()``` has been introduced to separate the logic of step generation, reducing redundancy and improving clarity.

Modifiable Parameters: Parameters for the random walk, such as step distances and directions, are adjustable. This allows for the simulation of different random walk patterns and behaviors by altering the step choices and randomization.

Advanced Walks with Multiple Steps: Modifications to the walk generation process include using longer lists for distance and direction choices, allowing for more diverse and complex paths.


Interactive Plots: The visualization of the random walk can be customized with different line widths, and the number of steps can be adjusted to see how larger numbers of points affect the walk’s behavior.

Updates:
Increased Walk Steps: The initial walk step count was updated from 50,000 to 5,000 points to balance between visual clarity and performance.

Path Refinement: Replaced ```plt.scatter()``` with ```plt.plot()``` for continuous path plotting, providing a smoother representation of the walk compared to discrete point markers.

Code Optimization: Refactoring of the core method ```fill_walk()``` by moving the logic for determining steps into a separate ```get_step()``` method. This change improves code readability, making it easier to extend and modify in the future.

Goal:
The purpose of this project is to experiment with different conditions and parameters in random walk simulations, offering valuable insights into the behavior of random processes. The implementation serves as a foundation for more complex simulations, potentially useful for various scientific fields, including physics, biology, and financial modeling.
