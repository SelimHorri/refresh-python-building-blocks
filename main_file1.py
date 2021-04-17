
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

elements = "9, 2, 7, 6, 0, 25, 58, 10, 2"
print(elements.split(", "))
for i in elements.split(", ") :
	print(i)

print("\n*****************************\n")


