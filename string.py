S=input("enter a string")
print("original string:",S)
char=S[0]
S=S.replace(char,'$')
S=char+S[1:]
print(S)
