def cript(frase):
    out = ''
    for i in frase:
        out += chr( ord(i)+69)

    return out

def decript(frase):
    out = ''
    for i in frase:
        out += chr( ord(i)-69)

    return out

