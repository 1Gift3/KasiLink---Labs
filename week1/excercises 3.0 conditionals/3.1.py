hours = input("Enter amount of hours: ")
rate = input("Enter rate: ")
hourz = float(hours)
ratez = float(rate)
#print(hourz, ratez)

if hourz > 40:
    normal_pay =  hourz * ratez
    otp = (hourz - 40) * (ratez * 0.5)
    #print("Overtime_pay", normal_pay)
    Overtime_pay = otp + normal_pay
    print(Overtime_pay)

else:
    X = hourz *ratez
    print(X)

