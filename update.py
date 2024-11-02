import requests
import re
import os


class Patch():
    def __init__(self):
        self.url = os.getenv("URL")
        self.new = ""
        self.current = ""

    def GetPatchVersionWeb(self):
        response = requests.get(self.url)
        response.raise_for_status()
        temp = response.text
        return self.GetVersionNumber(temp)

    def GetCurrentPatchVersion(self):
        with open('PatchVersionInfo.cfg', 'r') as file:
            temp = file.read()
        return self.GetVersionNumber(temp)

    def UpdatePatchVersion(self, version):
        with open('PatchVersionInfo.cfg', 'w') as file:
            file.write(f'version {version}')

    def GetVersionNumber(self, text):
        match = re.search(r'\d+', text)
        if match:
            return match.group()
        else:
            return None
import requests
import re
import os


class Patch():
    def __init__(self):
        self.url = os.getenv("URL")
        self.new = ""
        self.current = ""

    def GetPatchVersionWeb(self):
        response = requests.get(self.url)
        response.raise_for_status()
        temp = response.text
        return self.GetVersionNumber(temp)

    def GetCurrentPatchVersion(self):
        with open('PatchVersionInfo.cfg', 'r') as file:
            temp = file.read()
        return self.GetVersionNumber(temp)

    def UpdatePatchVersion(self, version):
        with open('PatchVersionInfo.cfg', 'w') as file:
            file.write(f'version {version}')

    def GetVersionNumber(self, text):
        match = re.search(r'\d+', text)
        if match:
            return match.group()
        else:
            return None
