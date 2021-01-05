from helpers.constants import ZOHO_AUTH_HEADER, ZOHO_AUTH_TOKEN_HEADER_PREFIX, ZOHO_ORG_ID_HEADER, ZOHO_ORG_ID, ZOHO_SUBSCRIPTION_API_URL

import requests

class Zohosubs:
    def __init__(self, config):
        self.config = config

    def list_subs(self):
        headers = {
            ZOHO_AUTH_HEADER : ZOHO_AUTH_TOKEN_HEADER_PREFIX +' '+ self.config['access_token'],
            ZOHO_ORG_ID_HEADER : ZOHO_ORG_ID
        }
        subs = requests.get(ZOHO_SUBSCRIPTION_API_URL+'subscriptions?filter_by=SubscriptionStatus.ACTIVE', headers=headers)
        return subs

    def subs_by_id(self):
        headers = {
            ZOHO_AUTH_HEADER : ZOHO_AUTH_TOKEN_HEADER_PREFIX +' '+ self.config['access_token'],
            ZOHO_ORG_ID_HEADER : ZOHO_ORG_ID
        }
        subs = requests.get(ZOHO_SUBSCRIPTION_API_URL+'subscriptions/{subsciptionid}', headers=headers)
        return subs