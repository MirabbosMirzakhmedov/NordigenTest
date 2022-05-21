import requests

from config import (
    base_url,
    account_id,
    from_date,
    end_date,
    res_paginated_id
)

url_transaction: str = f'{base_url}/{account_id}/transactions?status=booked&from={from_date}&to={end_date}'

res_transaction = requests.get(
    url=url_transaction,
    headers={
        'accept': 'application/json',
        'Authorization': f'Bearer {res_paginated_id.json()["access_token"]}'
    },
)
