# Stock Portfolio Tracker using Python

# Dictionary to store stock details
portfolio = {}

print("===== Welcome to Stock Portfolio Tracker =====")

while True:

    # Taking stock name from user
    stock = input("\nEnter stock name (or type 'done' to finish): ").title()

    # Exit condition
    if stock == "Done":
        break

    # Taking quantity input
    quantity = int(input("Enter quantity of shares: "))

    # Taking price input
    price = float(input("Enter price per share: "))

    # Calculating total value
    total_value = quantity * price

    # Storing data in dictionary
    portfolio[stock] = {
        "Quantity": quantity,
        "Price": price,
        "Total Value": total_value
    }

print("\n===== Your Stock Portfolio =====")

grand_total = 0

# Displaying portfolio details
for stock, details in portfolio.items():

    print("\nStock Name:", stock)
    print("Quantity:", details["Quantity"])
    print("Price per Share:", details["Price"])
    print("Total Value:", details["Total Value"])

    grand_total += details["Total Value"]

# Display total investment
print("\nTotal Investment Value:", grand_total)

print("\nThank you for using Stock Portfolio Tracker!")
