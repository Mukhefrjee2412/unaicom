def prediction_model(pclass, sex, age, sibsp, parch,fare,embarked, title ):
    import pickle
    # Dont change the prder of narguments as data form also follows same
    x = [[pclass, sex, age, sibsp, parch,fare,embarked, title]]
    randomforest = pickle.load(open('titanic_model.sav', 'rb'))
    prediction = randomforest.predict(x)
    if prediction==1:
        prediction = "Survived"
    elif prediction==0:
        prediction = "Not Survived"
    else:
        prediction = "Error"
    return prediction
    # print(predictions)
