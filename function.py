def calculate_total(exp):
    total=0
    for item in exp:
        total=total+item
    return total

tom_exp=[1000,452,3645,4626]
joe_exp=[654,56462,6446,6566]

tom_total=calculate_total(tom_exp)
joe_total=calculate_total(joe_exp)

print("tom's total expenditure=",tom_total)
print("joe's total expendtiture=",joe_total)
