poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day In a relative way, And
returned on the previous night.'''
print(poem)


try:
    fout = open('relativety', 'xt')
    fout.write(poem)
    fout.close()

except FileExistsError:
    print('relativety already exists! That was a close one.')