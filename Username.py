from RK4 import run
from Lorenz import lorenz
from Rikitake_Dynamo import rik_dyn
from Chen import chen
import matplotlib.pyplot as plt


def generate_key(username, initial_conditions, t, dt, function):
    y_values = [[], [], []]
    y_values[0], y_values[1], y_values[2], _, _ = run(initial_conditions, dt, t, function)
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot(y_values[0], y_values[1], y_values[2], 'b')
    plt.show()

    key = ""
    for y in y_values:
        # Convert decimal part of each y value to a binary representation
        key += format(int((abs(y[-1]) - int(abs(y[-1]))) * 256), '08b')
    return key[:len(username)]


def encrypt(username, initial_conditions, t_span, dt, function):
    key = generate_key(username, initial_conditions, t_span, dt, function)
    #print(key)
    encrypted = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(username, key))
    return encrypted


def decrypt(encrypted_username, initial_conditions, t_span, dt, function):
    return encrypt(encrypted_username, initial_conditions, t_span, dt, function)  # XOR is its own inverse

"""
# E ample usage with user input
username = input("Enter username: ")
x0 = float(input("Enter initial value for x: "))
y0 = float(input("Enter initial value for y: "))
z0 = float(input("Enter initial value for z: "))
T = 50
dt = 0.01

initial_conditions = [x0, y0, z0]

encrypted_username = encrypt(username, initial_conditions, T, dt, chen)
decrypted_username = decrypt(encrypted_username, initial_conditions, T, dt, chen)

print("Original username:", username)
print("Encrypted username:", encrypted_username)
print("Decrypted username:", decrypted_username)
"""