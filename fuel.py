def main():

    while True:
        try:
            percentage = convert("1/4")
            print(gauge(percentage))
            break

        except (ValueError, ZeroDivisionError):
            continue




def convert(fraction):
    try:
        frac = fraction.strip()
        num, denom = map(int, frac.split('/')) #map

        if denom == 0:
            raise ZeroDivisionError

        if num > denom:
            raise ValueError


        return round((num / denom) * 100)

    except ValueError:
        raise ValueError



def gauge(percentage):
    if percentage <= 1:
        return "E"

    elif percentage >= 99:
        return "F"

    else:
        return f"{percentage}%"




if __name__ == "__main__":
    main()
