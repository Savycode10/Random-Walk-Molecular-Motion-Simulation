import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # Create a random walk with 5000 points
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the path using plt.plot()
    plt.figure(figsize=(10, 6))  # Optional: Adjust the figure size for better visibility
    plt.plot(rw.x_values, rw.y_values, linewidth=1)

    # Highlight the start and end points
    plt.scatter(0, 0, c='green', edgecolors='none', s=100, label='Start')  # Start point
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100, label='End')  # End point

    # Add title and remove axes for better visualization
    plt.title("Random Walk - Molecular Motion Simulation", fontsize=14)
    plt.axis('off')  # Remove the axes for a cleaner look

    # Display the plot
    plt.legend()  # Optional: Display legend for start and end points
    plt.show()

    # Prompt user to run another simulation
    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':
        break

