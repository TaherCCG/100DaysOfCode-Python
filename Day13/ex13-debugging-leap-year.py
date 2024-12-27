def is_leap(year):
    print(f"Checking year: {year}")
    if year % 4 == 0:
        print("Divisible by 4")
        if year % 100 == 0:
            print("Divisible by 100")
            # if year % 4000 == 0:  problem here
            if year % 400 == 0:  # Correct condition
                # the error is that the year should be divisible by 400 instead of 4000
                
                print("Divisible by 400")
                return True
            else:
                print("Not divisible by 400")
                return False
        else:
            print("Not divisible by 100")
            return True
    else:
        print("Not divisible by 4")
        return False

    
print(is_leap(2000))  # This should be true.
