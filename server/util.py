import json
import pickle
import numpy as np


__countries = None
__data_columns = None
__items = None
__model = None


def get_estimated_crop_yield(country,item,avg_rainfall,pesticides_tonnes,avg_temp):
    try:
        country_index = __data_columns.index(country.lower())
    except:
        country_index = -1
    try:
        item_index = __data_columns.index(item.lower())
    except:
        item_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = avg_rainfall
    x[1] = pesticides_tonnes
    x[2] = avg_temp
    if country_index >= 0:
        x[country_index] = 1
    if item_index >= 0:
        x[item_index] = 1
    return round(__model.predict([x])[0],2)



def get_country_names():
    return __countries


def get_item_names():
    return __items


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __countries
    global __items
    global __model
    with open("./artifacts/columns.json",'r') as f:
        __data_columns  = json.load(f)['data_columns']
        __countries = __data_columns[3:-10]
        __items = __data_columns[-10:]

    with open("./artifacts/crop_yield_prediction_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")


if __name__ ==  '__main__':
    load_saved_artifacts()
    print(get_country_names())
    print(get_item_names())
    print(get_estimated_crop_yield('country_albania','item_maize',1485.0,121.0,16.37))
