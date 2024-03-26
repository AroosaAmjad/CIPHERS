
def prepare_plaintext(plaintext):
    plaintext = plaintext.replace(" ", "").upper()  # Remove spaces and convert to uppercase
    return plaintext

def construct_transposition_matrix(plaintext, key):
    num_cols = len(key)
    num_rows = len(plaintext) // num_cols + (1 if len(plaintext) % num_cols != 0 else 0)
    transposition_matrix = [[' ' for _ in range(num_cols)] for _ in range(num_rows)]
    for i, char in enumerate(plaintext):
        transposition_matrix[i // num_cols][i % num_cols] = char
    return transposition_matrix

def rearrange_columns(transposition_matrix, key):
    num_cols = len(key)
    rearranged_matrix = [[None] * num_cols for _ in range(len(transposition_matrix))]
    for i, col_idx in enumerate(key):
        for j in range(len(transposition_matrix)):
            rearranged_matrix[j][i] = transposition_matrix[j][col_idx - 1]
    return rearranged_matrix

def read_encrypted_text(rearranged_matrix):
    encrypted_text = ''
    for col in rearranged_matrix:
        encrypted_text += ''.join(col)
    return encrypted_text

def read_decrypted_text(transposition_matrix):
    decrypted_text = ''
    for row in transposition_matrix:
        for char in row:
            if char is not None:
                decrypted_text += char
    return decrypted_text

def encrypt(plaintext, key):
    plaintext = prepare_plaintext(plaintext)
    transposition_matrix = construct_transposition_matrix(plaintext, key)
    rearranged_matrix = rearrange_columns(transposition_matrix, key)
    encrypted_text = read_encrypted_text(rearranged_matrix)
    return encrypted_text

def reconstruct_transposition_matrix(encrypted_text, key):
    num_cols = len(key)
    num_rows = len(encrypted_text) // num_cols + (1 if len(encrypted_text) % num_cols != 0 else 0)
    transposition_matrix = [[' ' for _ in range(num_cols)] for _ in range(num_rows)]
    for i, char in enumerate(encrypted_text):
        transposition_matrix[i % num_rows][i // num_rows] = char
    return transposition_matrix

def reverse_column_rearrangement(transposition_matrix, key):
    num_cols = len(key)
    original_matrix = [[None] * num_cols for _ in range(len(transposition_matrix))]
    for i, col_idx in enumerate(key):
        for j in range(len(transposition_matrix)):
            original_matrix[j][col_idx - 1] = transposition_matrix[j][i]
    return original_matrix

def decrypt(encrypted_text, key):
    transposition_matrix = reconstruct_transposition_matrix(encrypted_text, key)
    original_matrix = reverse_column_rearrangement(transposition_matrix, key)
    decrypted_text = read_decrypted_text(original_matrix)
    return decrypted_text

def main():
    plaintext = input("Enter the plaintext: ")
    print("Please provide the key in the format of comma-separated numbers.")
    print("For example, if the key is [1, 2, 3, 4], enter it as '1,2,3,4'.")
    key = input("Enter the key: ").replace(" ", "")  # Remove spaces from the key
    key = list(map(int, key.split(',')))
    
    encrypted_text = encrypt(plaintext, key)
    print("Encrypted Text:", encrypted_text)
    
    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
