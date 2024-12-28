from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]

# the dice will show a random number between 1 and 6 but it will get an error because the index is out of range. it should be between 0 and 5
# dice_num = randint(1, 6)
dice_num = randint(0, 5)
print(dice_images[dice_num])