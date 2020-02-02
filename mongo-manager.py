import tokens
from pymongo import MongoClient

class MongoDBManager:
    def __init__(self):
        self.client = MongoClient(f"mongodb+srv://marlonvc:{tokens.MONGODB_PASS}@whoami-bot-1gfnt.mongodb.net/test?retryWrites=true&w=majority")
        self.db = self.client.database
        self.chats = self.db.chats

    def insert_chat(self, chat_data):
        self.chats.insert_one(chat_data)


    def checkChat(self, chat_id):
        chats = self.chats.find({})

        for r in chats:
            print(r)
            
    #     if not (chat_id in c.chats):
    #         c.chats.append(chat_id)
    #         c.put()
    #         return True
    #     return False
    #
    # def getChats():
    #     c = ndb.Key(Chats, 'chats').get()
    #     return c.chats
    #
    # def delChat(chat_id):
    #     c = ndb.Key(Chats, 'chats').get()
    #     if chat_id in c.chats:
    #         c.chats.remove(chat_id)
    #     c.put()
    #     return

if __name__ == '__main__':
    mongodb = MongoDBManager()
    # mongodb.insert_chat({'chat': '1'})

    mongodb.checkChat(1)
#
# post = {"author": "Marlon",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"]}
#
# post_id = posts.insert_one(post)
# print(post_id)
#
# cursor = posts.find()
# print(cursor)
# for record in cursor:
#     print(record)
