print("Welcome to my vehicle loan calculator")


def vehicleLoanCalcToFile():
    carType = input("What kind of car is it? \n"
                    "Year, Make, Model: \n")
    carCost = float(input("What is the cost of the car by itself: \n"))
    carTax = float(input("What is the sales tax rate? \n"
                         "ex: 7% = 7, 10.5% = 10.5: \n"))
    carTax2 = carTax / 100
    dealerFee = float(input("Are there any dealership fees? \n"
                            "If none enter a zero: \n"))
    carFees = float(input("What are the title and license fees: \n"))
    downPayment = float(input("Do you have a down payment? \n"
                              "If none enter a zero: \n"))
    rebates = float(input("Are there any incentives or rebates for this vehicle? \n"
                          "Enter amount: \n"))
    getSalesTax = carCost * carTax2
    carTotalPrice = carCost + getSalesTax + dealerFee + carFees - downPayment - rebates
    print("The vehicles total price before financing is:", carTotalPrice)
    lengthMonths = int(input("How long is the loan in months: \n"))
    intRate = float(input("What is the annual interest rate: \n"))
    carInt = intRate / 100 / 12  # get monthly interest
    monthlyPayment = carTotalPrice * (1 + carInt) ** lengthMonths * carInt / ((1 + carInt) ** lengthMonths - 1)
    print("Your monthly payment is: $" + ('%0.2f' % monthlyPayment), "for", lengthMonths, "months")
    filename = input("Enter a filename to save this vehicle info to: \n")  # Get user to input a file name
    print(f'Attempting to open file named \'{filename}\'')
    with open(filename, 'w') as v_info:  # opening user named file for writing as v_info
        v_info.write(carType + "\n")  # write car type to file
        v_info.write("Total vehicle price: " + str(carTotalPrice) + "\n")  # write total vehicle price
        v_info.write("Your monthly payment is: $" + ('%0.2f' % monthlyPayment) + " for " + str(lengthMonths) + " months"
                     + "\n")  # write monthly payment and length of loan to file
        v_info.close()  # File closed, we are done writing
    print("Saved to text file named:", filename) # reminding user what their filename is
    input("Press ENTER to end program")


vehicleLoanCalcToFile()


