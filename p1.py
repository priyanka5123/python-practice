score = int(input("Enter your score: "))

if score < 70:
    print("Needs Improvement.")
elif score > 70 and score < 90:
    print("Good.")
else:
    print("Excellent.")


# Dynamically Typed: You don’t need to declare the type of variables
x = 10      # x is an integer
x = "Hello" # Now, x is a string 
