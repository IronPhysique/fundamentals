import re

class PasswordStrengthChecker:
    def __init__(self, password_file):
        self.common_passwords = self.load_common_passwords(password_file)
        self.history = {}

    def load_common_passwords(self, filepath):
        try:
            with open(filepath, 'r') as file:
                return set(password.strip() for password in file)
        except FileNotFoundError:
            print(f"Error: File '{filepath}' not found.")
            return set()
        except Exception as e:
            print(f"An error occurred: {e}")
            return set()

    def check_strength(self, password):
        if password in self.common_passwords:
            return "Very Weak"
        score = 0
        length = len(password)
        if length >= 8:
            score += 1
        if length >= 12:
            score += 1

        if re.search(r'[A-Z]', password):
            score += 1
        if re.search(r'[a-z]', password):
            score += 1
        if re.search(r'\d', password):
            score += 1
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            score += 1

        if score <= 3:
            return "Weak"
        elif score <= 5:
            return "Moderate"
        elif score <= 7:
            return "Strong"
        else:
            return "Very Strong"

    def add_to_history(self, password, strength):
        self.history[password] = strength

def main():
    password_file = 'commonpass.txt'
    checker = PasswordStrengthChecker(password_file)
    print("Password Strength Checker (type 'quit' to exit)")

    while True:
        password = input("Enter a password to check: ")
        if password.lower() == 'quit':
            print("Password check history:")
            for pwd, strength in checker.history.items():
                print(f"Password: {pwd}, Strength: {strength}")
            break

        if password in checker.history:
            print(f"Password '{password}' has already been checked and is {checker.history[password]}.")
        else:
            strength = checker.check_strength(password)
            checker.add_to_history(password, strength)
            print(f"The password '{password}' is {strength}.")

if __name__ == "__main__":
    main()
