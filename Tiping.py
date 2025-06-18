def total_calc(bill_amount, tip_perc):
    total=bill_amount*(1+0.01*tip_perc)
    total=round(total, 2)
    print(f"Please pay ${total}")
bill_amount=int(input("Enter The Amount Of Your Bill: "))
tip=int(input("Please Enter The Amount of tip Percentage: "))

total_calc(bill_amount, tip)