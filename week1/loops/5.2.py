smallest_no = None
largest_no = None

while True:
    number = input("Enter number: ")
    #print("number:", number)
    if number.lower() == "done":
        break
    try:
        my_value = int(number)

        if smallest_no is None or my_value < smallest_no:
            smallest_no = my_value
        if largest_no is None or my_value > largest_no:
            largest_no = my_value

    except:
        print("Invalid input")
        continue
        

    print(f"Maximum is {largest_no}")
    print(f"Minimum is {smallest_no}")