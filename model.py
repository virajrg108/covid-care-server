def predict(data):
    fever = data["fever"]
    sb = data["breathe"]
    cough = data["cough"]
    weakness = data["weakness"]
    travel = data["travelled"]
    close_contact = data["contact"]
    pneumonia = data["pneumonia"]
    if (fever and (sb or weakness or cough) and (close_contact or pneumonia)):
        return True
    else:
        return False
