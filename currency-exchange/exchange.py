"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate): 
    return budget / exchange_rate

def get_change(budget, exchanging_value):
    return (budget - exchanging_value)

def get_value_of_bills(denomination, number_of_bills):
    return int(denomination * number_of_bills)

def get_number_of_bills(amount, denomination):
    return int(amount / denomination)

def get_leftover_of_bills(amount, denomination):
    return (amount % denomination)

def exchangeable_value(budget, exchange_rate, spread, denomination):
    total_exchange_rate = exchange_rate + (exchange_rate * (spread / 100))
    value_after_exchange = exchange_money(budget,total_exchange_rate)
    #print('value_after_exchange', value_after_exchange)
    number_of_bills = get_number_of_bills(value_after_exchange,denomination)
    #print('number_of_bills', number_of_bills)
    return get_value_of_bills(denomination,number_of_bills)