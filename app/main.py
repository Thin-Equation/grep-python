import sys
from string import ascii_letters, digits
# import re
# import pyparsing - available if you need it!
# import lark - available if you need it!
def match_pattern(input_line: str, pattern: str):
    """Basic pattern matching"""
    if len(pattern) == 1:
        return pattern in input_line
    if pattern == r"\d":
        return any(char.isdigit() for char in input_line)
    if pattern == r"\w":
        return any(char.isalnum() for char in input_line)
    if pattern[0] == r"[" and pattern[-1] == r"]":
        if pattern[1] == r"^":
            return not any(char in pattern for char in input_line)
        return any(char in pattern for char in input_line)
    raise RuntimeError(f"Unhandled pattern: {pattern}")
    # return re.search(pattern, input_line)
def main():
    """Main."""
    pattern = sys.argv[2]
    input_line = sys.stdin.read()
    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        sys.exit(1)
    # You can use print statements for debugging, they'll be visible when running tests.
    res = match_pattern(input_line, pattern)
    print(f"Res: {res}")
    sys.exit(not res)
if __name__ == "__main__":
    main()