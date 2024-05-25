from RK4 import run
from Lorenz import lorenz
from Ours import our_function
from people import people
import matplotlib.pyplot as plt


def get_last_subdivision(index):
    variable_range = max_values[index] - min_values[index]
    subdivision_size = variable_range / n
    normalized_value = (Y[index][-1] - min_values[index]) / subdivision_size
    last_subdivision = int(normalized_value)
    return last_subdivision

def generate_chaotic_sequence(solutions, bits_per_value=8):
    chaotic_seq_bits = ""
    for y_values in solutions:
        for value in y_values:
            decimal_part = abs(value - int(value))
            scaled_decimal = int(decimal_part * 2**bits_per_value)
            binary_value = format(scaled_decimal, f'0{bits_per_value}b')  # Convert to binary
            chaotic_seq_bits += binary_value
    return chaotic_seq_bits


y0 = [-1, 28, 1.6]
dt = 0.01
T = 65
Y = [[], [], []]


def get_word():
    global n, min_values, max_values
    Y[0], Y[1], Y[2], min_values, max_values = run(y0, dt, T, lorenz)
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot(Y[0], Y[1], Y[2], 'b')
    plt.show()

    # Selecting person
    n = len(people)
    person = people[get_last_subdivision(0)]

    # Selecting word
    n = len(person)
    word = person[get_last_subdivision(1)]

    # Selecting number
    n = 100
    num = get_last_subdivision(2)

    # Generate salt from chaotic sequence
    #salt_length = 32  # Adjust salt length as needed
    #salt = generate_chaotic_sequence(Y, bits_per_value=8)[:salt_length]  # Use Y[0] for salt generation
    #password = salt + word + str(num)  # Prepend salt to the password

    password = word + str(num)
    print(password)

    return password
