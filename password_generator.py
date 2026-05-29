import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("================================")
    print("      Password Generator        ")
    print("================================\n")

    try:
        length = int(input("Password length (press Enter for 12): ") or 12)
    except ValueError:
        length = 12

    use_digits = input("Include numbers? (y/n): ").strip().lower() != 'n'
    use_special = input("Include special characters? (y/n): ").strip().lower() != 'n'

    print("\n--- Your Generated Password ---")
    for i in range(1, 4):
        pwd = generate_password(length, use_digits, use_special)
        print(f"Option {i}: {pwd}")

    print("\nDone! Copy and use any password above.")

if __name__ == "__main__":
    main()
