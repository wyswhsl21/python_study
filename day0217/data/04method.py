def dic_method(**p):
    for i in p.keys():
        print(i, ':', p[i])
    print()


def profile(name, age, *language):
    print(
        name,
        '',
        age,
    )
    for lang in language:
        print(lang, end=' ')
    print()
    print()


profile('유재석', 30, 'django', 'react', 'bigData', 'python', 'MLAI', 'opencv')
profile('조세호', 25, 'flask', 'react', 'bigData', 'python', 'MLAI', 'opencv')
