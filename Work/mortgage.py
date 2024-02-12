# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0


extra_payment_start_month = 0
extra_payment_end_month = 12
extra_payment = 1000

month = 0
count = extra_payment_start_month

while principal - payment > 0:
    while extra_payment_start_month - 1 < count < extra_payment_end_month:
        principal = principal * (1+rate/12) - payment - extra_payment
        total_paid = total_paid + payment + extra_payment
        count = count + 1
        month = month + 1
        print(month, total_paid, principal)

    payment = 2684.11
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    month = month + 1
    print(f'In the {month} the amount of {total_paid:0.2f} was paid, remianing is {principal:0.2f}')

print('Total paid', total_paid)
