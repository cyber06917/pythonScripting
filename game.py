import random


level = int(input("Level: "))

value = None

while True:
    try:    
        if level >= 0:
            if value is None:
                guess = random.randint(1, level)
                value = "value"

            num = int(input("Guess: "))
            if num > guess:
                print("Too large!")
                
            if num < guess:
                print("Too small!")
                
            if num == guess:
                print("Just right!")
                break
    
    except ValueError:
        level = int(input("Level: "))
        value = None
        continue        