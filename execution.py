import typing

import requests

from config import Settings
from icabanken import IcabankenAPI

api = IcabankenAPI()

res_token = api.get_access_token(
    payload={
        'grant_type': 'client_credentials',
        'client_id': Settings.client_id,
        'client_secret': Settings.client_secret,
        'scope': f'psd2_sandbox:195505063676'
    }
)
res_data: typing.Dict = res_token.json()
access_token: str = res_data['access_token']
account_id: int = 12345678910

res_tx: requests.Response = (
    api.get_transactions(
        access_token=access_token,
        account_id=account_id,
        from_date='01.01.2022',
        end_date='01.05.2022'
    )
)

res_tx_id: requests.Response = (
    api.get_transaction_id(
        access_token=access_token,
        account_id=account_id,
        transaction_id='00000003116265606'
    )
)

res_tx_page: requests.Response = (
    api.get_transactions_paginated(
        access_token=access_token,
        account_id=account_id,
        from_date='01.01.2022',
        end_date='01.05.2022'
    )
)

print(res_tx)
print(res_tx_id)
print(res_tx_page)
