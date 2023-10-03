import mdeng

mdg = mdeng.MdDB()

noble = {
    "name": "Alice",
    "role": "warrior",
    "weapon": {
        "type": "sword",
        "quality": "fine",
        "damage": {
            "type": "slash",
            "amount": 1,
        },
    },
    "armor": {
        "type": "leather",
        "quality": "fine",
    },
}

mdg.create(noble, "noble.md")
print(mdg.read("noble.md"))

import jsoneng

jdb = jsoneng.JsonDB(mdg.read("noble.md"))

data = jdb.retrieve()

mdg.create(data, "jdb.md")
