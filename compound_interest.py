import matplotlib.pyplot as plt, mpld3
import numpy as np


def interest(P: int, r: float, n: int, t: int) -> float:
    A = round( P * (1 + r/n)**(n*t), 2 )
    return A


# Initiating the array
all_values = []

# Iterate over the interest rates
for j in np.linspace(0.01, 0.10, 10):
    values_for_j = []  # Initialize a list to store the interest values for the current interest rate
    # Iterate over the years
    for i in np.linspace(0, 26, 25):
        # Calculate the interest and append it to the list
        values_for_j.append(interest(500, j, 4, i))
    # Append the interest values for the current interest rate to the main list
    all_values.append(values_for_j)

# Convert the list of lists into a NumPy array
numpy_array = np.array(all_values)


number_of_arrays = numpy_array.shape[0]  # Number of 1-dimensional arrays
number_of_years = numpy_array.shape[1]   # Number of years
interest_rates = np.linspace(0.01, 0.10, 10) # Interest rates to be displayed as a legend


# Assuming years start from 1 and end at 25
x = range(1, number_of_years + 1)


# Plot each array separately
for i in range(number_of_arrays):
    y = numpy_array[i, :]
    plt.plot(x, y, label=f'Interest at {interest_rates[i]:.2f}')  # Format interest rate to 2 decimal places

plt.xlabel('Year')
plt.ylabel('Future Value')
plt.title('Future Value over 25 Years for Different Interest Rates')
plt.legend() # Add a legend to distinguish each array

plt.show()