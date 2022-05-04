import requests
import json

class TraitIDs:
    '''
    This class includes methods to gather all of the metadata from all 8,888 of The Wanderers, and to evaluate
    which Wanderers include rare traits. The rare traits can be printed to a terminal screen, or used to evaluate
    the current floors of any attributes.
    '''
    def __init__(self):
        ### All Wanderers object
        self.all_wanderers = []

        ### All traits
        # Planets
        self.destroyed_planet_ids = []
        self.eden_ids = []
        self.anger_orb_ids = []

        # Number of traits
        self.traits_16_ids = []
        self.traits_15_ids = []
        self.traits_14_ids = []

        # Panels
        self.bounty_ids = []
        self.crypto_ids = []
        self.no_panel_ids = []
        self.five_panel_ids = []

        # Hands
        self.joint_ids = []
        self.eth_hand_ids = []
        self.skull_ids = []
        self.jar_shrooms_ids = []
        self.jar_eyes_ids = []
        self.porn_ids = []
        self.alien_joint_ids = []
        self.hot_dog_ids = []
        self.robo_charge_ids = []
        self.left_bong_ids = []
        self.bong_glitch_ids = []
        self.wine_glitch_ids = []

        # Cockpits
        self.cat_ids = []

        # Specials
        self.guardian_marked_ids = []
        self.radioactive_ids = []
        self.ws16_ids = []

        # Anamolies
        self.monolith_ids = []

    ### Identify traits methods
    def anger_orb(self, traits, token_id):
        for trait in traits:
            if trait["trait_type"] == "Planet":
                if trait["value"] == "Anger Orb":
                    self.anger_orb_ids.append(token_id)

    def eden(self, traits, token_id):
        for trait in traits:
            if trait["trait_type"] == "Planet":
                if trait["value"] == "Eden Planet":
                    self.eden_ids.append(token_id)

    def destroyed_planet(self, traits, token_id):
        for trait in traits:
            if trait["trait_type"] == "Planet":
                if trait["value"] == "Destroyed Planet":
                    self.destroyed_planet_ids.append(token_id)

    def traits_16(self, traits, token_id):
        if len(traits) == 16:
            self.traits_16_ids.append(token_id)

    def traits_15(self, traits, token_id):
        if len(traits) == 15:
            self.traits_15_ids.append(token_id)

    def traits_14(self, traits, token_id):
        if len(traits) == 14:
            self.traits_14_ids.append(token_id)

    def bounty(self, traits, token_id):
        for trait in traits:
            if trait["trait_type"] == "Panel 1" or trait["trait_type"] == "Panel 2" or trait["trait_type"] == "Panel 3" or \
                    trait["trait_type"] == "Panel 4" or trait["trait_type"] == "Panel 5":
                if trait["value"] == "Bounty":
                    self.bounty_ids.append(token_id)

    def crypto(self, traits, token_id):
        for trait in traits:
            if trait["trait_type"] == "Panel 1" or trait["trait_type"] == "Panel 2" or trait["trait_type"] == "Panel 3" or \
                    trait["trait_type"] == "Panel 4" or trait["trait_type"] == "Panel 5":
                if trait["value"] == "Crypto":
                    self.crypto_ids.append(token_id)

    def alien_joint(self, traits, token_id):
        for trait in traits:
            if trait["trait_type"] == "Left Arm" or trait["trait_type"] == "Right Arm":
                if trait["value"] == "Alien Joint":
                    self.alien_joint_ids.append(token_id)

    def joint(self, traits, token_id):
        for trait in traits:
            if trait["trait_type"] == "Left Arm" or trait["trait_type"] == "Right Arm":
                if trait["value"] == "Joint":
                    self.joint_ids.append(token_id)

    def eth_hand(self, traits, token_id):
        for trait in traits:
            if trait["trait_type"] == "Left Arm" or trait["trait_type"] == "Right Arm":
                if trait["value"] == "ETH":
                    self.eth_hand_ids.append(token_id)

    def skull(self, traits, token_id):
        for trait in traits:
            if trait["trait_type"] == "Left Arm" or trait["trait_type"] == "Right Arm":
                if trait["value"] == "Skull":
                    self.skull_ids.append(token_id)

    def jar_shrooms(self, traits, token_id):
        for trait in traits:
            if trait["trait_type"] == "Left Arm" or trait["trait_type"] == "Right Arm":
                if trait["value"] == "Jar Shrooms":
                    self.jar_shrooms_ids.append(token_id)

    def jar_eyes(self, traits, token_id):
        for trait in traits:
            if trait["trait_type"] == "Left Arm" or trait["trait_type"] == "Right Arm":
                if trait["value"] == "Jar Eyes":
                    self.jar_eyes_ids.append(token_id)

    def porn(self, traits, token_id):
        for trait in traits:
            if trait["trait_type"] == "Left Arm" or trait["trait_type"] == "Right Arm":
                if trait["value"] == "Porn":
                    self.porn_ids.append(token_id)

    def hot_dog(self, traits, token_id):
        for trait in traits:
            if trait["trait_type"] == "Left Arm" or trait["trait_type"] == "Right Arm":
                if trait["value"] == "Hotdog":
                    self.hot_dog_ids.append(token_id)

    def robo_charge(self, traits, token_id):
        for trait in traits:
            if trait["trait_type"] == "Left Arm" or trait["trait_type"] == "Right Arm":
                if trait["value"] == "Robo Charge":
                    self.robo_charge_ids.append(token_id)

    def left_bong(self, traits, token_id):
        for trait in traits:
            if trait["trait_type"] == "Left Arm":
                if trait["value"] == "Bong":
                    self.left_bong_ids.append(token_id)

    def bong_glitch(self, traits, token_id):
        for trait in traits:
            if trait["trait_type"] == "Right Arm":
                if trait["value"] == "Bong":
                    self.bong_glitch_ids.append(token_id)

    def wine_glitch(self, traits, token_id):
        for trait in traits:
            if trait["trait_type"] == "Right Arm":
                if trait["value"] == "Wine":
                    self.wine_glitch_ids.append(token_id)

    def monolith(self, traits, token_id):
        for trait in traits:
            if trait["trait_type"] == "Anomaly":
                if trait["value"] == "Monolith":
                    self.monolith_ids.append(token_id)

    def cat(self, traits, token_id):
        for trait in traits:
            if trait["trait_type"] == "Cockpit":
                if trait["value"] == "Cat":
                    self.cat_ids.append(token_id)

    def radioactive(self, traits, token_id):
        for trait in traits:
            if trait["trait_type"] == "special":
                if trait["value"] == "RADIOACTIVE":
                    self.radioactive_ids.append(token_id)

    def guardian_marked(self, traits, token_id):
        for trait in traits:
            if trait["trait_type"] == "special":
                if trait["value"] == "Guardian Marked":
                    self.guardian_marked_ids.append(token_id)

    def ws16(self, traits, token_id):
        for trait in traits:
            if trait["trait_type"] == "special":
                if trait["value"] == "Warp Squad Sixteen":
                    self.ws16_ids.append(token_id)

    def no_panels(self, traits, token_id):
        dump = json.dumps(traits)
        if "Panel" not in dump:
            self.no_panel_ids.append(token_id)

    def five_panels(self, traits, token_id):
        dump = json.dumps(traits)
        count = dump.count("Panel")
        if count == 5:
            self.five_panel_ids.append(token_id)

    def print_ids(self):
        # Planets
        print("Destroyed Planets: ")
        print(self.destroyed_planet_ids)

        print("Eden Planets: ")
        print(self.eden_ids)

        print("Anger Orbs: ")
        print(self.anger_orb_ids)

        # Number of traits
        print(" 16 Traits: ")
        print(self.traits_16_ids)

        print("15 Traits: ")
        print(self.traits_15_ids)

        print("14 Traits: ")
        print(self.traits_14_ids)

        # Panels
        print("Bounty Panels: ")
        print(self.bounty_ids)

        print("Crypto Panels:")
        print(self.crypto_ids)

        print("No Panels:")
        print(self.no_panel_ids)

        print("Five Panels:")
        print(self.five_panel_ids)

        # Hands
        print("Joints:")
        print(self.joint_ids)

        print("ETH Hands:")
        print(self.eth_hand_ids)

        print("Skulls:")
        print(self.skull_ids)

        print("Jar Shrooms:")
        print(self.jar_shrooms_ids)

        print("Jar Eyes:")
        print(self.jar_eyes_ids)

        print("Porn:")
        print(self.porn_ids)

        print("Alien Joint:")
        print(self.alien_joint_ids)

        print("Hot Dog:")
        print(self.hot_dog_ids)

        print("Robo Charge:")
        print(self.robo_charge_ids)

        print("Left Bong:")
        print(self.left_bong_ids)

        print("Bong Glitch:")
        print(self.bong_glitch_ids)

        print("Wine Glitch:")
        print(self.wine_glitch_ids)

        # Cockpits
        print("Cat Cockpit:")
        print(self.cat_ids)

        # Specials
        print("Guardian Marked:")
        print(self.guardian_marked_ids)

        print("Radioactive:")
        print(self.radioactive_ids)

        print("Warp Squad Sixteen:")
        print(self.ws16_ids)

        # Anomalies
        print("Monolith:")
        print(self.monolith_ids)
        