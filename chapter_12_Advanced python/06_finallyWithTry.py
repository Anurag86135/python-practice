def main():
    try:
        a=int(input("Enter a number :"))
        print(a)
        return
    
    except Exception as e:
        print(e)
        return
    
    finally:
        print("Hey! I am an inside of finally")# it will run int any case either code is write or has an an error

    # print("you are inside finally") it won't be run due to return keyword

main()