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

    print(f'{l1.tokens}\n')

    for i in range(len(l1.tokens)):
        current_tok = l1.tokens[i][0]
        print(current_tok)
        if i >= len(l1.tokens)-1:
            print('Done parsing\n')
            if current_tok == 'RightBracket':
                if not brackets:
                    # code to delete the bracket
                    print("too many right brackets")
                else:
                    brackets.pop(-1)
            else:
                print("not valid last token")
        else:
            next_tok = l1.tokens[i + 1][0]
            prev_tok = l1.tokens[i - 1][0]
            if current_tok == 'Class':
                if next_tok != 'LeftBracket':
                    print('Missing left bracket after class')
                    print(next_tok)
                    # Code to add a bracket at the index given by l1.tokens[i][2]
                    brackets.append('{')
            if current_tok == 'Public':
                public_count += 1
                if next_tok != "LeftBracket":
                    print("missing left bracket after public")
                    # Code to add a bracket at the index given by l1.tokens[i][2]
                    brackets.append('{')
            if current_tok == 'Decision':
                if next_tok != "LeftBracket":
                    print("missing left bracket after if")
                    # Code to add a bracket at the index given by l1.tokens[i][2]
                    brackets.append('{')
            if current_tok == 'Else':
                if prev_tok != 'RightBracket':
                    print("missing right bracket before else")
                    # Code to add a bracket at the index given by l1.tokens[i][2]
                    brackets.pop(-1)
                if next_tok == "Decision":
                    continue
                elif next_tok != 'LeftBracket':
                    print("missing left bracket after else")
                    # Code to add a bracket at the index given by l1.tokens[i][2]
                    brackets.append('{')
            if current_tok == 'Loop':
                if next_tok != "LeftBracket":
                    print("missing left bracket after a loop")
                    # Code to add a bracket at the index given by l1.tokens[i][2]
                    brackets.append('{')
            if current_tok == 'RightBracket':
                if not brackets:
                    # code to delete the bracket
                    print("too many right brackets")
                else:
                    brackets.pop(-1)
            if current_tok == 'LeftBracket':
                brackets.append('{')

    if brackets != []:
        print("missing brackets")
        # code to add the last bracket
        brackets.pop(-1)
        print(brackets)

    text_file.close()
    print(f'the amount of times the public keyword was used is: {public_count}\n')
    print(f'this is the old file...\n{file_string}')
    # print(f'this is the fixed file...\n{fixed_file}')
