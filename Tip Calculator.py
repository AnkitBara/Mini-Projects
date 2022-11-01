print("🤑 Welcome to the Tip Calculator! 🤑")

bill=int (input("What was the total bill? Rs."))

tip= int(input("How much tip would you like yo give? 10,12 or 15 "))
totaltip=(bill* tip)/100
split=int(input("How many People to split the bill? "))
totalbill=(totaltip+bill)/split

print("Your tip is RS",totalbill)