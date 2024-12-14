import requests

def verifyAPI(api):
    """
    
    self explanatory
    
    """

    try:
        requests.get(api)
        return True
    except:
        return False