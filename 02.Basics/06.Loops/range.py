# range() is a built-in function for generating integers

# this will print 0 to 4, starts from 0 and ends one step before the limit
for i in range(5):
    print(i)
# this will print 5 to 15 , first one is the start, next one is stop limit
for i in range(5, 16):
    print(i)

# this will print the intergers from a start to end following a step
# start from 20 and goes to one stpe before 40, the step is 2
# start from 20 then follow the step, 22,24,26,...38
for i in range(20, 40, 2):
    print(i)


# negative steping (reverse loop)
for i in range(10, 1, -1):
    print(i)


# range with list
nums = list(range(1, 11))
print(nums)


# range with len
lst = ["alen", "amal", "arjun", "albin"]
for i in range(len(lst)):
    print(i, lst[i])


# range in conditional loops
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is Even")
