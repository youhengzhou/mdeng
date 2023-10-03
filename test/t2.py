def parse_markdown(lines):
    output = {}
    # Initialize an empty stack to keep track of the nesting levels
    stack = []
    # Loop through the lines
    for line in lines:
        # Strip any whitespace from the line
        line = line.strip()
        # If the line is empty, skip it
        if not line:
            continue
        # If the line starts with a hash sign, it is a key
        if line.startswith("#"):
            # Count the number of hash signs to determine the level
            level = len(line) - len(line.lstrip("#"))
            # Get the key name by removing the hash signs and whitespace
            key = line.lstrip("#").strip()
            # If the level is one, it is a top-level key
            if level == 1:
                # Add the key and an empty dictionary to the output dictionary
                output[key] = {}
                # Reset the stack and push the key to it
                stack = [key]
            # If the level is greater than one, it is a nested key
            else:
                # Pop the stack until it has the same size as the level minus one
                while len(stack) > level - 1:
                    stack.pop()
                # Get the parent dictionary by traversing the output dictionary using the stack
                parent = output
                for k in stack:
                    parent = parent[k]
                # Add the key and an empty dictionary to the parent dictionary
                parent[key] = {}
                # Push the key to the stack
                stack.append(key)
        # If the line does not start with a hash sign, it is a value
        else:
            # Get the last key from the stack
            key = stack[-1]
            # Get the parent dictionary by traversing the output dictionary using the stack
            parent = output
            for k in stack[:-1]:
                parent = parent[k]
            # Assign the line as the value to the key in the parent dictionary
            parent[key] = line
    return output


markdown = [
    "# name",
    "Alice",
    "# role",
    "warrior",
    "# weapon",
    "## type",
    "sword",
    "## quality",
    "fine",
    "## damage",
    "### type",
    "slash",
    "### amount",
    "1",
    "# armor",
    "## type",
    "leather",
    "## quality",
    "fine",
]

result = parse_markdown(markdown)
print(result)
