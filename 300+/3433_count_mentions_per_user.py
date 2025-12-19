

from typing import List

"""
3433. Count Mentions Per User (https://leetcode.com/problems/count-mentions-per-user/?envType=daily-question&envId=2025-12-15)

first make sure to sort all events by their timestamp in ascending order cause thats how time works
    SINCE OFFLINE/ONLINE THINGS ARE PROCESSED BEFORE ANY EVENT, MAKE SURE YOU SORT BY EVENT == "MESSAGE"
    THIS PRIORITIZES OFFLINE EVENT BEFORE MESSAGE EVENTS AS A SECONDARY SORT

all you need to keep track of are the times that each user becomes online
create a list online_time, where online_time[i] is the latest time we know so far that user[i] becomes online

if offine event:
    change the specified user's online_time[user] to 60 minutes from the current timestamp
    online_time[user] = timestamp + 60

if message event:
    if all -> mentions every user -> just increment the mention for each user from 0 to n-1 by 1
    if here -> mentions only online users
        we use the online_time list to see which users are online at the time of the message
        since online_time[user] contains the latest time we know a user becomes online
            we just need to check whether or not the current time is after online_time[user]
            for each user: if timestamp >= online_time[user], then the user becomes online before the event, count them in the mention

if mentining multiple people:
    make sure to split the string by space
    also make sure to clean each user_id with int(user[2:]), since each user_id is in the string format of ex. "id20", "id1", "id6", etc.

runtime: O(n logn) where n is the number of users
space: O(n)
"""

def countMentions(numberOfUsers: int, events: List[List[str]]) -> List[int]:
    n = numberOfUsers
    online_time = [0] * n # online_time[i] will represent the latest time we know that user[i] will be online
    events.sort(key=lambda evt: (int(evt[1]), evt[0] == "MESSAGE")) # sort by the timestamp element, and prioritize non-messages
    mentions = [0 for _ in range(n)]

    for evt, timestamp, mentions_str in events:
        timestamp = int(timestamp)

        if evt == "OFFLINE":
            online_time[int(mentions_str)] = timestamp + 60

        elif evt == "MESSAGE":
            if mentions_str == "ALL":
                for user in range(n):
                    mentions[user] += 1

            elif mentions_str == "HERE":
                for user in range(n):
                    if timestamp >= online_time[user]:
                        mentions[user] += 1

            else: # mentions is a string of users
                for user in mentions_str.split():
                    mentions[int(user[2:])] += 1

    return mentions

numberOfUsers = 3
events = [["OFFLINE","1","0"],
          ["MESSAGE","2","HERE"],
          ["OFFLINE","2","1"],
          ["MESSAGE","61","HERE"]]
print(countMentions(numberOfUsers, events))

        




