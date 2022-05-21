import requests

from config import (
    base_url,
    account_id,
    transaction_ids,
    res_paginated_id
)


url_transaction_id: str = f'{base_url}/{account_id}/transactions/{transaction_ids[0]}'

res_transaction_id = requests.get(
    url=url_transaction_id,
    headers={
        'accept': 'application/json',
        'Authorization': f'Bearer {res_paginated_id.json()["access_token"]}'
    },
)
