def main():
    print(f"${value("hello")}")


def value(greeting):
    sentence = greeting.strip().lower()
    if sentence.startswith("h") and not sentence.startswith("hello"):
        return 20
    elif sentence.startswith("h") and sentence.startswith("hello"):
        return 100
    else:
        return 0


if __name__ == "__main__":
    main()




