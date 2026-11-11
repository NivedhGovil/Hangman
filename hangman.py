import random

def dashmaker(code_word, guess_letters): 
    dash_word = ""
    for letter in code_word: 
        if letter in guess_letters: 
            dash_word += letter
        else: 
            dash_word += "_"
    return dash_word


# dashmaker("hello", ['h', 'l'])


def main(): 
    code_word = random.choice(['electricity', 'donkey', 'hardware', 'xerox', 'transistor', 'computer', 'submarine', 'chess', 'resistance', 'matrix', 'function', 'laser', 'mechanism', 'bodyguard', 'titanic', 'global', 'ozone', 'bridge', 'technology', 'spider', 'six', 'seven', 'algorithm', 'blizzard', 'cascade', 'dynamo', 'eclipse', 'fossil', 'galaxy', 'horizon', 'isotope', 'junction', 'kinetic', 'labyrinth', 'magnet', 'nebula', 'orbit', 'prism', 'quantum', 'radar', 'satellite', 'telescope', 'umbrella', 'vacuum', 'warp', 'xenon', 'yield', 'zenith', 'anchovy', 'biscuit', 'cactus', 'dolphin', 'emerald', 'falcon', 'glacier', 'hammer', 'iguana', 'jungle', 'kangaroo', 'lantern', 'meteor', 'nomad', 'octopus', 'pioneer', 'quartz', 'relic', 'saffron', 'tornado', 'urchin', 'vortex', 'walrus', 'xylophone', 'yacht', 'zodiac', 'altitude', 'battery', 'compass', 'dynasty', 'element', 'friction', 'gravity', 'habitat', 'ignition', 'jigsaw', 'kernel', 'latitude', 'molecule', 'nucleus', 'oxygen', 'piston', 'quasar', 'reactor', 'solstice', 'turbine', 'ultrasound', 'velocity', 'wavelength', 'xray', 'yolk', 'zephyr'])
    guess_letters = []
    a = ""
    guesses = 15
    while True: 
        if guesses == 0: 
            print(f"You are out of guesses! the word was {code_word}")
            break
        a = input("What's your guess? ").lower()

        if len(a) == 1 and a.isalpha():
            guess_letters.append(a)
        else:
            print("Enter one letter at a time.")
        x = dashmaker(code_word, guess_letters)
        if a not in code_word: 
            guesses -= 1
            print(x)
        elif a in code_word: 
            
            print(x)
            
        else: 
            print(f"{a} is not in the word")
        
        
        if x == code_word:
            print(f"You won! The word was {code_word}") 
            break
        else: 
            pass


        

main()

    


