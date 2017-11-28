import pickle


# 加载数据
def load_data_from_db(dbname):
    dbtemp = open(dbname,'rb')
    p =pickle.load(dbtemp)
    dbtemp.close()
    return p


# 写入数据库
def write_new_to_db(dbname,data):
    dbtemp = open(dbname,'wb')
    p = pickle.dump(data,dbtemp)
    dbtemp.close()
