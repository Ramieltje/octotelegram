for i in range(1, 9): #'for' used to set an instance.
    print(i)          #'prints the series of numbers between the upper and lower bounds'
#prints numseries 1-9
#original error was use of "within" ipv function 'in'

#problem-2: only prints up to
#increase upper bound to 10

print('\n') #inserts blank line

for i in range(1, 10):
    print(i)


a = "Hello, world"
b = 5
print(a.endswith("d"))
#print(b.endswith("d"))
#Line 18 tries to test whether an integer end with 'd' which is clearly impossible
