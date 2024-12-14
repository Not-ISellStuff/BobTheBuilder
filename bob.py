import os
import json
import shutil
from tkinter import messagebox
from Modules.dir import *

class BobTheBuilder:
    def __init__(self):
        """
        
        Hi this lib was made by isellstuff
        Hope you like my cool library!

        (btw im adding comments to this cuz i might make a separate repo for this)
        
        """

    def editVar(self, path, var, value, dt):
        """
        
        Edits the value of a variable
        Supported Types: Str, Int
        
        """

        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if line.strip().startswith(f'{var} ='):
                if dt == "str":
                    lines[i] = f'{var} = "{value}"\n'
                elif dt == "int":
                    lines[i] = f'{var} = "{value}"\n'
                break

        with open(path, 'w', encoding='utf-8') as file:
            file.writelines(lines)

    def editBasicPayload(self, path, var, user_, password_, dt):
        """
        
        Edits a basic payload for a req
        
        """

        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if line.strip().startswith(f'{var} ='):
                if dt == "dict":
                    payload = f"{var} = "
                    payload += "{"
                    payload += f'"{user_}": username, "{password_}": password'
                    payload += "}"
                    lines[i] = f'    {payload}\n'
                else:
                    payload = f'{var} = f"{user_}={{username}}&{password_}={{password}}"'
                    lines[i] = f'    {payload}\n'
                break

        with open(path, 'w', encoding='utf-8') as file:
            file.writelines(lines)

    def data(self):
        with open("Files/checker.json", "r") as f:
            data = json.load(f)

        return data

    def build(self):
        """
        
        Builds Checker

        """

        with open("Files/template.json", "r") as f:
            d_ = json.load(f)
            template = d_['template']

        templates = ["Basic | Payload: JSON", "Basic | Payload: URL Format"]
        basicJSON = templates[0]
        basicURL = templates[1]

        if template not in templates:
            messagebox.showerror(title="Error", message="Invalid Template")
            return

        if template == basicJSON or basicURL:

            data = self.data()
            api = data['api-1']
            good = data['good-1']
            bad = data['bad-1']
            username = data['user-field']
            password = data['password-field']
            name = data['name']

            dir_ = dirMAKE(name)
            if dir_[0] == True:
                messagebox.showinfo(title="Done", message="Created Dir For Checker")
                shutil.copy("Templates/basic.py", str(dir_[1]))
            else:
                messagebox.showerror(title="Error", message="Failed To Create Directory For Checker")
                return

            self.editVar(f"{dir_[1]}\\basic.py", "api", api, "str")
            self.editVar(f"{dir_[1]}\\basic.py", "hit", good, "str")
            self.editVar(f"{dir_[1]}\\basic.py", "bad", bad, "str")
            
            if template == basicJSON:
                self.editBasicPayload(f"{dir_[1]}\\basic.py", "d", username, password, "dict")
            else:
                self.editBasicPayload(f"{dir_[1]}\\basic.py", "d", username, password, "other")

            messagebox.showinfo(title="Done", message="Built Checker. If your checker does not open then you did something wrong or if you know you did nothing wrong let me know, also make sure you drag the file to another folder")