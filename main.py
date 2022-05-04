'''
next steps:
- figure out best way to run all attribute classes against all 8888 objects
'''
from classes.TraitIDs import TraitIDs
from classes.CheckFloor import CheckFloor
from classes.CallOpenseaAPI import CallOpenseaAPI
import ast
import json
import numpy as np

# Main block
# instantiate classes
IDs = TraitIDs()
Floor = CheckFloor()
API = CallOpenseaAPI()

# Open file with metadata for every Wanderer - could be a method of checkfloor class
with open('./all_wanderers.txt', 'r') as read_file:
    data = read_file.read()

wanderers_json = ast.literal_eval(data)
print(type(wanderers_json))
print(wanderers_json[0])

# Begin gathering IDs for each trait
for wanderer in wanderers_json:

    try:
        # Gather required vars
        traits = wanderer["traits"]
        token_id = wanderer["token_id"]

        # Planets
        IDs.anger_orb(traits, token_id)
        '''        
        IDs.eden(traits, token_id)
        IDs.destroyed_planet(traits, token_id)

        # Trait counts
        IDs.traits_16(traits, token_id)
        IDs.traits_15(traits, token_id)
        IDs.traits_14(traits, token_id)

        # Panels
        IDs.bounty(traits, token_id)
        IDs.crypto(traits, token_id)
        IDs.no_panels(traits, token_id)
        IDs.five_panels(traits,token_id)

        # Hands
        IDs.joint(traits, token_id)
        IDs.eth_hand(traits, token_id)
        IDs.skull(traits, token_id)
        IDs.jar_shrooms(traits, token_id)
        IDs.jar_eyes(traits, token_id)
        IDs.porn(traits, token_id)
        IDs.alien_joint(traits, token_id)
        IDs.hot_dog(traits, token_id)
        IDs.robo_charge(traits, token_id)
        IDs.left_bong(traits, token_id)
        IDs.bong_glitch(traits, token_id)
        IDs.wine_glitch(traits, token_id)

        # Cockpits
        IDs.cat(traits, token_id)

        # Specials
        IDs.guardian_marked(traits, token_id)
        IDs.radioactive(traits, token_id)
        IDs.ws16(traits, token_id)

        # Anomalies
        IDs.monolith(traits, token_id)
        '''

    except KeyError:
        print("failed Opensea API call; skipping")

# Gather sales data
print("Gathering Wanderers data for selected trait")
API.gather_wanderers_floor(IDs.anger_orb_ids)  # this is missing an input to determine which trait to check
print("Gathered successfully")

# Evaluate and return the floor price
Floor.check_floor(API.assets)

attribute = "Anger Orb" # using anger orb to test since <50 IDs
print(f"{attribute} attribute's floor: ") # attribute will eventually come from input
print(Floor.floor)
