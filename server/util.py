import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = _data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >=0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)




def load_saved_artifacts():
    print('loading saved artifacts...start')
    global __data_columns
    global __locations

    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    with open('./artifacts/real_estate_price_prediction_Bengluru.pickle', 'rb') as f:
        __model = pickle.load(f)
    print('loading saved artifacts...done')

def get_location_names():
    global __locations
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3,3))
    print(get_estimated_price('1st Phase JP Nager', 1000, 2, 2))
    print(get_estimated_price('Kathalli', 1000, 2,2))# other locations
    print(get_estimated_price('Ejipur', 1000, 2,2)) # other locations