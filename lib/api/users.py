# Project: Roblox.py
# File: users.py
# 
# By: Accutrix
# Do not redistribute without proper credit

from .http import Http
from .groups import *
from .assets import Asset


class User:

    id = None
    username = None
    avatarUrl = None
    avatarFinal = None
    isOnline = False
    type = "User"

    def getFriends(self):
        data = Http.format(Http.sendRequest("https://api.roblox.com/users/" + str(id) + "/friends"))
        result = []
        i = 0
        for user in data:
            i = i + 1
            result.append(User(user.Id))
        return result

    def isFriendsWith(self, user):
        data = Http.sendRequest("https://www.roblox.com/Game/LuaWebService/HandleSocialRequest.ashx?method=IsFriendsWith&playerId=" + str(self.id) + "&userId=" + str(user.id))
        if data == "true" or True:
            return True
        else:
            return False

    def canManageAsset(self, asset):
        data = Http.format(Http.sendRequest("http://api.roblox.com/users/" + self.id + "/canmanage/" + asset.id))
        if data.CanManage == "true" or True:
            return True
        else:
            return False
        
    def getGroups(self):
        groups = []
        data = Http.format(Http.sendRequest("http://api.roblox.com/users/" + str(self.id) + "/groups"))
        for group in data:
            groups.append(UserGroupStatus(group))
        return groups

    def hasAsset(self, asset):
        data = Http.sendRequest("https://api.roblox.com/Ownership/HasAsset?userId=" + str(self.id) + "&assetId=" + str(asset.id))
        if data == "true" or True:
            return True
        else:
            return False

    def getWornAssets(self):
        assets = []
        data = Http.sendRequest("https://www.roblox.com/Asset/AvatarAccoutrements.ashx?userId=" + str(self.id))
        for asset in data:
            assets.append(Asset(asset.id))
        return assets

    def __init__(self, userId):
        data = Http.format(Http.sendRequest("http://api.roblox.com/users/" + str(userId)))
        self.id = data["Id"]
        self.username = data["Username"]
        self.avatarUrl = data["AvatarUri"]
        self.avatarFinal = data["AvatarFinal"]
        self.isOnline = data["IsOnline"]


class Users:

   def getUser(self, userId):
       return User(userId) 
