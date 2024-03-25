
import numpy as np

def take_matrix_input(matrix_size):
    matrix = []
    print(f"Enter the elements of the {matrix_size}x{matrix_size} key matrix:")
    for i in range(matrix_size):
        row = []
        for j in range(matrix_size):
            element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

def plaintext_to_numerical(plaintext):
    numerical_values = []
    for char in plaintext:
        if char.isalpha():
            numerical_values.append(ord(char.upper()) - ord('A'))
    return numerical_values

def pad_plaintext(plaintext, key_size, filler='X'):
    padded_plaintext = plaintext
    remainder = len(plaintext) % key_size
    if remainder != 0:
        padding_length = key_size - remainder
        padded_plaintext += filler * padding_length
    return padded_plaintext

def split_into_blocks(numerical_values, block_size):
    blocks = [numerical_values[i:i+block_size] for i in range(0, len(numerical_values), block_size)]
    return blocks

def multiply_with_key(blocks, key_matrix):
    modulo = 26  # Size of the English alphabet
    encrypted_blocks = []
    for block in blocks:
        encrypted_block = [sum([block[i] * key_matrix[i][j] for i in range(len(block))]) % modulo for j in range(len(key_matrix))]
        encrypted_blocks.append(encrypted_block)
    return encrypted_blocks

def multiply_with_inverse_key(blocks, inv_key_matrix):
    modulo = 26  # Size of the English alphabet
    decrypted_blocks = []
    for block in blocks:
        decrypted_block = [int(sum([block[i] * inv_key_matrix[i][j] for i in range(len(block))]) % modulo) for j in range(len(inv_key_matrix))]
        decrypted_blocks.append(decrypted_block)
    return decrypted_blocks

def numerical_to_ciphertext(encrypted_blocks):
    ciphertext = ''
    for block in encrypted_blocks:
        ciphertext += ''.join([chr(val + ord('A')) for val in block])
    return ciphertext

def numerical_to_plaintext(decrypted_blocks):
    plaintext = ''
    for block in decrypted_blocks:
        plaintext += ''.join([chr(val + ord('A')) for val in block])
    return plaintext

def main():
    plaintext = input("Enter the plaintext: ")
    key_size = 3  # Size of the key matrix is fixed to 3x3
    key_matrix = take_matrix_input(key_size)
    key_matrix_inv = np.linalg.inv(key_matrix) % 26  # Calculate the inverse of the key matrix modulo the size of the alphabet

    numerical_values = plaintext_to_numerical(plaintext)
    padded_plaintext = pad_plaintext(numerical_values, key_size)
    blocks = split_into_blocks(padded_plaintext, key_size)
    encrypted_blocks = multiply_with_key(blocks, key_matrix)

    # Decryption steps
    decrypted_blocks = multiply_with_inverse_key(encrypted_blocks, key_matrix_inv)
    decrypted_plaintext = numerical_to_plaintext(decrypted_blocks)

    print("Encrypted ciphertext:", numerical_to_ciphertext(encrypted_blocks))
    print("Decrypted plaintext:", decrypted_plaintext)

if __name__ == "__main__":
    main()
