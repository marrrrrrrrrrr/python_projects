'''
მომხმარებელს შეუძლია ითამაშოს ინგლისური ან ქართული სიტყვებით.
მან უნდა გამოიცნოს დაფარული სიტყვა თითო-თითო ასოების გამოცნობით.
აქვს შეზღუდული რაოდენობის მცდელობები და თუ ამ მცდელობისას სიტყვას ვერ გამოიცნობს, თამაში მთავრდება და სიტყვა ვლინდება.
ყოველი თამაშის შემდეგ მოთამაშეს აქვს შესაძლებლობა კვლავ ითამაშოს ან თამაშიდან გავიდეს.

ვალიდაციები:
- როდესაც მომხმარებელს სთხოვენ აირჩიოს ენა, პროგრამა უზრუნველყოფს, რომ მის მიერ მოწოდებული input იყოს „1“ ან „2“ (ანუ ციფრი შეესაბამებოდეს ენას, რომელიც მას სურს)
- პროგრამა მომხმარებელს სთხოვს გამოიცნოს ასო - input უნდა აკმაყოფილებდეს შემდეგ კრიტერიუმებს: სიგრძე იყოს 1-ის ტოლი და შეიცავდეს მხოლოდ ანბანურ სიმბოლოს
- პროგრამა ამოწმებს, უკვე გამოიცნო თუ არა მომხმარებელმა ასო, რა შემთხვევაშიც აცნობებს მას, რომ ეს ასო უკვე გამოცნობილია და სთხოვს მას გამოიცნონ სხვა ასო

'''


import random

english_word_list = ["mountain", "ocean", "elephant", "watermelon", "rainbow", "country", "waterfall", "python", "guitar", "dragon",
                    "bookcase", "dictionary", "autumn", "basketball", "butterfly", "cinema", "yesterday", "umbrella", "helicopter", "engineer"]

georgian_word_list = ["ფანქარი", "პეპელა", "ფილოსოფია", "ღრუბელი", "ცისარტყელა", "მსხალი", "ვეშაპი", "დინოზავრი", "ბატკანი", "ჭაობი",
                      "ბროწეული", "გვირილა", "ღუმელი", "ჰიდროელექტროსადგური", "დედაქალაქი", "პითონი", "კურდღელი", "ფორტეპიანო", "ვულკანი", "სათვალე"]

# ფუნქცია, რომელიც აირჩევს სიტყვას შემთხვევითობის პრინციპით. პარამეტრად გადაეცემა ენა, რომელსაც მომხმარებელი მიუთითებს და აბრუნებს სიტყვას
def choose_word(language):
    if language == '2':
        return random.choice(georgian_word_list)
    else:
        return random.choice(english_word_list)

# ფუნქცია, რომელსაც გამოაქვს გამოსაცნობი სიტყვა - გამოუცნობი ასოების ნაცვლად ქვედა ტირე. პარამეტრად გადაეცემა სიტყვა, რომელიც უნდა გამოვიცნოთ და გამოცნობილი ასოების სია
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += '_ '
    return display


def play_hangman():
    print("Welcome to Hangman!")
    print("Choose a language:")
    print("1. English")
    print("2. Georgian")
    
    # ვალიდაცია ენის არჩევისას
    language_choice = input("Enter your choice (1/2): ")
    while language_choice not in ['1', '2']:
        print("Invalid choice. Please enter 1 for English or 2 for Georgian.")
        language_choice = input("Enter your choice (1/2): ")
    
    # ირჩევს სიტყვას მითითებული ენის მიხედვით
    word = choose_word(language_choice)
    guessed_letters = []  # სია გამოცნობილი ასოების შესანახად
    attempts = 10  # დაშვებული მცდელობების რაოდენობა
    
    while attempts > 0:
        # გამოაქვს სიტყვის მიმდინარე მდგომარეობა
        display = display_word(word, guessed_letters)
        print("\nWord:", display)
        
        # ამოწმებს სრულად გამოიცნო თუ არა სიტყვა
        if '_' not in display:
            print("Congratulations! You guessed the word:", word)
            break
        
        # სთხოვს მოთამაშეს გამოიცნოს ასო
        guess = input("Guess a letter: ").lower()
        
        # ამოწმებს, არის თუ არა მომხმარებლის input-ის სიგრძე 1-ის ტოლი და შეიცავს თუ არა მხოლოდ ანბანურ სიმბოლოებს
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # ამოწმებს, არის თუ არა ასო უკვე გამოცნობილი
        if guess in guessed_letters:
            print("You've already guessed the letter '{}'.".format(guess))
            continue
        
        # ამატებს სწორად გამოცნობილ ასოს სიაში
        guessed_letters.append(guess)
        
        # ამოწმებს გამოცნობილი ასო თუ არის სიტყვაში და ამცირებს დარჩენილი მცდელობების რაოდენობას, თუ შეყვანილი ასო სიტყვაში არ არის.
        if guess not in word:
            attempts -= 1
            print("Incorrect guess. Attempts left:", attempts)
    
    # თუ მცდელობები ამოეწურება, გამოაქვს რა იყო გამოსაცნობი სიტყვა
    if attempts == 0:
        print("You are out of attempts! The word was:", word)
    
    # ეკითხება მოთამაშეს, სურს თუ არა კვლავ თამაში
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again in ['yes', 'y', 'yeah', 'yup', 'sure']:
        play_hangman()
    else:
        print("Thanks for playing!")

play_hangman()