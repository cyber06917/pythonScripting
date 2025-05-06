import inflect

# Initialize inflect engine
n = inflect.engine()

# Initial list of names
names = ["Adieu", "adieu"]

try:
    while True:
        # Take input and strip leading/trailing spaces
        name = input("Name: ").strip()
        
        # Add name to the list if it's not an empty string
        if name != "":
            names.append(name)

except EOFError:
    if len(names) > 2:
        names[2] = "to " + names[2]
    if len(names) == 3:
        # One user name — don't prepend "to", just print without 'and'
        print(", ".join(names))
        exit()
    
    if len(names) == 4:
        output = ', '.join(names[:-1])
        print(f"{output} and {names[-1]}")

    else:
        print(n.join(names))
