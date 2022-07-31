a = []
print("Enter the numbers")
for i in range(4):
    a.append(int(input()))
if sorted(a) == a:
    print("Is sorted")
else:
    print("Is not sorted")