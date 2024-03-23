#DSC510
#Week5
#Programming Assignment Week5
#Author Joanna Sierra-Mendoza
#01/13/24

print("Welcome to my Calculator!")
numOne = int(float(input("Enter First Number: ")))
numTwo = int(float(input("Enter Second Number: ")))
print("Enter which operation would you like to perform?")
operation = input("Enter any of these characters for specific operation +,-,*,/: ")

performCalculation = 0.0
if operation == '+':
    performCalculation = numOne + numTwo
elif operation == '/':
    performCalculation = numOne / numTwo
elif operation == '*':
    performCalculation = numOne * numTwo
elif operation == '-':
    performCalculation = numOne - numTwo
else:
    print("Input character is not recognized!")

print(numOne, operation , numTwo, "=", performCalculation)

def main():
    total = 0.0
    count = 0

    price = float(input("Enter a Price or -1 to Quit: "))
    while price >= 0.0:

        if price >= 0.0:
            total = total + price
            count = count + 1
        price = float(input("Enter a Price or -1 to Quit: "))

    if count > 0:
        calculateAverage = total / count
        print("Average Price is: ")
        print('${}'.format(calculateAverage))
    else:
        print("No Data Was Entered.")


    for runamount in range(count):
        print("~Number of Loops Completed~")
        print("Ran the loop " + str(count + 1) + " times")
        break

if __name__ == "__main__":
    main()








