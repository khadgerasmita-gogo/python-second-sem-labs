scores={"Alice":85, "Bob":60,"Charlie":90,"Diana":55}

students_passed={key:value for (key,value) in scores.items() if value>=70}
print(students_passed)