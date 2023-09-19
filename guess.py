import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    lower_limit = int(input("Enter the lower limit of the range: "))
    upper_limit = int(input("Enter the upper limit of the range: "))

    if lower_limit >= upper_limit:
        print("Invalid range. Please make sure the lower limit is less than the upper limit.")
        return

    secret_number = random.randint(lower_limit, upper_limit)
    attempts = 0

    while True:
        try:
            guess = int(input(f"Guess the number between {lower_limit} and {upper_limit}: "))
            attempts += 1

            if guess < lower_limit or guess > upper_limit:
                print("Your guess is outside the specified range. Try again.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
