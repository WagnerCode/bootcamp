kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

i = 0
for key in kata.keys():
    print(f"{key} was created by {kata[list(kata.keys())[i]]}")
    i += 1