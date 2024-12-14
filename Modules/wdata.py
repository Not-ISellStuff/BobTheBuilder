import json

def writeTEMPLATE(template):
    with open("Files/template.json", "r") as f:
        data = json.load(f)

    data['template'] = template

    with open("Files/template.json", "w") as f:
        json.dump(data, f, indent=4)

def BASICwritedata(api, good_m, bad_m, user_field, pass_field, name):
    with open("Files/checker.json", "r") as f:
        data = json.load(f)

    data['api-1'] = api
    data['good-1'] = good_m
    data['bad-1'] = bad_m
    data['user-field'] = user_field
    data['password-field'] = pass_field
    data['name'] = name

    with open("Files/checker.json", "w") as f:
        json.dump(data, f, indent=4)