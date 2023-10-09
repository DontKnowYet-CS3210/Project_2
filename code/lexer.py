class Lexer:
    def __init__(self, string):
        self.string = string

    tokens = []

    tok_lookup = {
        '}': 'RightBracket',
        '{': 'LeftBracket',
        # '(': 'LeftParen',
        # ')': 'RightParen',
        'public': 'Public',
        'static': 'Static',
        'void': 'Void',
        'class': 'Class',
        'if': 'Decision',
        'else': 'Decision2',
        'switch': 'Decision',
        'while': 'Loop',
        'do': 'DoLoop',
        'for': 'Loop'
    }

    def tokenize(self, lexeme):
        if lexeme in self.tok_lookup:
            return self.tok_lookup[lexeme]

    def lex(self):

        symbols = ['{', '}', '(', ')', '[', ']', '.', '"', '*', '\n', ':', ',']  # single-char keywords
        other_symbols = ['\\', '/*', '*/']  # multi-char keywords
        keywords = ['public', 'private', 'class', 'static', 'void', 'main', 'String', 'int', 'if',
                    'else', 'switch', 'for', 'while', 'do']
        KEYWORDS = symbols + other_symbols + keywords

        white_space = ' '
        lexeme = ''
        loc = []

        for i, char in enumerate(self.string):
            if char == '*':
                if self.string[i - 1] == '/':
                    lexeme += '/*'
                    loc.append(i)
                elif self.string[i + 1] == '/':
                    lexeme += '*/'
                    loc.append(i)
                else:
                    lexeme += '*'
                    loc.append(i)
            elif char == '/':
                if self.string[i + 1] != '*' and self.string[i - 1] != '*':
                    lexeme += '/'
                    loc.append(i)
                else:
                    continue
            else:
                if char != white_space:
                    lexeme += char  # adding a char each time
                    loc.append(i)
            if (i + 1 < len(self.string)):  # prevents error
                if self.string[i + 1] == white_space or self.string[i + 1] in KEYWORDS or lexeme in KEYWORDS:  # if next char == ' '
                    if lexeme != '':
                        #print(lexeme.replace('\n', '<newline>'))
                        #print(loc)
                        if self.tokenize(lexeme.strip()) is not None:
                            self.tokens.append([self.tokenize(lexeme.strip()), loc[0], loc[-1]])
                        loc = []
                        lexeme = ''
