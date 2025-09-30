# src/simplify.py

def simplify_path(path: str) -> str:
    """
    Simplify a Unix-style absolute path.
    """
    parts = path.split('/')
    stack = []

    for part in parts:
        if part == '' or part == '.':
            continue
        elif part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)

    return '/' + '/'.join(stack)
