import matplotlib.pyplot as plt
import numpy as np
import time


def interest(P: int, r: float, n: int, t: int) -> float:
    A = round( P * (1 + r/n)**(n*t), 2 )
    return A


# Get a numpy array using the interest function

principal = int(input("How much money do you plan in investing? ")) # The principal can only be an integer
times_per_year = int(input("How often will the interest be compounded per year? "))
years = int(input("How many years do you plan on investing for? "))
low_interest_str = input("What's the lowest interest rate you're willing to take? ")
high_interest_str = input("What's the *most reasonable* highest interest rate you're willing to take? ")

# Convert input strings to floats and round to two decimal places
low_interest = round(float(low_interest_str.rstrip('%')) / 100, 2)
high_interest = round(float(high_interest_str.rstrip('%')) / 100, 2)

# Prompt the user to input the number of samples they want to generate
num_samples = int(input("How many samples do you want to generate? "))


# Measure start time
start_time = time.perf_counter()


# Initiating the array
all_values = []


# Iterate over the interest rates
for j in np.linspace(low_interest, high_interest, num_samples):
    values_for_j = []  # Initialize a list to store the interest values for the current interest rate
    # Iterate over the years
    for i in np.linspace(0, years + 1, years):
        # Calculate the interest and append it to the list
        values_for_j.append(interest(principal, j, times_per_year, i))
    # Append the interest values for the current interest rate to the main list
    all_values.append(values_for_j)

# Convert the list of lists into a NumPy array
numpy_array = np.array(all_values)


# Measure time it took to complete the program
passed_time = time.perf_counter() - start_time
print(f"It took {passed_time} seconds")


# Plot the interest values using matplotlib

number_of_arrays = numpy_array.shape[0]  # Number of 1-dimensional arrays
number_of_years = numpy_array.shape[1]   # Number of years
interest_rates = np.linspace(low_interest, high_interest, num_samples) # Interest rates to be displayed as a legend

# Assuming years start from 1 and end at 25
x = range(1, number_of_years + 1)

# Plot each array separately
for i in range(number_of_arrays):
    y = numpy_array[i, :]
    plt.plot(x, y, label=f'Interest at {interest_rates[i]:2f}')  # Format interest rate to 3 decimal places

plt.xlabel('Year')
plt.ylabel('Future Value')
plt.title('Future Value over 25 Years for Different Interest Rates')
plt.legend() # Add a legend to distinguish each array

plt.show()