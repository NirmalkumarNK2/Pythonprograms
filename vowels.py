n = input("Enter a word:")
c = 0
for i in n:
    if i in 'aeiouAEIOU':
        c += 1
print(c)
