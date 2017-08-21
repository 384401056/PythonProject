from pymongo import MongoClient


class Write_to_mongo:

    def __init__(self, ip, port, db_name, col_name):
        self.db_name = db_name
        self.col_name = col_name
        self.col = MongoClient(ip, port)[db_name][col_name]


    def __call__(self, data):
        self.col.insert(data)

if __name__ == '__main__':
    pass