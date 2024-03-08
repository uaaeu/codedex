import random

symbols = ['🍒', '🍇', '🍉', '7️⃣']

def play():
    results = random.choices(symbols, k=3)
    print(f'{results[0]} | {results[1]} | {results[2]}')
    if results[0] == results[1] and results[1] == results[2]:
        print('You win!')
    else:
        print('You lose!')

while True:
    play()
    play_again = input('Play again? (y/n): ')
    if play_again != 'y':
        break
