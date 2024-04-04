
from collections import Counter

def min_window(s, t):
    if not s or not t:
        return ""

    freq_t = Counter(t)
    required_chars = len(freq_t)
    satisfied_chars = 0

    start, end = 0, float('inf')
    left = 0

    for right, char in enumerate(s):
        if char in freq_t:
            freq_t[char] -= 1
            if freq_t[char] == 0:
                satisfied_chars += 1

        while satisfied_chars == required_chars:
            if right - left < end - start:
                start, end = left, right

            if s[left] in freq_t:
                freq_t[s[left]] += 1
                if freq_t[s[left]] > 0:
                    satisfied_chars -= 1
            left += 1

    return s[start:end+1] if end != float('inf') else ""

# Example usage:
s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s, t))  # Output: "BANC"
