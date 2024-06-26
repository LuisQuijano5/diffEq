from matplotlib import pyplot as plt
from RK4 import run
from Adam_Bashforth import adams_bashforth_4
from chooseWord import get_word
from Lorenz import lorenz
from Rikitake_Dynamo import rik_dyn


def prepare_password(password, block_size=32):
    password_bytes = password.encode()  # Convert password to bytes
    password_bits = ''.join(format(byte, '08b') for byte in password_bytes)  # Convert to bits
    padding_length = block_size - (len(password_bits) % block_size)
    if (padding_length > 0):
        password_bits += '0' * padding_length  # Pad with zeros ONLY if necessary

    return password_bits


def generate_chaotic_sequence(bits_per_value=16):
    y0 = [-1, 28, 6]
    dt = 0.01
    T = 50
    t_span = (0, 25)
    Y = [[], [], []]

    # Y[0], Y[1], Y[2], _, _ = run(y0, dt, T, lorenz)
    Y[0], Y[1], Y[2] = adams_bashforth_4(lorenz, y0, t_span, dt)
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot(Y[0], Y[1], Y[2], 'b')
    plt.show()

    chaotic_seq_bits = ""  # Initialize an empty binary string

    for solution in Y:
        decimal_part = abs(solution[-1] - int(solution[-1]))  # Get absolute decimal part
        binary_value = format(int(decimal_part * 2 ** bits_per_value),
                              f'0{bits_per_value}b')  # Convert to fixed-length binary
        chaotic_seq_bits += binary_value


    #print(chaotic_seq_bits)
    return chaotic_seq_bits


def normalize_abc(password):
    z0 = [-1, 28, 4.65]
    dr = 0.01
    R = 50
    Z = [[], [], []]
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
    n = len(abc)

    Z[0], Z[1], Z[2], min_values, max_values = run(z0, dr, R, lorenz)

    normalized_ranges = []
    for j in range(3):
        variable_range = max_values[j] - min_values[j]
        subdivision_size = variable_range / n
        subdivisions = [min_values[j] + k * subdivision_size for k in range(n)]
        normalized_ranges.append(subdivisions)

    subdivision_string = ""
    for letter in password:
        if letter not in abc:
            continue

        index = abc.index(letter)
        subdivision_value = normalized_ranges[2][index]  # Use Y[2] for the values
        #print(subdivision_value)
        subdivision_string += f"{subdivision_value:.2f},"  # Format as a string with 2 decimal places

    return subdivision_string[:-1]


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


def permute_block_inverse(block, block_size):
    z0 = [-1, 28, 3.4]
    dr = 0.01
    R = 65
    Z = [[], [], []]

    _, Z[1], _, _, _ = run(z0, dr, R, lorenz)
    sequence = list(set(int(i) for i in Z[1]))

    # Construct the inverse permutation map
    inverse_permutation_map = [-1] * block_size
    for i in range(block_size):
        chaotic_index = sequence[i] % block_size
        inverse_permutation_map[chaotic_index] = i

    # Apply inverse permutation
    unpermuted_block = ""
    for i in range(block_size):
        new_pos = inverse_permutation_map[i]
        unpermuted_block += block[new_pos]

    return unpermuted_block


block_size = 32

def encrypt(password):
    h = 0
    password = normalize_abc(password)
    password_bits = prepare_password(password, block_size=block_size)
    chaotic_seq_bits = generate_chaotic_sequence(bits_per_value=16)

    for i in range(0, len(password_bits), block_size):
        block = password_bits[i:i + block_size]

        # Permutation of the block
        block = permute_block(block, block_size)

        # Preparing chaotic sequence
        chaotic_chunk = chaotic_seq_bits[:block_size].ljust(block_size, '0')
        chaotic_seq_bits = chaotic_seq_bits[block_size:]
        chaotic_value = int(chaotic_chunk, 2)

        byte_values = [int(block[i:i + 8], 2) for i in range(0, len(block), 8)]  # Convert from string to bytes
        block_bytes = bytes(byte_values)
        block_int = int.from_bytes(block_bytes, byteorder='big')

        # Encryption Algorithm
        # Bitwise XOR
        xored_value = block_int ^ chaotic_value

        # Rotate (chaotic amount example)
        rotation_amount = chaotic_value % block_size
        rotated_value = (xored_value >> rotation_amount) | (xored_value << (block_size - rotation_amount))

        # Modular Addition
        h = (h + rotated_value) % 2 ** block_size

    return h

# encrypted_password = encrypt()
# print(encrypted_password)

#use thhis method to run the class
def generate_password_hash():
    password = get_word()
    encrypted_password = encrypt(password)
    return encrypted_password, password

generate_password_hash()
#print(generate_password_hash())