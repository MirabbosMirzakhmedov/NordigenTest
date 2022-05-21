import requests

from config import (
    base_url,
    account_id,
    from_date,
    end_date,
    payload_transaction
)

res = requests.post(
    url='https://ims.icagruppen.se/oauth/v2/token',
    headers={
        'Content-Type': 'application/x-www-form-urlencoded'
    },
    data=payload_transaction
)

url_transaction: str = f'{base_url}/{account_id}/transactions?status=booked&from={from_date}&to={end_date}'

res_transaction = requests.get(
    url=url_transaction,
    headers={
        'accept': 'application/json',
        'Authorization': f'Bearer {res.json()["access_token"]}'
    },
)

print(res_transaction.status_code)
print(res.json()["access_token"])