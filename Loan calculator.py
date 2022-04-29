import argparse
import math


parser = argparse.ArgumentParser()
parser.add_argument("--type", help="type of loan")
parser.add_argument("--principal", help="amount of money")
parser.add_argument("--periods", help="number of months to repay the loan")
parser.add_argument("--interest", help="bank interest")
parser.add_argument("--payment", help="amount of monthly payment")
args = parser.parse_args()


def calculate_diff_payment(principal, periods, interest):
    convert_rate_num = 12 * 100
    i = interest / convert_rate_num
    overpayment = -principal
    for m in range(periods):
        diff_payment = math.ceil(principal / periods + i * (principal - (principal * m / periods)))
        print(f'Month {m + 1}: payment is {diff_payment}')
        overpayment += diff_payment
    print('\n'
          f'Overpayment = {int(overpayment)}')


def diff_args_checker(principal, periods, interest):
    if not principal or not periods or not interest:
        print('Incorrect parameters.')
        return False
    elif args.payment:
        print('Incorrect parameters.')
        return False
    else:
        return True


def annuity_args_checker(principal, periods, interest, payment):
    check_arg_list = [principal, periods, interest, payment]
    arg_control_sum = 3
    arg_sum = 0
    for arg in check_arg_list:
        if arg:
            arg_sum += 1
    if arg_sum != arg_control_sum:
        print('Incorrect parameters.')
        return False
    else:
        return True


def annuity_calculation_type(principal, periods, payment, interest_rate):
    if not principal:
        calculate_loan_principal(float(payment), float(periods), float(interest_rate))
    elif not periods:
        calculate_number_payments(float(principal), float(payment), float(interest_rate))
    elif not payment:
        calculate_payment_amount(float(principal), float(periods), float(interest_rate))


def calculate_number_payments(principal, month_payment, interest_rate):
    convert_rate_num = 12 * 100
    i = interest_rate / convert_rate_num
    log_base = 1 + i
    num_of_month = math.ceil(math.log((month_payment / (month_payment - i * principal)), log_base))
    years = ''
    months = ''
    union = ''
    if num_of_month // 12 >= 1:
        if num_of_month // 12 == 1:
            years = '1 year'
        else:
            years = str(num_of_month // 12) + ' years'
    if num_of_month % 12 >= 1:
        if num_of_month % 12 == 1:
            months = '1 month'
        else:
            months = str(num_of_month % 12) + ' months'
    if num_of_month // 12 >= 1 and num_of_month % 12 >= 1:
        union = ' and '
    overpayment = month_payment * num_of_month - principal
    print(f'It will take {years}{union}{months} to repay this loan!')
    print(f'Overpayment = {overpayment}')


def calculate_payment_amount(principal, num_of_month, interest_rate):
    convert_rate_num = 12 * 100
    i = interest_rate / convert_rate_num
    i_1_n = pow((i + 1), num_of_month)
    month_payment = math.ceil(principal * i * i_1_n / (i_1_n - 1))
    overpayment = month_payment * num_of_month - principal
    print(f'Your monthly payment = {month_payment}!')
    print(f'Overpayment = {overpayment}')


def calculate_loan_principal(month_payment, num_of_month, interest_rate):
    convert_rate_num = 12 * 100
    i = interest_rate / convert_rate_num
    i_1_n = pow((i + 1), num_of_month)
    principal = month_payment / ((i * i_1_n) / (i_1_n - 1))
    overpayment = month_payment * num_of_month - principal
    print(f'Your loan principal = {principal}!')
    print(f'Overpayment = {overpayment}')


if args.type not in ("diff", "annuity"):
    print("Incorrect parameters")
elif args.type == 'diff':
    if diff_args_checker(args.principal, args.periods, args.interest):
        calculate_diff_payment(float(args.principal), int(args.periods), float(args.interest))
else:
    if annuity_args_checker(args.principal, args.periods, args.interest, args.payment):
        annuity_calculation_type(args.principal, args.periods, args.payment, args.interest)
        