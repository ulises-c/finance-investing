# Program to calculate compound interest with monthly contribution at the end of the month
principalinput = input("Enter principal: ")
annualrateinput = input("Enter annual rate: ")
numberoftimescompoundedinput = input("Enter number of times that the interest is compounded per year: ")
yearsinput = input("Time in years: ")
monthlycontributioninput = input("Enter monthly contribution amount: ")

# Convert entered input from strings into integers
principal = int(principalinput)
annualrate = int(annualrateinput) / 100
numberoftimescompounded = int(numberoftimescompoundedinput)
years = int(yearsinput)
monthlycontribution = int(monthlycontributioninput)

# Calculate the compound interest plus the principal
preliminarynumber = (1 + (annualrate / numberoftimescompounded))
raisedtopower = (numberoftimescompounded * years)
compoundinterestplusprincipal = principal * (preliminarynumber ** raisedtopower)
print("The compound interest plus the principal is:", compoundinterestplusprincipal)

# Calculate the future value with deposits
oneplus = (1 + (annualrate / numberoftimescompounded))
raisedtopower2 = (numberoftimescompounded * years)
ratedividedbynumberoftimes = annualrate / numberoftimescompounded
halfdone = (((oneplus ** raisedtopower2) - 1) / ratedividedbynumberoftimes)
futurevaluewithdeposits = monthlycontribution * halfdone
print("Future value with deposits:", futurevaluewithdeposits)

totalamount = compoundinterestplusprincipal + futurevaluewithdeposits
print("Total Amount:", totalamount)
