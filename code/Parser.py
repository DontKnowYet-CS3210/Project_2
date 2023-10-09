import lexer

def removeChar(s,i):
    b = bytearray(s, 'utf-8')
    del b[i]
    return b.decode()


def parse(file):

    public_count = 0
    brackets = []



    text_file = open(file)
    file_string = text_file.read()
    fixed_file = file_string

    l1 = lexer.Lexer(file_string)
    l1.lex()

    print(l1.tokens)

    for i in range(len(l1.tokens)):
        current_tok = l1.tokens[i][0]
        next_tok = l1.tokens[i+0][0]
        prev_tok = l1.tokens[i-1][0]

        if current_tok == 'Class':
            if next_tok != 'LeftBracket':
                print('Missing right bracket after class')
                # Code to add a bracket at the index given by l1.tokens[i][2]
                brackets.append('{')
        if current_tok == 'Public':
            public_count += 1
            if next_tok != "Static":
                print("missing static after void")
                print(f"ended at {l1.tokens[i][2]}")
                break
        if current_tok == 'Static':
            public_count += 1
            if next_tok != "Void":
                print("missing void after static")
                print(f"ended at {l1.tokens[i][2]}")
                break
        if current_tok == 'Void':
            public_count += 1
            if next_tok != "LeftBracket":
                print("missing left bracket after void")
                # Code to add a bracket at the index given by l1.tokens[i][2]
                brackets.append('{')







    text_file.close()
    print(f'the amount of times the public keyword was used is: {public_count}')
    print(f'this is the old file...\n{file_string}')
    print(f'this is the fixed file...\n{fixed_file}')
