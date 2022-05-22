import typing

import requests


class IcabankenAPI:
    base_url: str = 'https://apimgw-icabanken.ica.se/t/icabanken.tenant' \
                    '/ica/bank/services/psd2/accounts/sandbox/1.0.0/Accounts'

    def _gen_headers(self, access_token: str):
        return {
            'accept': 'application/json',
            'Authorization': f'Bearer {access_token}'
        }

    def get_access_token(
            self,
            payload: typing.Dict[str, str]
    ) -> requests.Response:
        return requests.post(
            url='https://ims.icagruppen.se/oauth/v2/token',
            headers={
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            data=payload
        )

    def get_transactions(
            self,
            access_token: str,
            account_id: int,
            from_date: str,
            end_date: str,
    ) -> requests.Response:
        return requests.get(
            url=f'{self.base_url}/{account_id}'
                f'/transactions'
                f'?status=booked'
                f'&from={from_date}'
                f'&to={end_date}',
            headers=self._gen_headers(
                access_token=access_token
            ),
        )

    def get_transaction_id(
            self,
            access_token,
            account_id: int,
            transaction_id: str

    ) -> requests.Response:
        return requests.get(
            url=f'{self.base_url}/{account_id}'
                f'/transactions'
                f'/{transaction_id}',
            headers=self._gen_headers(
                access_token=access_token
            )
        )

    def get_transactions_paginated(
            self,
            access_token,
            account_id: int,
            from_date: str,
            end_date: str

    ) -> requests.Response:
        return requests.get(
            url=f'{self.base_url}/{account_id}'
                f'/transactions'
                f'?status=booked'
                f'&from={from_date}&to={end_date}',
            headers=self._gen_headers(
                access_token=access_token
            )
        )
