import random

chain = {
    'the': ['cat', 'hat'],
    'hat': ['is'],
    'is': ['really'],
    'cat': ['has'],
    'has': ['no', 'big'],
    'no': ['paws'],
    'big': ['poops'],
    'really': ['big'],
}

sentence = 'the'
token = 'the'

while token in chain:
    # pick a random word from the list of "next words"
    numWords = len(chain[token])
    choice = random.randint(0, numWords - 1)

    # change tokens for next loop
    token = chain[token][choice]

    # add our token to the end of the sentence
    sentence += ' ' + token

print sentence
