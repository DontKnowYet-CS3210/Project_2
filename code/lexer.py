class Lexer:
    def __int__(self, code):
        self.input = code

    tokens = []

    tok_lookup = {
        '}': 'RightBracket',
        '{': 'LeftBracket',
        '(': 'LeftParen',
        ')': 'RightParen',
        ';': 'Semi',
        'public': 'Start',
        'void': 'Void',
        'if': 'Decision',
        'if-else': 'Decision',
        'if-else-if': 'Decision',
        'switch': 'Decision',
        'while': 'Loop',
        'do-while': 'Loop',
        'for': 'Loop'
    }

    def tokenize(self, lexeme):
        if lexeme in self.tok_lookup:
            self.tokens.append(self.tok_lookup[lexeme])

    def lexer(self):

        string = '''
        public class Test {

           public static void main(String args[]) {
              int [] numbers = {10, 20, 30, 40, 50};
              // printing !
              for(int x : numbers ) {
                 System.out.print( x );
                 System.out.print(",");
              }
              System.out.print("\n");
              String [] names = {"James", "Larry", "Tom", "Lacy"};
              /*
              looping over 
              */
              for( String name : names ) {
                 System.out.print( name );
                 System.out.print(",");
              }
           }
        }
        '''

        symbols = ['{', '}', '(', ')', '[', ']', '.', '"', '*', '\n', ':', ',']  # single-char keywords
        other_symbols = ['\\', '/*', '*/']  # multi-char keywords
        keywords = ['public', 'class', 'void', 'main', 'String', 'int', 'if',
                    'if-else', 'if-else-if', 'switch', 'for', 'while', 'do-while']
        KEYWORDS = symbols + other_symbols + keywords

        white_space = ' '
        lexeme = ''

        for i, char in enumerate(self.input):
            if char == '*':
                if string[i - 1] == '/':
                    lexeme += '/*'
                elif string[i + 1] == '/':
                    lexeme += '*/'
                else:
                    lexeme += '*'
            elif char == '/':
                if string[i + 1] != '*' and string[i - 1] != '*':
                    lexeme += '/'
                else:
                    continue
            else:
                if char != white_space:
                    lexeme += char  # adding a char each time
            if (i + 1 < len(string)):  # prevents error
                if string[i + 1] == white_space or string[i + 1] in KEYWORDS or lexeme in KEYWORDS:  # if next char == ' '
                    if lexeme != '':
                        print(lexeme.replace('\n', '<newline>'))
                        lexeme = ''
