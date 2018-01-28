__author__ = 'Sudheer'
import pymongo

connection = pymongo.MongoClient(host="mongodb://localhost")
db = connection.momentdata


def insert_zernike_moments_into_database(key, mean, value):
    zernike = db.zernike
    try:
        zernike.insert_one({"key": key, "mean": mean, "value": value})
    except Exception as e:
        print "Unexpected Exception", e


def find_object_via_zernike_moments(key):
    zernike = db.zernike
    try:
        result = zernike.find_one({"key": key})
        return result['value']
    except:
        raise Exception


def insert_Hu_moments_into_database(key, mean, value):
    hu = db.hu
    try:
        hu.insert_one({"key": key, "mean": mean, "value": value})
    except Exception as e:
        print "Unexpected Exception", e


def find_object_via_Hu_moments(key):
    hu = db.hu
    try:
        result = hu.find_one({"key": key})
        return result['value']
    except:
        raise Exception
