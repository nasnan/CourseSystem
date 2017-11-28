# import sys
# import os
#
# BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
#
# from modules.school import School
# from dbapi import *
#
# school_Db = School("sch1")
#
# write_new_to_db("database.db",school_Db)
#


import sys
import os

BASE_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from modules.school import School
from dbapi import *


school_db = load_data_from_db("database.db")

print(school_db)