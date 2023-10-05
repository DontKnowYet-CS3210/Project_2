

def format_code(filename):
    with open(filename, 'r') as file:
        input_code = file.read()

    lines = input_code.split("\n")
    output_code = []
    stack = []
    public_count = 0
    indent_level = 0
    indent_size = 4  # 4 spaces per indentation level; can be adjusted

    for line in lines:
        stripped_line = line.strip()

        # Counting 'public' keyword occurrences
        public_count += stripped_line.count('public')

        # Decrease indentation for closing curly braces
        if '}' in stripped_line:
            indent_level -= 1

        # Apply current indentation
        current_indent = ' ' * (indent_level * indent_size)
        indented_line = current_indent + stripped_line

        # Check for missing curly braces and adjust indentation accordingly
        if 'MISSING OPEN CURLY BRACE' in stripped_line:
            output_code.append(current_indent + "{")
            stripped_line = stripped_line.replace('// MISSING OPEN CURLY BRACE', '')
            stack.append('{')
            indent_level += 1

        if 'MISSING CLOSE  CURLY BRACE' in stripped_line:
            indent_level -= 1
            output_code.append(current_indent + "}")
            stripped_line = stripped_line.replace('// MISSING CLOSE CURLY BRACE', '')
            if stack and stack[-1] == '{':
                stack.pop()

        # Adjust indentation based on actual curly braces in the line
        for char in stripped_line:
            if char == '{':
                stack.append('{')
                indent_level += 1
            elif char == '}':
                if stack and stack[-1] == '{':
                    stack.pop()

        output_code.append(indented_line)

    # If there are unmatched opening braces, append closing braces
    while stack:
        indent_level -= 1
        output_code.append(' ' * (indent_level * indent_size) + "}")
        stack.pop()

    formatted_code = "\n".join(output_code)
    
    # Write to output.txt
    with open('output.txt', 'w') as output_file:
        output_file.write("=== ORIGINAL ===\n")
        output_file.write(input_code)
        output_file.write("\n\n=== FORMATTED ===\n")
        output_file.write(formatted_code)
        output_file.write(f"\n\nPublic Count: {public_count}")

# Call the function with your file name
format_code("Test.java")
