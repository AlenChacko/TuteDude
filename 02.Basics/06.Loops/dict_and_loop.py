user = {
    "user_name": "user123",
    "password": "test@123",
    "email": "user123@example.com",
    "address": "ABC Road,1111",
    "country": "Australia",
}
print(user)

sensitive_info = ["password", "address", "phone"]

for item in sensitive_info:

    if item in user:
        print(f"Key = {item}, Value = {user[item]}")
        user.pop(item)

    else:
        print(f"{item} not present")

print(user)
