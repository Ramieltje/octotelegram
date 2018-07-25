#########################################################################
#Object of code is to count  1-10 and back, printing only the final num.#

#i = 10
#count = 1
#while count < i:
#    count = count + 1
#while count > 0:
#    count = count + 1
#print(count)
#above code non-functioning. Second while statement goes to infinity

#i = 10
#count = 1
#print("Starting first loop...")
#while count < i:
#    count = count + 1
#print("First loop complete.")
#print("Starting second loop...")
#while count > 0:
#    count = count + 1
#print("Second loop complete...")
#print("output" + count)
#above code adds print statements in order to check where the problem occurs
#print statements no longer necessary once code is repaired

i = 10
count = 1
print("Starting first loop...")
while count < i:
    count = count + 1
print("First loop complete.")
print("Starting second loop...")
while count > 0:
    count = count - 1             #changes operator from plus to minus
print("Second loop complete...")
print(count)
