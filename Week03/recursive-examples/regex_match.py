def is_match(s: str, p: str) -> bool:
    if not p:
        return not s
    first_match = bool(s) and (p[0] == s[0] or p[0] == '.')
    if len(p) >= 2 and p[1] == '*':
        return is_match(s, p[2:]) or (first_match and is_match(s[1:], p))
    else:
        return first_match and is_match(s[1:], p[1:])

if __name__ == "__main__":
    tests = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("mississippi", "mis*is*p*.", False)
    ]
    for s, p, expected in tests:
        result = is_match(s, p)
        print(f"is_match('{s}', '{p}') == {result} (expected: {expected})")


# Iterative regex matcher using dynamic programming (DP table)
def is_match_iterative(s: str, p: str) -> bool:
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    dp[0][0] = True

    for j in range(2, len(p) + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] |= dp[i - 1][j]
    return dp[len(s)][len(p)]

if __name__ == "__main__":
    tests = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("mississippi", "mis*is*p*.", False)
    ]
    for s, p, expected in tests:
        result = is_match_iterative(s, p)
        print(f"is_match_iterative('{s}', '{p}') == {result} (expected: {expected})")
