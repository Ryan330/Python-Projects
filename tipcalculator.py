#Ask user for total bill amount
total = float(input("What is the total amount of your bill? "))


#Ask user for service rating
rating = input("How was the overall service? Good, Fair, or Bad? ")


#Check user's service rating
if rating == "Good" or rating == "good":
    rating = total * 0.20
elif rating == "Fair" or rating == "fair":
    rating = total * 0.15
elif rating == "Bad" or rating == "bad":
    rating == total * 0.10

print("Tip Amount: $%.2f" % (rating))
print("Total Amount: $%.2f" % (total + rating))