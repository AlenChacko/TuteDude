name = "John"
age = 20
percentage = 85.5

student = ["John", 20, 85.5]
print(type(student))

# Creating List
# 1.EMPTY LIST
a = []
print(a)  # empty list
b = list()  # empty list

# 2. LIST WITH VALUES
colors = ["red", "blue", "green"]

# From another data type
s = "python"
lst = list(s)
print(lst)

# matrix list
matrix_1 = [
    [1, 2, 3],  # row 1
    [4, 5, 6],  # row 2
    [7, 8, 9]  # row 3
]


# accessing elements
# matrix[row][column]
matrix_2 = [
    [10, 20, 30],
    [40, 50, 60]
]

print(matrix_2[0][1])   # 20
print(matrix_2[1][2])   # 60


# loop
matrix_3=[
    [54,67,23,76],
    [12,4,55],
    [45,87,23,78,23,87,23],
    [12,45]
]

for row in matrix_3:
    for item in row:
        print(item)


print(matrix_3[2][4])