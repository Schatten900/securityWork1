from attack import VigenereAttack
from vigenere import Vigenere

def main():
    algorithm = Vigenere()
    attackEN = VigenereAttack(False)
    attackPT = VigenereAttack(True)

    while True:
        print("=== Vigenere Cipher System ===")
        print("1. Encrypt message")
        print("2. Decrypt message")
        print("3. Simulate attack")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            msg = input("Enter the message: ")
            key = input("Enter the key: ")
            print("Encrypted message:", algorithm.encrypt(msg, key))

        elif choice == "2":
            msg = input("Enter the encrypted message: ")
            key = input("Enter the key: ")
            print("Decrypted message:", algorithm.decrypt(msg, key))

        elif choice == "3":
            msg = input("Enter the encrypted message: ")
            lang = input("Message language\n 1 - English \n 2 - Portuguese: ")
            if lang == "2":
                print("Attack result:\n", attackPT.originalText(msg))
            else:
                print("Attack result:\n", attackEN.originalText(msg))

        elif choice == "4":
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
