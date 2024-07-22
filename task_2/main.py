import re
from decimal import Decimal

def generator_numbers(text: str):
    numbers = re.findall(r"\b\d+\.\d+\b", text)

    for number in numbers:
        yield Decimal(number)

def sum_profit(text: str, func: callable):
    numbers_sum = 0

    # or just use sum(), wasn't mentioned before on lectures or I just missed this..
    for num in func(text):
        numbers_sum += num

    return numbers_sum

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід,\
        доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)

print(f"Total: {total_income}")
