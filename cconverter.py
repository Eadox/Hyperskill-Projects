from requests import get

currency_had = input()

pull = get(f"http://www.floatrates.com/daily/{currency_had}.json").json()

if currency_had == 'usd':
    rates = {'eur': float(pull['eur']['rate'])}
elif currency_had == 'eur':
    rates = {'usd': float(pull['usd']['rate'])}
else:
    rates = {'usd': float(pull['usd']['rate']),
             'eur': float(pull['eur']['rate'])}

while True:
    currency_want = input()
    if not currency_want:
        break
    currency_amount = float(input())

    print("Checking the cache...")
    if currency_want in rates:
        print("Oh! It is in the cache!")
        print(f"You received {round(currency_amount * rates[currency_want], 2)} {currency_want.upper()}.")
    else:
        rates[currency_want] = float(pull[currency_want]['rate'])
        print("Sorry, but it is not in the cache!")
        print(f"You received {round(currency_amount * rates[currency_want], 2)} {currency_want.upper()}.")