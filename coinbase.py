from dotenv import load_dotenv
import requests
import argparse
import sys
import os



load_dotenv()



def main():
    try:
        api_key = os.getenv("COINBASE_API_KEY")
        url = "https://rest.coincap.io/v3/assets/bitcoin"

        headers = {
                "Authorization": f"Bearer {api_key}"
                }

        parser = argparse.ArgumentParser()
        # Check for missing argument
        if len(sys.argv) == 1:
            print("Missing Command-line argument")

            sys.exit(1)

        # Define expected argument

        parser.add_argument("number")
        args = parser.parse_args()



        option = float(args.number)

        # Check if option is allowed
        if option not in [1, 1.5, 2, 2.5]:
            sys.exit(1)

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            value = response.json()
            rate = value["data"]["priceUsd"]
            result = float(rate) * option

            # round result to 4 decimal places (float)
            rate_float = round(result, 4)

            # print with commas and 4 decimal places formatting
            print(f"${rate_float:,.4f}")

        else:
            raise ValueError
        
    except requests.RequestException:
        sys.exit()

    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

if __name__ == "__main__":
    main()
