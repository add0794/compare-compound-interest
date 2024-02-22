import json
import matplotlib.pyplot as plt
import numpy as np
import re
import time


def interest(P: int, r: float, n: int, t: int) -> float:
    A = round( P * (1 + r/n)**(n*t), 2 )
    return A

# Get a numpy array using the interest function

with open("currency_symbols.json", "r") as json_file:
    currency_symbols = json.load(json_file)

def get_input(prompt, currency_symbol=None, input_type=None):
    while True:
        try:
            user_input = input(prompt)

            if currency_symbol is not None:
                if user_input not in currency_symbols.values():
                    raise ValueError("You entered an incorrect value. Please enter a correct value.")
                else:
                    result = user_input

            elif input_type == int and isinstance(user_input, str): 
                user_input = re.sub(r'\D', '', user_input)
                result = input_type(user_input)

            elif input_type == float and isinstance(user_input, str):
                user_input = re.sub(r'[^0-9.]', '', user_input)
                result = round(input_type(user_input) / 100, 3)

            else:
                result = user_input
            
            return result

        except Exception:
            print("\nYou entered an incorrect value. Please enter a correct value.")


# Get values for each variable in the interest function
unit_of_currency = get_input("What unit of currency do you use? ", "$")
principal = get_input("How much money do you plan in investing? ", None, int)
times_per_year = get_input("How often will the interest be compounded per year? ", None, int)
years = get_input("How many years do you plan on investing for? ", None, int)
low_interest = get_input("What's the lowest interest rate you're willing to take? ", None, float)
high_interest = get_input("What's the *most reasonable* highest interest rate you're willing to take? ", None, float)
num_samples = get_input("How many samples do you want to generate? ", None, int)

print([unit_of_currency, principal, times_per_year, years, low_interest, high_interest, num_samples])


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

# Set the limits of the plot
plt.xlim(1, years)  # Set the x-axis limit to start at 0 and automatically adjust the maximum value
plt.ylim(0, None)  # Set the y-axis limit to start at 0 and automatically adjust the maximum value

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Future Value')
plt.title('Future Value over 25 Years for Different Interest Rates')
plt.legend() # Add a legend to distinguish each array

print(numpy_array)
plt.show()