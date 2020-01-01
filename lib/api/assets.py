# Project: Roblox.py
# File: assets.py
# 
# By: Accutrix
# Do not redistribute without proper credit

from .http import Http
from .users import User
from .groups import Group
import json


class AssetVersion:

    id = None
    assetId = None
    versionNumber = None
    creatorType = None
    creatorTargetId = None
    creatingUinverseId = None
    created = None
    updated = None
    type = "AssetVersion"


class Asset:
    
    name = None
    id = None
    productId = None
    description = None
    assetTypeId = None
    creator = None
    #creatorName = None
    #creatorId = None
    creatorType = None
    #creatorTargetId = None
    iconImageAssetId = None
    created = None
    updated = None
    priceInRobux = None
    sales = None
    isNew = None
    isForSale = None
    isPublicDomain = None
    isLimited = None
    isLimitedUnique = None
    remaining = None
    minimumMembershipLevel = None
    contentRatingTypeId = None
    type = "Asset"

    def getOwners(self, sortOrder, limit):
        owners = []
        data = Http.format(Http.sendRequest("https://inventory.roblox.com/v2/assets/" + self.id + "/owners?sortOrder=" + sortOrder or "asc" + "&limit=" + str(limit or 100))).data
        for dataElement in data:
            if dataElement.owner:
                owners.append(User(dataElement.owner.id))
        return owners

    def __init__(self, assetId):
        data = Http.format(Http.sendRequest("https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(assetId)))
        self.name = data["Name"]
        self.id = data["AssetId"]
        self.productId = data["ProductId"]
        self.description = data["Description"]
        self.assetTypeId = data["AssetTypeId"]
        #self.creatorName = data["Creator"]["Name"]
        #self.creatorId = data["Creator"]["Id"]
        self.creatorType = data["Creator"]["CreatorType"]
        #self.creatorTargetId = data["Creator"]["CreatorTargetId"]
        self.iconImageAssetId = data["IconImageAssetId"]
        self.created = data["Created"]
        self.updated = data["Updated"]
        self.priceInRobux = data["PriceInRobux"]
        self.sales = data["Sales"]
        self.isNew = data["IsNew"]
        self.isForSale = data["IsForSale"]
        self.isPublicDomain = data["IsPublicDomain"]
        self.isLimited = data["IsLimited"]
        self.isLimitedUnique = data["IsLimitedUnique"]
        self.remaining = data["Remaining"]
        self.minimumMembershipLevel = data["MinimumMembershipLevel"]
        self.contentRatingTypeId = data["ContentRatingTypeId"]
        if self.creatorType == "Group":
            self.creator = Group(data["Creator"]["Id"])
        else:
            self.creator = User(data["Creator"]["Id"])


class Assets:

    def getAsset(self, assetId):
        return Asset(assetId)
