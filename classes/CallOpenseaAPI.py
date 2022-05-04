import requests
import json
import numpy as np


class CallOpenseaAPI:
    '''
    This class contains two methods for calling different endpoints on the Opensea API in order to gather asset
    metadata and gather data about listings.
    '''

    def __init__(self):
        self.asset_contract_address = '0x8184a482a5038b124d933b779e0ea6e0fb72f54e'
        self.all_wanderers = []
        self.assets = []

    def gather_all_wanderers(self):
        '''
        Collects metadata for all 8888 of The Wanderers NFTs.
        If you already have the full JSON file, you shouldn't need to run this - takes ~2 hours without concurrency.
        :return massive JSON document with metadata for all Wanderers
        '''
        i = 0
        while i <= 8887:  # Wanderers IDs run from 0-8887, totaling 8888 - this could be variablized for other projects
            # API URL for retrieving assets - trailing number is the ID
            token_id = i
            url = f"https://api.opensea.io/api/v1/asset/{self.asset_contract_address}/{token_id}/"
            response = requests.request("GET", url)
            text = json.loads(response.text)
            self.all_wanderers.append(text)
            i += 1

    def gather_wanderers_floor(self, token_ids):
        '''
        Collects metadata for Wanderers listed for sale. In its current state, it only targets the IDs it's passed
        through an argument. Therefore, there's an assumption that the attribute being targeted has the IDs of all
        matched in another method passed in as an arguemnt.
        :return the lowest price, in ETH, of the Token IDs evaluated, in type int
        '''

        url = "https://api.opensea.io/api/v1/assets"

        if len(token_ids) > 30: # Opensea docs claim you can pass it 50 items, but it gave me an error when IDs > 30

            all_ids = [token_ids[i:i + 30] for i in range(0, len(token_ids), 30)]

            for sublist in all_ids:
                querystring = {"token_ids": sublist, "asset_contract_address": self.asset_contract_address,
                               "order_direction": "desc", "offset": "0", "limit": "30"}

                response = requests.request("GET", url, params=querystring)

                text = response.text
                text = json.loads(text)
                text = text["assets"]
                for item in text:
                    self.assets.append(item)

        elif len(token_ids) <= 30:
            querystring = {"token_ids": token_ids, "asset_contract_address": self.asset_contract_address,
                           "order_direction": "desc", "offset": "0", "limit": "30"}

            response = requests.request("GET", url, params=querystring)

            text = response.text
            text = json.loads(text)
            self.assets = text["assets"]


#ids = ['2', '6', '20', '29', '76', '84', '109', '125', '160', '306', '324', '396', '462', '480', '538', '587', '671', '695', '698', '701', '753', '790', '797', '799', '814', '817', '818', '897', '1032', '1035', '1047', '1048', '1062', '1088', '1127', '1133', '1139', '1159', '1161', '1196', '1278', '1292', '1303', '1338', '1364', '1368', '1370', '1372', '1407', '1416', '1477', '1479', '1676', '1691', '1693', '1729', '1785', '1814', '1821', '1824', '1868', '1871', '1939', '1956', '2123', '2148', '2203', '2268', '2321', '2357', '2398', '2472', '2477', '2494', '2602', '2618', '2675', '2701', '2758', '2831', '2837', '2858', '2878', '2888', '2893', '2992', '3005', '3044', '3052', '3105', '3119', '3144', '3149', '3157', '3188', '3216', '3244', '3256', '3305', '3324', '3345', '3367', '3423', '3455', '3499', '3527', '3533', '3567', '3584', '3597', '3599', '3610', '3824', '3889', '3927', '4001', '4046', '4061', '4075', '4093', '4100', '4122', '4145', '4153', '4197', '4204', '4221', '4293', '4372', '4436', '4512', '4545', '4638', '4689', '4708', '4716', '4774', '4811', '4853', '5031', '5052', '5082', '5090', '5121', '5135', '5229', '5236', '5240', '5261', '5296', '5311', '5378', '5420', '5592', '5671', '5726', '5760', '5840', '5841', '5852', '5860', '5895', '5896', '5914', '5920', '5929', '5952', '5970', '6057', '6062', '6072', '6090', '6120', '6238', '6248', '6291', '6379', '6386', '6427', '6440', '6510', '6519', '6536', '6573', '6601', '6643', '6644', '6651', '6666', '6697', '6711', '6732', '6759', '6922', '6946', '6997', '7008', '7012', '7052', '7056', '7069', '7074', '7091', '7108', '7127', '7152', '7179', '7262', '7327', '7330', '7336', '7433', '7444', '7484', '7538', '7580', '7612', '7636', '7674', '7732', '7733', '7823', '7850', '7894', '8143', '8229', '8232', '8253', '8284', '8303', '8327', '8337', '8360', '8395', '8422', '8453', '8482', '8487', '8492', '8505', '8582', '8595', '8671', '8704', '8735', '8767', '8778', '8792', '8796', '8817', '8825']
#print(len(ids))
#print(ids)
#API = CallOpenseaAPI()
#assets = API.gather_wanderers_floor(ids)
#print(len(API.assets))
#print(type(API.assets))
