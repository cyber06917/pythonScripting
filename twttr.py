import re

def main():
    result = shorten("hay' it's me !")
    print(f"Output: {result}")


def shorten(word):
    # Syntax: re.sub(pattern, replacement, string, count=0, flags=0)
    return re.sub(r'[aeiou]', '', word)



if __name__ == "__main__":
    main()
