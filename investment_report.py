startbalance=float(input("Enter the investment account: "))
years=int(input("Enter the number of years: "))
rate=int(input("Enter the rate percentage: "))

rate=rate/100

totInterest=0.0

print("%4s%18s%10s%16s" % \
      ("Year","Starting balance","Interest","Ending balance"))

for year in range(1,years + 1):
    interest =startbalance*rate
    endBalance=startbalance+interest
    print("%4d%18.2f%10.2f%16.2f" % \
          (year,startbalance,interest,endBalance))
    balance=endBalance
    totInterest+=interest

print("Ending balance:$%0.2f" % endBalance)
print("Total interest earned: $%0.2f" %totInterest)