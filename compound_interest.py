import matplotlib.pyplot as plt
import numpy as np


def interest(P: int, r: float, n: int, t: int) -> float:
    A = round( P * (1 + r/n)**(n*t), 2 )
    return A


# Get a numpy array using the interest function

years = input("How many years do you plan on investing for? ")
low_interest_str = input("What's the lowest interest rate you're willing to take? ")
high_interest_str = input("What's the *most reasonable* highest interest rate you're willing to take? ")

# Convert input strings to floats and round to two decimal places
low_interest = round(float(low_interest_str.rstrip('%')) / 100, 4)
high_interest = round(float(high_interest_str.rstrip('%')) / 100, 4)

# Prompt the user to input the number of samples they want to generate
num_samples = int(input("How many samples do you want to generate? "))

# Initiating the array
all_values = []


# Iterate over the interest rates
for j in np.linspace(low_interest, high_interest, num_samples):
    values_for_j = []  # Initialize a list to store the interest values for the current interest rate
    # Iterate over the years
    for i in np.linspace(0, int(years) + 1, int(years)):
        # Calculate the interest and append it to the list
        values_for_j.append(interest(500, j, 4, i))
    # Append the interest values for the current interest rate to the main list
    all_values.append(values_for_j)

# Convert the list of lists into a NumPy array
numpy_array = np.array(all_values)


# Plot the interest values using matplotlib

number_of_arrays = numpy_array.shape[0]  # Number of 1-dimensional arrays
number_of_years = numpy_array.shape[1]   # Number of years
interest_rates = np.linspace(low_interest, high_interest, num_samples) # Interest rates to be displayed as a legend

# Assuming years start from 1 and end at 25
x = range(1, number_of_years + 1)

# Plot each array separately
for i in range(number_of_arrays):
    y = numpy_array[i, :]
    plt.plot(x, y, label=f'Interest at {interest_rates[i]:3f}')  # Format interest rate to 3 decimal places

plt.xlabel('Year')
plt.ylabel('Future Value')
plt.title('Future Value over 25 Years for Different Interest Rates')
plt.legend() # Add a legend to distinguish each array

plt.show()