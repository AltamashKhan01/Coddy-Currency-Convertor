"""
Follow below link to get started:
https://coddy.tech/courses/currency_converter__python_project/introduction
"""


# Coddy Currency Convertor 1/5
"""
Welcome Page
"""


# Coddy Currency Convertor 2/5
"""
# Hardcoded values, don't change these
CURRENCIES = {
    'USD': 1,
    'EUR': 1.06,
    'YEN': 0.0067,
    'GBP': 1.23,
    'AUD': 0.64,
    'CAD': 0.74
}

# Write code here
def to_usd(cur_code, amt):
    # check if the currency is supported
    if cur_code in CURRENCIES:
        return CURRENCIES[cur_code] * amt
"""


# Coddy Currency Convertor 3/5
"""
CURRENCIES = {
    'USD': 1,
    'EUR': 1.06,
    'YEN': 0.0067,
    'GBP': 1.23,
    'AUD': 0.64,
    'CAD': 0.74
}

# Write code here
def to_usd(cur_code, amt):
    # check if the currency is supported
    if cur_code in CURRENCIES:
        return CURRENCIES[cur_code] * amt
    # print not supported message
    elif cur_code not in CURRENCIES:
        return f"{cur_code} is not supported"
    # print invalid amount message
    elif amt < 0:
        return "Invalid amount"
"""


# Coddy Currency Convertor 4/5
"""
CURRENCIES = {
    'USD': 1,
    'EUR': 1.06,
    'YEN': 0.0067,
    'GBP': 1.23,
    'AUD': 0.64,
    'CAD': 0.74
}

def to_usd(cur_code, amt):
    # check if the currency is supported
    if cur_code in CURRENCIES:
        return CURRENCIES[cur_code] * amt
    # print not supported message
    elif cur_code not in CURRENCIES:
        return f"{cur_code} is not supported"
    # print invalid amount message
    elif amt < 0:
        return "Invalid amount"

# Write code here
def from_usd(cur_code, amt):
    # check if the currency is supported
    if cur_code in CURRENCIES and amt >= 0:
        return round(amt / CURRENCIES[cur_code] , 4)
    # print not supported message
    elif cur_code not in CURRENCIES:
        return f"{cur_code} is not supported"
    # print invalid amount message
    elif amt < 0:
        return 'Invalid amount'
"""


# Coddy Currency Convertor 5/5
"""
CURRENCIES = {
    'USD': 1,
    'EUR': 1.06,
    'YEN': 0.0067,
    'GBP': 1.23,
    'AUD': 0.64,
    'CAD': 0.74
}

def to_usd(cur_code, amt):
    # check if the currency is supported
    if cur_code in CURRENCIES:
        return CURRENCIES[cur_code] * amt
    # raise Exception if not supported
    elif cur_code not in CURRENCIES:
        raise Exception(f"{cur_code} is not supported")
    # raise Exception if invalid amount
    elif amt < 0:
        raise Exception("Invalid amount")

# Write code here
def from_usd(cur_code, amt):
    # check if the currency is supported
    if cur_code in CURRENCIES and amt >= 0:
        return round(amt / CURRENCIES[cur_code] , 4)
    # raise Exception if not supported
    elif cur_code not in CURRENCIES:
        raise Exception(f"{cur_code} is not supported")
    # raise Exception if invalid amount
    elif amt < 0:
        raise Exception("Invalid amount")

def convert(from_currency, amount, to_currency):
    try:
        res = to_usd(from_currency, amount)
        res = from_usd(to_currency, res)
        print(f'{amount} {from_currency} is {res} {to_currency}')
    except Exception as e:
        print(e)
"""



"""
Apart from limited support for currencies and hardcoded values, this project is fun and easy for beginners in python programming. Do try!!!
"""