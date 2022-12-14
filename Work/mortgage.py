# mortgage.py
#
# Exercise 1.7 to 1.11
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_amt = 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108
months = 0

while principal > 0:
    if months >= extra_payment_start_month and months <= extra_payment_end_month:
        principal = principal * (1 + rate / 12) - payment - extra_payment_amt
        total_paid += payment + extra_payment_amt
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid += payment
    months += 1

    if principal < 0:
        principal -= principal  # Clear overpayment

    # print(months, round(total_paid, 2), round(principal, 2))
    print(f'{months} {total_paid:0.2f} {principal:0.2f}')

# print('Total paid', round(total_paid, 2))
# print('Months required', months)
print(f'Total payment of {total_paid:0.2f} across {months} months')
