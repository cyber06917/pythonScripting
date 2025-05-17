import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):  # Run 10 questions
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        error_time = 0  # Reset for each question

        while error_time < 3:
            try:
                prediction = int(input(f"{x} + {y} = "))
                if prediction == answer:
                    score += 1
                    break  # Correct, go to next question
                else:
                    print("EEE")
                    error_time += 1
            except ValueError:
                print("EEE")
                error_time += 1

        if error_time == 3:
            print(f"{x} + {y} = {answer}")

    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]: #Validate if it's in between value 1 to 3
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")


if __name__ == "__main__":
    main()
