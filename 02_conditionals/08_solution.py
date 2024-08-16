# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("Enter your password: ")
password_length = len(password)

if password_length < 6:
    print("Weak Password")
elif password_length < 10:
    print("Medium Password")
else:
    print("Strong Password")