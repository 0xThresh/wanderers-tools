import requests
import json
import numpy as np
import classes.CallOpenseaAPI

class CheckFloor:
    '''
    This class includes methods that take an asset JSON block to determine the floor price of a specific attribute.
    The output is currently to a terminal window, but could be easily modified to drop the data into a CSV.
    It could later be modified to combine attributes (such as searching for the floor for Wanderers that have a
    combination of traits).
    '''
    def __init__(self):
        self.floor = np.array([])


    def check_floor(self, assets):
        for asset in assets:
            current_price = asset["sell_orders"]#[0]["current_price"]
            #print(current_price)

            if asset["sell_orders"] is None:
                pass

            elif "." in current_price[0]["current_price"]:
                current_price = int(float(current_price))
                current_price = current_price / 1000000000000000000
                self.floor = np.insert(self.floor, [0], current_price)

            else:
                current_price = int(current_price[0]["current_price"])
                current_price = current_price / 1000000000000000000
                self.floor = np.insert(self.floor, [0], current_price)

        self.floor = np.amin(self.floor)
