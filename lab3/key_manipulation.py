scores={"Alice":85, "Bob":60,"Charlie":90,"Diana":55}

key_uppercased={key.upper() :value for (key,value) in scores.items()}
print(key_uppercased)