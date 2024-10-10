import requests
import json

base_url = 'https://v6.exchangerate-api.com/v6'
api_key = '6ceb5bfa119bc577c39f2792'
latest = 'latest/USD'
pair_con = 'pair'
currency_1 = input('Input base currency (e.g., USD): ')
currency_2 = input('Input target currency (e.g., EUR): ')
amount = input('How much do you want to convert (default is 1): ')
if not amount:
    amount = 1

main_url = base_url + '/' + api_key + '/' + pair_con + '/' + currency_1 + '/' + currency_2 + '/' + amount
print(main_url)

response_1 = requests.get(main_url)

if response_1.status_code == 200:
    response_2 = response_1.json()
    print(json.dumps(response_2, indent=5))

    if response_2["result"] == "success":
        conversion_rate = response_2["conversion_rate"]
        converted_amount = response_2["conversion_result"]
        print(f"{amount} {currency_1} is equal to {converted_amount:.2f} {currency_2}.")
    else:
        print("Conversion could not be performed. Please check the currency codes.")
else:
    print(f"Error: {response_1.status_code} - {response_1.text}")
