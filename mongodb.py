__author__ = 'larkin'

import pymongo

CLIENT = pymongo.MongoClient("121.199.20.234", 27017)
DB = CLIENT['activity']
