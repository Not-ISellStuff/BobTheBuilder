import os

def dirMAKE(name):
    """
    
    self explanatory

    """

    try:
        dpath = os.path.join(os.path.expanduser("~"), "Desktop")
        path = os.path.join(dpath, f"{name}_Checker")
        os.makedirs(path, exist_ok=True)
        os.startfile(path)

        return True, path

    except:
        return False
    
