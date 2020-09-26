def predict(data):
    fever = data["Fever"]
    sb = data["Short_breathe"]
    cough = data["Cough"]
    weakness = data["Weakness"]
    travel = data["Travelled"]
    cc = data["Close_Contact_covid"]
    pne = data["Pneumonia"]
    if (fever and
        (sb or weakness or cough) and
            (close_contact or exposure)) or pnemonia = Test:
        return 1
    else:
        return 0
