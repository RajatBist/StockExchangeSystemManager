import random
Dollars = 10000
Day = 1
Companies = ["Facebook", "Amazon", "Apple", "Netflix", "Google"]

#prices
Facebook_pr = 309 
Amazon_pr = 3400
Apple_pr = 134
Netflix_pr = 553
Google_pr = 2267

CompanyPrices = [Facebook_pr, Amazon_pr, Apple_pr, Netflix_pr, Google_pr]

#number of shares
Facebook_sh = 0 
Amazon_sh = 0
Apple_sh = 0
Netflix_sh = 0
Google_sh = 0

CompanyShares = [Facebook_sh, Amazon_sh, Apple_sh, Netflix_sh, Google_sh]

#volume
Facebook_vol = 0
Amazon_vol = 0
Apple_vol = 0
Netflix_vol = 0
Google_vol = 0

CompanyCol = [Facebook_vol, Amazon_vol, Apple_vol, Netflix_vol, Google_vol]

#differences/changes in price (random initials)
Facebook_diff = 10
Amazon_diff = 200
Apple_diff = 5
Netflix_diff = 23
Google_diff = 147

while True:
  if Dollars <= 0 and (Facebook_sh + Amazon_sh + Apple_sh + Netflix_sh + Google_sh) == 0:
    break
  print("Day" + str(Day))
  while True:
    print("From which company would you like to buy shares? \n (1:Facebook 2:Amazon 3:Apple 4:Netflix 5:Google) [ (sell) to exit ]")
    Company = input()
    if Company == 'sell':
      break
    else:
      Company = int(Company)
      print("The price of a share from " +Companies[Company-1]+ " is " +str(CompanyPrices[Company-1])+" Dollars")
      print("You have " + str(Dollars)+" Dollars")
      print("How many shares would you like to buy?")
      Quantity = int(input())
      Cost = Quantity * CompanyPrices[Company-1]
      while Cost > Dollars:
        print("You don't have enough money for this transaction.")
        Quantity = int(input())
        Cost = Quantity * CompanyPrices[Company-1]
      Dollars = Dollars-Cost
      print("You now have " + str(Dollars) + " Dollars")
      CompanyShares[Company-1] += Quantity
      print("You now have " + str(CompanyShares[Company-1]) + " Shares of " + Companies[Company-1])
  while True:
    print("From which company would you like to sell shares? \n (1:Facebook 2:Amazon 3:Apple 4:Netflix 5:Google) [ (next) to exit ]")
    Company = input()
    if Company == "next":
        break
    else:
        Company = int(Company)
        print("The price of a share from " +Companies[Company-1]+ " is " +str(CompanyPrices[Company-1])+" Dollars")
        print("You have " + str(Dollars)+" Dollars")
        print("How many shares would you like to sell?")
        Quantity = int(input())
        while Quantity > CompanyShares[Company-1]:
          print("You don't have enough shares for this transaction.")
          Quantity = int(input())
        Value = Quantity * CompanyPrices[Company-1]
        Dollars = Dollars+Value
        print("You now have " + str(Dollars) + " Dollars")
        CompanyShares[Company-1] -= Quantity
        print("You now have " + str(CompanyShares[Company-1]) + " Shares of " + Companies[Company-1])
  
  Facebook_pr = random.randint((Facebook_pr-Facebook_diff), (Facebook_pr+Facebook_diff))
  Amazon_pr = random.randint((Amazon_pr-Amazon_diff), (Amazon_pr+Amazon_diff))
  Apple_pr = random.randint((Apple_pr-Apple_diff), (Apple_pr+Apple_diff))
  Netflix_pr = random.randint((Netflix_pr-Netflix_diff), (Netflix_pr+Netflix_diff))
  Google_pr = random.randint((Google_pr-Google_diff), (Google_pr+Google_diff))

  Day+=1
