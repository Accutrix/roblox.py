
<img src="https://raw.githubusercontent.com/accutrix/roblox.py/master/art/logo.png" alt="The Python Roblox API Wrapper" />

[![Build Status](https://travis-ci.org/Accutrix/roblox.py.svg?branch=master)](https://travis-ci.org/Accutrix/roblox.py)
![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)
[![ROBLOX API Discord](https://img.shields.io/badge/discord-roblox%20api%20chat-blue.svg)](https://discord.gg/Y5Rkzyb)

## About
Roblox.py is a API wrapper for the Roblox API written in the Python programming language. It was developed in late 2019, and continues to be supported to this day. 


## Modules

#### Assets:
- getAsset(assetId) - gets the asset of the given ID (returns a "Asset" object)

#### Groups:
- getGroup(groupId) - gets the group of the given ID (returns a "Group"  object)

#### Users:
 - getUser(userId) - gets the user of the given ID (returns a "User" object)


## Classes

#### Asset:

##### Properties:
- name - the name of the asset
- id - the AssetId of the asset
- productId - the product ID of the asset
- description - the description of the asset
- assetTypeId
- creator - the creator of the asset
- creatorType - the type of creator of the asset ("User" or "Group")
- iconImageAssetId - the Asset ID for the icon of the asset
- created - the timestamp of creation of the asset
- updated - the timestamp of the last update of the asset
- priceInRobux - the price of robux the asset
- sales - the amount of sales the asset has had
- isNew - whether or not the asset is new
- isForSale - whether or not the asset is for sale
- isPublicDomain
- isLimited - whether or not the asset is Limited
- isLimitedUnique - whether or not the asset is Limited Unique
- remaining - the amount of remaining copies of the asset
- minimumMembershipLevel - the minimum membership level required to purchase the asset
- contentTypeRatingId - the content type rating ID for the asset

##### Methods:
- getOwners(sortOrder, limit) - gets all the owners of the asset within the limit, and in the given sort order "Asc" or "Desc" (returns an array of "User" objects) 

#### Group:

##### Properties:
- name - the name of the group
- id - the ID of the group
- owner - the owner of the group
- emblemUrl - the URL for the emblem of the group
- description - the description of the group
- roles -an array of "GroupRole" objects of the group

##### Methods:
- getAllies() - gets all the allies of the group (returns an array of "Group" objects)
- getEnemies() - gets all the enemies of the group (returns an array of "Group" objects)

#### GroupRole:

##### Properties:
- name - the name of the group role
- rank - the rank of the group role

#### UserGroupStatus:

 ##### Properties:
- id - the ID of the group
- role - the role of the player ("GroupRole" object)
- isInClan - whether or not the user is in the clan
- isPrimary - whether or not the group is the user's primary group

#### User:

##### Properties:
- id - the User ID of the user
- username - the username of the user
- avatarUrl - the url for the avatar of the user
- avatarFinal
- isOnline - whether or not the user is currently online on the platform

##### Methods:
- getFriends() - gets all the friends of the user (returns an array of "User" objects)
- isFriendsWith(user) - gets the friendship status of the user of the object with the given user (returns a bool)
- hasAsset(asset) - checks to see if the user has the asset (returns a bool)
- getGroups() - gets all the groups the player is in (returns an array of "UserGroupStatus" objects)
- getWornAssets() - gets all the assets that is being worn by the user (returns an array of "Asset" objects)

## Examples

#### Finding the amount of limiteds owned by a user
```python
user = Users.getUser(userId) # returns a "User" object
limitedItems = []
assetsOwned = user.getAssets() #returns an array of "Asset" objects
for asset in assetsOwned:
  if asset.isLimited or asset.isLimitedUnique:
    limitedItems.append(asset)
print(user.username + " owns " + len(limitedItems) + " limited items on Roblox!")
```
#### Finding the groups a user is in
```python
user = Users.getUser(userId) # returns a "User" object
groups = []
groupsIn = user.getGroups() #returns an array of "UserGroupStatus" objects
for groupStatus in groupsIn:
  group = Group(groupStatus.id)
  groups.append(group
print(user.username + " is in " + len(groups) + " group(s)!")
```
#### Finding the amount of enemies a group has
```python
user = Groups.getGroup(groupId) # returns a "Group" object
enemies = group.getEnemies() #returns an array of "Group" objects
print(group.name + " has " + len(enemies) + " enemies on Roblox!")
if len(enemies) > 10:
  print("Woah! That's a lot of enemies! Better not mess with " + group.creator.username + "!")
```


