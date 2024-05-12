import random
import string

def pas(l):
    ch = (string.digits + string.ascii_letters + string.punctuation + string.hexdigits)
    p = "".join(random.choice(ch) for _ in range (l))
    return p

def main():
    while True:
        try:
            length = int(input("enter the password length: "))
            p = pas(length)
            print("Password: ", p)
            choice = input("Enter yes to generate again.").lower()
            if choice != "yes":
                break

        except ValueError:
            print("Invalid input! Please enter a valid length")

if __name__ == "__main__":
    main()