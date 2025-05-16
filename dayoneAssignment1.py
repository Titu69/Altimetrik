EmployeeID = input("EmployeeID: ")
Name = input("Name: ")
Job= input("Job: ")
BasicPay = float(input("basicpay:"))

#calculating the totalpay
totalpay = BasicPay + (BasicPay*.05) if Job == "manager" else BasicPay + (BasicPay*.08) if Job == "developer" else  BasicPay + (BasicPay*.10) if Job == "analyst" else 0

#printing the output
print(f"{EmployeeID}, {Name}, {totalpay}")
