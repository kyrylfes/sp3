import re

# Regular expressions for token identification
number_pattern = r'\d+(\.\d+)?|\.\d+'
string_pattern = r'\'[^\']*\'|"[^"]*"'
directive_pattern = r'\{[^}]*\}'
comment_pattern = r'\/\/([^\n]*)'
reserved_words_list = [
    'begin', 'end', 'if', 'then', 'else', 'while', 'do', 'repeat', 'until',
    'for', 'to', 'downto', 'array', 'of', 'function', 'procedure', 'var',
    'const', 'integer', 'real', 'boolean', 'char', 'string'
]
identifier_pattern = r'\b\w+\b'
operator_pattern = r'\+|\-|\*|<|>|:=|>=|<=|%|<>|&|\||!|~|<<|\*|>>'

# Opening and reading the Pascal program file
with open('pascal.pas', 'r') as file:
  program_code = file.read()

number_tokens = re.findall(number_pattern, program_code)

string_tokens = re.findall(string_pattern, program_code)

directive_tokens = re.findall(directive_pattern, program_code)

comment_tokens = re.findall(comment_pattern, program_code)

reserved_words_tokens = re.findall("|".join(map(re.escape, reserved_words_list)), program_code)

identifier_tokens = re.findall(identifier_pattern, program_code)

operator_tokens = re.findall(operator_pattern, program_code)

# Output results
print("Numbers:", number_tokens)
print("Strings:", string_tokens)
print("Directives:", directive_tokens)
print("Comments:", comment_tokens)
print("Reserved Words:", reserved_words_tokens)
print("Operators:", operator_tokens)
print("Identifiers:", identifier_tokens)
