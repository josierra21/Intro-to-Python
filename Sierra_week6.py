#DSC510
#Week6: Strings and Lists
#Programming Assignment Week6
#Author Joanna Sierra-Mendoza
#01/20/24

def main():
    def largest(temps):
        largest_temp = float('-inf')
        for temp in temps:
            largest_temp = max(largest_temp, temp)
        return largest_temp

    def smallest(temps):
        smallest_temp = float('inf')
        for temp in temps:
            smallest_temp = min(smallest_temp, temp)
        return smallest_temp

    temperatures = []
    while True:
        user_input = input("Please enter a Temperature or use 'Q' to Quit:")
        if user_input == 'Q' or user_input == 'q':
            print("Thank you for using my program!")
            break
        try:
            temp_value = int(user_input)
            temperatures.append(temp_value)
            largest_temp = largest(temperatures)
            smallest_temp = smallest(temperatures)
            print(f"You Have Entered {len(temperatures)} Temperature(s), the Largest Temperature Entered is {largest_temp}, and the Smallest Temperature Entered is {smallest_temp}")
        except ValueError:
            print("Please Enter an Integer")


if __name__ == "__main__":
    main()





