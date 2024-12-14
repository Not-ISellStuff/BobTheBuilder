from bob import BobTheBuilder
from Modules.wdata import *

bob = BobTheBuilder()

def build(*data):
    """
    
    self explanatory

    """

    with open("Files/template.json", "r") as f:
        d_ = json.load(f)
        template = d_['template']
    basic = ["Basic | Payload: JSON", "Basic | Payload: URL Format"]

    if template in basic:
        api = data[0]
        good_m = data[1]
        bad_m = data[2]
        user_field = data[3]
        pass_field = data[4]
        name = data[5]

        BASICwritedata(api, good_m, bad_m, user_field, pass_field, name)
        bob.build()

    else:
        return False