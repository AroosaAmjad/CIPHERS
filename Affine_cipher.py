import string

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def find_coprimes(n):
    coprimes = []
    for i in range(1, n):
        if gcd(i, n) == 1:
            coprimes.append(i)
    return coprimes

def affine_encrypt(plaintext, key_a, key_b):
    plaintext = plaintext.upper().replace(" ", "")
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            x = ord(char) - ord('A')
            encrypted_text += chr(((key_a * x + key_b) % 26) + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def affine_decrypt(ciphertext, key_a, key_b):
    m = len(string.ascii_uppercase)
    a_inv = mod_inverse(key_a, m)
    if a_inv is None:
        return "Key 'a' is not coprime with 26. Choose another key."
    
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            y = ord(char) - ord('A')
            decrypted_text += chr(((a_inv * (y - key_b)) % 26) + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("Coprimes with 26 for key 'a':", find_coprimes(26))
    key_a = int(input("Enter key 'a' (must be coprime with 26): "))
    
    key_b = int(input("Enter key 'b' (any integer): "))
    plaintext = input("Enter plaintext: ")

    encrypted_text = affine_encrypt(plaintext, key_a, key_b)
    print("Encrypted text:", encrypted_text)

    decrypted_text = affine_decrypt(encrypted_text, key_a, key_b)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
