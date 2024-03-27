
def generate_key_table(keyword):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key_table = ''
    keyword = keyword.upper().replace('J', 'I')
    for char in keyword:
        if char not in key_table:
            key_table += char
    for char in alphabet:
        if char not in key_table:
            key_table += char
    return key_table

def prepare_plaintext(plaintext):
    plaintext = plaintext.upper().replace('J', 'I')
    plaintext = ''.join(filter(str.isalpha, plaintext))
    plaintext_pairs = []
    i = 0
    while i < len(plaintext):
        if i == len(plaintext) - 1 or plaintext[i] == plaintext[i + 1]:
            plaintext_pairs.append(plaintext[i] + 'X')
            i += 1
        else:
            plaintext_pairs.append(plaintext[i] + plaintext[i + 1])
            i += 2
    return plaintext_pairs

def encrypt_digraph(digraph, key_table):
    idx1 = key_table.index(digraph[0])
    idx2 = key_table.index(digraph[1])
    row1, col1 = idx1 // 5, idx1 % 5
    row2, col2 = idx2 // 5, idx2 % 5
    if row1 == row2:
        return key_table[row1 * 5 + (col1 + 1) % 5] + key_table[row2 * 5 + (col2 + 1) % 5]
    elif col1 == col2:
        return key_table[((row1 + 1) % 5) * 5 + col1] + key_table[((row2 + 1) % 5) * 5 + col2]
    else:
        return key_table[row1 * 5 + col2] + key_table[row2 * 5 + col1]

def encrypt(plaintext, keyword):
    key_table = generate_key_table(keyword)
    plaintext_pairs = prepare_plaintext(plaintext)
    ciphertext = ''
    for pair in plaintext_pairs:
        ciphertext += encrypt_digraph(pair, key_table)
    return ciphertext

def decrypt_digraph(digraph, key_table):
    idx1 = key_table.index(digraph[0])
    idx2 = key_table.index(digraph[1])
    row1, col1 = idx1 // 5, idx1 % 5
    row2, col2 = idx2 // 5, idx2 % 5
    if row1 == row2:
        return key_table[row1 * 5 + (col1 - 1) % 5] + key_table[row2 * 5 + (col2 - 1) % 5]
    elif col1 == col2:
        return key_table[((row1 - 1) % 5) * 5 + col1] + key_table[((row2 - 1) % 5) * 5 + col2]
    else:
        return key_table[row1 * 5 + col2] + key_table[row2 * 5 + col1]

def decrypt(ciphertext, keyword):
    key_table = generate_key_table(keyword)
    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        plaintext += decrypt_digraph(ciphertext[i:i+2], key_table)
    return plaintext

def main():
    plaintext = input("Enter the plaintext: ")
    keyword = input("Enter the keyword: ")
    ciphertext = encrypt(plaintext, keyword)
    print("Encrypted ciphertext:", ciphertext)
    decrypted_plaintext = decrypt(ciphertext, keyword)
    print("Decrypted plaintext:", decrypted_plaintext)

if __name__ == "__main__":
    main()
