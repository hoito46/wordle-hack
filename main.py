def loading(file):
    try:
        with open(file, 'r') as f:
            data = [line.strip().lower() for line in f]
        return set(data)
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

words = loading('words.txt')
if words is not None:
    print(f"Loaded {len(words)} words.")
    
def get_feedback(guess, secret):
    feedback = [0, 0, 0, 0, 0] 
    secret_list = list(secret)
    guess_list = list(guess)
    
    for i in range(5):
        if guess_list[i] == secret_list[i]:
            feedback[i] = 2
            secret_list[i] = None 
            guess_list[i] = None
            
    for i in range(5):
        if guess_list[i] is not None and guess_list[i] in secret_list:
            feedback[i] = 1
            secret_list[secret_list.index(guess_list[i])] = None 
            
    return tuple(feedback)

"""
test_cases = [
    ("apple", "apply", (2, 2, 2, 2, 0)), 
    ("abcde", "edcba", (1, 1, 2, 1, 1)), 
    ("hello", "world", (0, 1, 0, 0, 2)), 
]

for guess, secret, expected in test_cases:
    result = get_feedback(guess, secret)
    print(f"Guess: {guess}, Secret: {secret} | Result: {result}, Correct: {result == expected}")
"""