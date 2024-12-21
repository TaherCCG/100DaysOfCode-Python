# Love Calculator

def calculate_love_score(name1, name2):
    combined_names= (name1 + name2).lower()
    
    true_letters = "true"
    love_letters = "love"
    
    true_count = sum(combined_names.count(letter) for letter in true_letters)
    love_count = sum(combined_names.count(letter) for letter in love_letters)
    
    love_score = int(f"{true_count}{love_count}")
    
    print(love_score)
    
calculate_love_score("Kanye West", "Kim Kardashian")

