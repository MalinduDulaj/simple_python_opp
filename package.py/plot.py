import matplotlib.pyplot as plt

def main():
    # Sample data
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]

    # Create a new figure
    plt.figure()

    # Plot the data
    plt.plot(x, y, marker='o')

    # Add labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Simple Line Plot')

    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
