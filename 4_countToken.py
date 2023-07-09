import tokenize

def count_tokens(code):
    tokens = tokenize.tokenize(code)
    count = 0
    for token in tokens:
        count += 1
    return count

# Example usage
code = "print('Hello, world!')"
num_tokens = count_tokens(code)
print("Number of tokens:", num_tokens)
# Keywords.
# Identifiers.
# Literals.
# Operators.