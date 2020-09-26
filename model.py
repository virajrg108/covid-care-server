def predict(data):
    fever = data["Fever"]
    sb = data["Short_breathe"]
    cough = data["Cough"]
    weakness = data["Weakness"]
    travel = data["Travelled"]
    close_Contact_covid = data["Close_Contact_covid"]
    pneumonia = data["Pneumonia"]
    if ((fever and (sb or weakness or cough) and (close_contact or exposure)) or pnemonia=Test):
        return "yes"
    else:
        return "no"
