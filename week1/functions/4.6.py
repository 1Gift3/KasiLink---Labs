def computepay(hours, rate):
    print("In computepay", hours, rate)
    if fh > 40 :
       reg = rate * hours
       otp = (fh - 40.0) * (fr * 0.5)
       pay =  reg + otp 
    else:
        pay = hours * rate
    return pay
    
hours = input("Enter hours: ")
rate = input("Enter rate:")
fh  = float(hours)
fr = float(rate)


xp = computepay(fh, fr)
      

print("Pay", xp)
