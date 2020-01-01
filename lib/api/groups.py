# Project: Roblox.py
# File: assets.py
# 
# By: Accutrix
# Do not redistribute without proper credit

from .http import Http
from .users import User


class Group:

    name = None
    id = None
    owner = None
    emblemUrl = None
    description = None
    roles = None
    type = "Group"

    def getAllies(self):
        allies = []
        for ally in Http.format(Http.sendRequest("https://api.roblox.com/groups/" + str(self.id) + "allies")).Groups:
            allies.append(Group(ally))
        return allies

    def getEnemies(self):
        enemies = []
        for enemy in Http.format(Http.sendRequest("https://api.roblox.com/groups/" + str(self.id) + "enemies")).Groups:
            enemies.append(Group(enemy))
        return enemies

    def __init__(self, groupId):
        data = Http.format(Http.sendRequest("https://api.roblox.com/groups/" + str(groupId)))
        self.name = data["Name"]
        self.id = data["Id"]
        self.owner = User(data["Owner"]["Id"])
        self.emblemUrl = data["EmblemUrl"]
        self.description = data["Description"]
        self.roles = data["Roles"]


class UserGroupStatus(Group):

    rank = 0
    role = None
    isInClan = False
    isPrimary = False

    def __init__(self, userId, groupId):
        data = Http.format(Http.sendRequest("http://api.roblox.com/users/" + str(userId) + "/groups"))
        for group in data:
            if group.id == groupId:
                self.name = data["Name"]
                self.id = data["Id"]
                self.owner = User(data["Owner"]["Id"])
                self.emblemUrl = data["EmblemUrl"]
                self.description = data["Description"]
                self.roles = data["Roles"]
                self.rank = data["Rank"]
                self.role = data["Role"]
                self.isInClan = data["IsInClan"]
                self.isPrimary = data["IsPrimary"]


class Groups:

    def getGroup(self, groupId):
        return Group(groupId)
