
def ceaser(s):
    if not s:
        return 0

    max_len = 1

    for i in range(len(s)):
        left, right = i, i 
        while left >= 0 and right < len(s) and s[left] == s[right]:
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
            left -= 1
            right += 1

    return max_len
s = "akontnoknonabcddcba"
print(ceaser(s))