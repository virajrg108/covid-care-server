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
    arr_symptoms = arr_symptoms.reshape(-1, 7)

    prediction = covid_classifier_pkl.predict(arr_symptoms)[0]
    
    print(prediction)
    print(type(prediction))

    if prediction == 0:
        return False
    
    return True


    # if (fever and (sb or weakness or cough) and (close_contact or pneumonia)):
    #    return True
    # else:
    #    return False


def severity(test1, test2):
    # only one test required
    if test1 != 0:
        if test1 < 8:
            return "mild"
        elif test1 < 15:
            return "moderate"
        else:
            return "severe"
    else:
        if test2 < 2:
            return "mild"
        elif test2 < 4:
            return "moderate"
        else:
<<<<<<< HEAD:python_modules/model.py
            return "severe"
=======
            return "severe"
>>>>>>> ae84681d643eee51c770612b69cfc581a36bca30:model.py
