mdg = MDEng()

noble = {
    "name": "Alice",
    "type": "noble",
    "age": 18,
    "gender": "female",
}

mdg.create(noble, "noble.md")
print(mdg.read("noble.md"))

import jsoneng

jdb = jsoneng.JsonDB(mdg.read("noble.md"))

data = jdb.retrieve()

mdg.create(data, "jdb.md")
