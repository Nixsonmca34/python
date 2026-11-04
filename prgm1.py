startYear=int(input("Enter the startyear:"))
lastYear=int(input("Enter the lastyear:"))
endYear=int(input("Enter the endyear:"))
print("List of leap years:")
for Year in range (startYear,endYear):
      if((Year%4==0)and(Year%100!=0))or(Year%400==0):
          print(Year)
