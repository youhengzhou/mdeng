def markdown_to_dict(markdown_text):
    lines = markdown_text.split("\n")
    stack = [{}]
    for line in lines:
        if not line:  # Skip empty lines
            continue
        key = line.lstrip("# ").rstrip()
        if line.startswith("#"):
            level = line.count("#", 0, len(line) - len(line.lstrip()))
            while len(stack) > level:
                stack.pop()
            if stack:  # Check if stack is not empty
                stack[-1][key] = {}
                stack.append(stack[-1][key])
        else:
            if len(stack) > 1:
                stack[-2][key] = line.rstrip()
            elif stack:  # Check if stack is not empty
                stack[-1][key] = line.rstrip()
    return stack[0] if stack else {}  # Return an empty dict if stack is empty


markdown_text = """
# name
Alice
# role
warrior
# weapon
## type
sword
## quality
fine
## damage
### type
slash
### amount
1
# armor
## type
leather
## quality
fine
"""

result = markdown_to_dict(markdown_text)
print(result)
