def life_in_weeks(age):
    weeks_in_a_year = 52
    target_age = 90
    
    weeks_left = (target_age - age) * weeks_in_a_year
    
    print(f"You have {weeks_left} weeks left.")
    
life_in_weeks(20)
life_in_weeks(40)
life_in_weeks(70)
life_in_weeks(12)
life_in_weeks(56)