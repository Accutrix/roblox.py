# Project: Roblox.py
# File: assets.py
# 
# By: Accutrix
# Do not redistribute without proper credit

from .http import Http
from .users import User


class GroupRole:

    name = None
    rank = None
    type = "GroupRole"
    
    def __init__(self, role):
        self.name = role.Name
        self.rank = role.Rank


class GroupPost:
    
    id = None
    user = None
    role = None
    body = None
    created = None
    updated = None
    type = "GroupPost"

    def __init__(self, data):
        self.id = data["id"]
        self.user = User(data["user"]["userId"])
        self.role = GroupRole(data["role"])
        self.body = data["body"]
        self.created = data["created"]
        self.updated = data["updated"]


class Group:

    name = None
    id = None
    owner = None
    emblemUrl = None
    description = None
    roles = []
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

    def getPosts(self, sortOrder, limit):
        posts = []
        for post in Http.format(Http.sendRequest("https://groups.roblox.com/v2/groups/" + self.id + "/wall/posts?sortOrder=" + sortOrder or "asc" + "&limit=" + str(limit or 100))):
            posts.append(GroupPost(post))
        return posts

    def __init__(self, groupId):
        data = Http.format(Http.sendRequest("https://api.roblox.com/groups/" + str(groupId)))
        self.name = data["Name"]
        self.id = data["Id"]
        self.owner = User(data["Owner"]["Id"])
        self.emblemUrl = data["EmblemUrl"]
        self.description = data["Description"]
        for role in data["Roles"]:
            self.roles.append(GroupRole(role))


class UserGroupStatus:

    id = None
    role = None
    isInClan = False
    isPrimary = False

    def __init__(self, userId, groupId):
        data = Http.format(Http.sendRequest("http://api.roblox.com/users/" + str(userId) + "/groups"))
        for group in data:
            if group.id == groupId:
                self.id = groupId
                self.role = GroupRole(data["Role"])
                self.isInClan = data["IsInClan"]
                self.isPrimary = data["IsPrimary"]


class Groups:

    def getGroup(self, groupId):
        return Group(groupId)
