from matplotlib import pyplot as plt
from RK4 import run
from chooseWord import gen_password
from Lorenz import lorenz
from Ours import our_function


def prepare_password(password, block_size=32):
    password_bytes = password.encode()  # Convert password to bytes
    password_bits = ''.join(format(byte, '08b') for byte in password_bytes)  # Convert to bits
    padding_length = block_size - (len(password_bits) % block_size)
    password_bits += '0' * padding_length  # Pad with zeros
    blocks = []
    for i in range(0, len(password_bits), block_size):
        blocks.append(password_bits[i:i+block_size])

    return blocks


def generate_chaotic_sequence(solutions, bits_per_value=16):
    chaotic_seq_bits = ""  # Initialize an empty binary string

    for solution in solutions:
        decimal_part = abs(solution[-1] - int(solution[-1]))  # Get absolute decimal part
        binary_value = format(int(decimal_part * 2 ** bits_per_value),
                              f'0{bits_per_value}b')  # Convert to fixed-length binary
        chaotic_seq_bits += binary_value

    return chaotic_seq_bits


def normalize_abc(password):
    z0 = [-1, 28, 4.65]
    dr = 0.01
    R = 50
    Z = [[], [], []]
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    n = len(abc)
    normalized_last_values = []

    Z[0], Z[1], Z[2], min_values, max_values = run(z0, dr, R, lorenz)
    for j, z_array in enumerate(Z):
        variable_range = max_values[j] - min_values[j]
        subdivision_size = variable_range / n
        normalized_value = (z_array[-1] - min_values[j]) / subdivision_size
        last_subdivision = int(normalized_value)
        normalized_last_values.append(last_subdivision)

    subdivision_string = ""
    for i, letter in enumerate(password):
        index = i % 3
        subdivision = normalized_last_values[index]
        subdivision_string += str(subdivision)

    return subdivision_string


def permute_block(block, block_size):
    z0 = [-1, 28, 3.4]
    dr = 0.01
    R = 65
    Z = [[], [], []]

    _, Z[1], _, _, _ = run(z0, dr, R, lorenz)
    sequence = list(set(int(i) for i in Z[1]))

    permutation_map = list(range(block_size))  # Initialize with identity permutation
    for i in range(block_size):
        chaotic_index = sequence[i] % block_size
        permutation_map[i], permutation_map[chaotic_index] = permutation_map[chaotic_index], permutation_map[i]  # Swap

    permuted_block = ""
    for i in range(block_size):
        original_pos = permutation_map.index(i)
        permuted_block += block[original_pos]  # Extract bit from original position

    return permuted_block



y0 = [-1, 28, 6]
dt = 0.01
T = 50
Y = [[], [], []]
block_size = 32

def encrypt():
    Y[0], Y[1], Y[2], _, _ = run(y0, dt, T, lorenz)
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot(Y[0], Y[1], Y[2], 'b')
    plt.show()

    h = 0
    password = gen_password()
    password = normalize_abc(password)
    blocks = prepare_password(password, block_size=block_size)
    chaotic_seq_bits = generate_chaotic_sequence(Y, bits_per_value=16)
    for block in blocks:
        #Permutation of each block
        block = permute_block(block, block_size)

        # Preparing chaotic sequence
        if len(chaotic_seq_bits) >= block_size:
            chaotic_chunk = chaotic_seq_bits[:block_size]
            chaotic_seq_bits = chaotic_seq_bits[block_size:]
        else:
            chaotic_chunk = chaotic_seq_bits.ljust(block_size, '0')  # Pad with zeros
            chaotic_seq_bits = ""
        chaotic_value = int(chaotic_chunk, 2)

        byte_values = [int(block[i:i + 8], 2) for i in range(0, len(block), 8)] #Convert from string to bytes
        block_bytes = bytes(byte_values)
        block_int = int.from_bytes(block_bytes, byteorder='big')


        #Encryption Algorithm
        # Bitwise XOR
        xored_value = block_int ^ chaotic_value

        # Rotate (chaotic amount example)
        rotation_amount = chaotic_value % block_size
        rotated_value = (xored_value >> rotation_amount) | (xored_value << (block_size - rotation_amount))

        # Modular Addition
        h = (h + rotated_value) % 2 ** block_size

    print(h)

encrypt()

