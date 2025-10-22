try:    
    a=int(input("hey enter a number : "))
    print(a)

except ValueError as v:
    print("Heyy its value error")
    print(v)
except Exception as e:
    print(e)

print("thankyou")