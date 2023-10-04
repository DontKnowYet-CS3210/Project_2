import lexer
def parse(file):
    textFile = open(file)
    fileString = textFile.read()

    l1 = lexer.Lexer(fileString)
    l1.lex()
    print(l1.tokens)

    textFile.close()
    print(fileString)
