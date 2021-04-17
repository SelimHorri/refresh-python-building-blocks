
print("\n*****************************\n")

try :
	while True :
		age = input("give your age : \n")
		if int(age) >= 25 :
			print("old")
		elif int(age) < 25 :
			print("young")
		else :
			break
except ValueError :
	print("do not ruin my programs with Strings")

print("\n*****************************\n")
