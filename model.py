import pickle
import numpy as np


def predict(data):
    fever = data["fever"]
    sb = data["breathe"]
    cough = data["cough"]
    weakness = data["weakness"]
    travel = data["travelled"]
    close_contact = data["contact"]
    pneumonia = data["pneumonia"]
    symptoms = []
    symptoms.extend([fever, sb, cough, weakness, travel,
                     close_contact, pneumonia])
    pkl_filename = "./model-covid.pkl"
    with open(pkl_filename, 'rb') as file:
        covid_classifier_pkl = pickle.load(file)
    arr_symptoms = np.array(symptoms)
    prediction = covid_classifier_pkl.predict(
        arr_neg.reshape(-1, len(symptoms)))
    return prediction
    # if (fever and (sb or weakness or cough) and (close_contact or pneumonia)):
    #    return True
    # else:
    #    return False
