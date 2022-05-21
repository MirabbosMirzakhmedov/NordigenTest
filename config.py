from typing import List, Dict

import requests

base_url: str = "https://apimgw-icabanken.ica.se/t/icabanken.tenant/ica/bank/services/psd2/accounts/sandbox/1.0.0/Accounts"
client_id: str = 'BY4Al1LkdkF18awpuImB1uZtli0a'
client_secret: str = '_YliZ2vpxXfwrXVJjHyTvSFfRXMa'
account_id: str = '12345678910'
from_date: str = '01.01.2022'
end_date: str = '01.03.2022'

transaction_ssn_nums: List = [
    '195505063676',
    '197301175209',
    '196311210063',
    '198904153866',
    '201011119789',
    '198312112678'
]

paginated_id_ssn_nums: List = [
    '195505063676',
    '197301175209',
    '196311210063',
    '198904153866',
    '194112010014',
    '197002022692',
    '201011119789',
    '198312112678'
]

payload_transaction: Dict = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': f'psd2_sandbox:{transaction_ssn_nums[0]}'
}

payload_paginated_id: Dict = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': f'psd2_sandbox:{paginated_id_ssn_nums[0]}'
}

transaction_ids: List = [
    '00000003116265606',
    '00000003114459127',
    '00000003116364886',
    '00000003116116872',
    '00000003116262615',
    '00000003109932323'
]

res_paginated_id = requests.post(
    url='https://ims.icagruppen.se/oauth/v2/token',
    headers={
        'Content-Type': 'application/x-www-form-urlencoded'
    },
    data=paginated_id_ssn_nums[0]
)
