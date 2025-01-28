def calculate_love_score(name1, name2):
    combined_name = name1.lower() + name2.lower()
    
    true = 'true'
    love = 'love'
    
    true_count = 0
    love_count = 0
    
    for letter in true:
        for char in combined_name:
            if letter == char:
                true_count += 1
                
    for letter in love:
        for char in combined_name:
            if letter == char:
                love_count += 1
        
                
    print(str(true_count) + str(love_count))
    
calculate_love_score("Kanye West", "Kim Kardashian")