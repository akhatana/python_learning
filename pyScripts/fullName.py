firstName = "aditya"
lastName = "khatana"
fullName = f"{firstName} {lastName}"
message = "Hello " + fullName.title() + " !"
print (message)

#strip whiteSpace using rstrip()

Name1= "aditya"
Name2="aditya  "

print(Name1==Name2.rstrip())
#Fibonacci series
t1=0
t2=1
n=10
print(f"Fibonacci series' below\n\t|{t1}|\n\t|{t2}|")
for i in range(n):
	sum=t1+t2
	print(f"\t|{sum}|")
	t1=t2
	t2=sum
