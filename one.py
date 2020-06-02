'''
f("junyiacademy") == "ymedacaiynuj"
f("flipped class room is important") == "deppilf ssalc moor si tnatropmi"
'''

def func_a(string: str):
    '''
    f("junyiacademy") == "ymedacaiynuj"
    '''
    return string[::-1]


def func_b(string: str):
    '''
    f("flipped class room is important") == "deppilf ssalc moor si tnatropmi"
    '''
    return ' '.join([
        func_a(word)
        for word in string.split()
    ])


if __name__ == '__main__':
    print(func_a("junyiacademy") == "ymedacaiynuj")
    print(func_b("flipped class room is important") == "deppilf ssalc moor si tnatropmi")
