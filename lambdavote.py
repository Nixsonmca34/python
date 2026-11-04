age=int(input("Enter your age:"))
vote=lambda age:"Eligible to vote" if age >= 18 else"Not Eligible to vote"
print(vote(age))
