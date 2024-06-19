'''
Question - 
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Example - 
    Note that an empty string is also considered valid.

    Example 1:

    Input: "()"
    Output: true
    Example 2:

    Input: "()[]{}"
    Output: true
    Example 3:

    Input: "(]"
    Output: false
    Example 4:

    Input: "([)]"
    Output: false
    Example 5:

    Input: "{[]}"
    Output: true

'''

input_string = "[()[()]{()}]"

def validate_braces(strings):
    braces_hash = {
        '()', '[]', '{}'
    }

    stack = []

    for brace in strings:
        if brace in '([{':
            stack.append(brace)
        elif not stack or stack.pop() + brace not in braces_hash:
            return False
    return not stack



# print(validate_braces(input_string))


# stack = []
# stack.append('(')
# stack.append('p')
# print(stack)
# print(not stack)
# print(stack.pop())
# print(stack)
# print(not stack)


