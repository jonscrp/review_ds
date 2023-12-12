
number = input("Enter a number")


if( int(number) < 5):
    print("number:", number)
else:
    raise Exception("Number is greater or equal to 5")
