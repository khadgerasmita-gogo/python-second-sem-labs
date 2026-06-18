people={'John':25,'Emma':15,'Lucus':8,'Sophia':42}

def classify_age(age):
    if age<13:
        return "Child"
    elif age>13 and age<19:
        return "Teen"
    elif age>=20 :
        return "Adult"
    

classified={key:classify_age(value) for (key,value) in people.items()}

print(classified)
