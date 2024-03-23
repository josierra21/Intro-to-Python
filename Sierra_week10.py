#DSC510
#Week10: Introduction to Web Services
#Programming Assignment Week10
#Author: Joanna Sierra-Mendoza
#02/16/24

import requests
from pprint import pprint

def api_call():
    try:
        url = "https://api.chucknorris.io/jokes/random?category=science"
        response = requests.get(url)
        joke = response.json()['value']
        response.raise_for_status()
    except request.exceptions.HTTPError as errh:
        raise SystemExit(err)
    pprint(joke)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def another_one():
    input_two = input("Would you like another joke? Enter Y for new joke or any other character to END\n")
    next_response = input_two.lower()
    if next_response == 'y':
        api_call()
        another_one()
    else:
        print("Thank you for using my program!")
        exit()

def main():
    print("*Welcome to the Chuck Norris Joke Provider*")
    user_input=input("Would you like a joke? Enter Y for joke or any other character to END\n")
    user_response = user_input.lower()
    if user_response == 'y':
        api_call()
        another_one()
    else:
        print("Thank you for using my program!")
        exit()

if __name__ == "__main__":
    main()



