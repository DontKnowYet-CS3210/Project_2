import re
# java code formatter


print("Reading input...")


def format_code(input_program):
    # Ensure curly braces for decision structures
    structures = ['if', 'else if', 'while', 'for', 'do']

    lines = input_program.split('\n')
    formatted_lines = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Identify if line starts with one of the structures
        if any(line.startswith(struct) for struct in structures) or 'else:' in line:
            if not line.endswith("{"):
                formatted_lines.append(line + " {")

                # Check for next non-empty line
                i += 1
                while not lines[i].strip():
                    formatted_lines.append(lines[i])
                    i += 1

                formatted_lines.append(lines[i])
                formatted_lines.append("}")
            else:
                formatted_lines.append(line)
        else:
            formatted_lines.append(line)
        i += 1

    # Combining the formatted lines
    return '\n'.join(formatted_lines)


print("Input formatted...")


def count_public(input_program):
    return len(re.findall(r'\bpublic\b', input_program))


def write_to_file(original_program, updated_program, count_public):
    with open('output.txt', 'w') as f:
        f.write("Original Program:\n")
        f.write(original_program)
        f.write("\n\nUpdated Program:\n")
        f.write(updated_program)
        f.write("\n\nCount of 'public' keyword: ")
        f.write(str(count_public))


print("Output written to output.txt")


if __name__ == "__main__":
    input_program = open('Test.java', 'r').read()
    updated_program = format_code(input_program)
    pub_count = count_public(input_program)
    write_to_file(input_program, updated_program, pub_count)
