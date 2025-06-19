def generate_parentheses(n: int):
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)
    result = []
    backtrack('', 0, 0)
    return result

if __name__ == "__main__":
    print("generate_parentheses(3):", generate_parentheses(3))


# Iterative version using a stack (less elegant, more complex)
def generate_parentheses_iterative(n):
    stack = [("", 0, 0)]
    result = []
    while stack:
        s, left, right = stack.pop()
        if len(s) == 2 * n:
            result.append(s)
        if left < n:
            stack.append((s + '(', left + 1, right))
        if right < left:
            stack.append((s + ')', left, right + 1))
    return result

if __name__ == "__main__":
    print("generate_parentheses_iterative(3):", generate_parentheses_iterative(3))
