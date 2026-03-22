import random
import string

print("=== Password Generator ===")

length = int(input("Enter password length: "))
print("Complexity: 1=Letters only  2=Letters+Numbers  3=Letters+Numbers+Symbols")
choice = input("Choose complexity (1/2/3): ")

chars = string.ascii_letters
if choice == "2":
    chars += string.digits
elif choice == "3":
    chars += string.digits + string.punctuation

password = "".join(random.choice(chars) for _ in range(length))
print("Generated Password:", password)
