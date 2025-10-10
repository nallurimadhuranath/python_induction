# Q7
num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")

# Q8
a, b, c = map(int, input("Enter three numbers: ").split())
print("Largest:", max(a, b, c))

# Q9
num = int(input("Enter a number: "))
print(num % 3 == 0 and num % 5 == 0)

# Q11
for i in range(1, 51):
    if i > 40:
        break
    if i % 3 == 0:
        continue
    print(i)

# Q17
n = int(input("Enter number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial:", fact)

#Q18

tup = ((1,2),(3,4))
for x,y in tup:
    print(x,y)

# Q29
keys = ["a","b","c"]
vals = [1,2,3]
print(dict(zip(keys, vals)))

# Q33

s = input("Enter string: ").lower()
print(sum(1 for ch in s if ch in "aeiou"))


# Q42
def flatten(lst):
    result = []
    for x in lst:
        if isinstance(x, list):
            result.extend(flatten(x))
        else:
            result.append(x)
    return result

# Q43
def maximum(lst):
    max_val = lst[0]
    for x in lst:
        if x > max_val:
            max_val = x
    return max_val