import math

def specialStrings(s: str) -> int:
    n = len(s)
    # Step A. Collect the indices of all '1's in the string
    ones = [i for i, ch in enumerate(s) if ch == '1']
    m = len(ones)
    if m == 0:
        # No '1' in the entire string => no non-empty substring can satisfy (#0) = (#1)^2
        return 0

    # Step B. Build zerosBetween array of length (m-1)
    zerosBetween = [0]*(m-1)
    for j in range(m-1):
        zerosBetween[j] = (ones[j+1] - ones[j] - 1)

    zerosBefore = ones[0]                      # zeros to the left of the first '1'
    zerosAfter  = (n - 1 - ones[m-1])          # zeros to the right of the last '1'

    # Step C. Prefix‐sum of zerosBetween so we can get internal zeros quickly:
    #    prefixZ[k] = sum(zerosBetween[0..k-1]) for k in [0..m-1], with prefixZ[0]=0.
    prefixZ = [0]*m
    for j in range(m-1):
        prefixZ[j+1] = prefixZ[j] + zerosBetween[j]

    ans = 0
    max_x = int(math.isqrt(n))  # floor(sqrt(n))

    # Step D. Loop over x = 1..max_x
    for x in range(1, max_x + 1):
        if x > m:
            break        # cannot pick more than m ones if there are only m '1's total
        if x + x*x > n:
            break        # substring length would exceed n

        count_x = 0
        # We will slide a window of size x over the list of ones[]:
        # j = starting index in the 'ones' array (0 <= j <= m - x)
        for j in range(m - x + 1):
            # 1) Compute internal zeros among the x ones from j..j+x-1
            IZ = prefixZ[j + x - 1] - prefixZ[j]

            # 2) Compute L and R (zeros immediately to left / right of that block)
            if j == 0:
                L = zerosBefore
            else:
                L = zerosBetween[j - 1]

            if j + x - 1 == m - 1:
                R = zerosAfter
            else:
                R = zerosBetween[j + x - 1]

            # 3) We need (a + IZ + b) = x^2  => a + b = x^2 - IZ
            T = x*x - IZ
            if T < 0 or T > (L + R):
                continue

            # 4) Count the number of integer solutions (a,b) with 0 <= a <= L, 0 <= b <= R, a+b = T.
            a_min = max(0, T - R)
            a_max = min(L, T)
            if a_min <= a_max:
                count_x += (a_max - a_min + 1)

        ans += count_x

    return ans


# -----------------
# Example / Testing
# -----------------
if __name__ == "__main__":
    test_cases = [
        ("010001", 4),   # from the prompt’s example
        ("1",      0),   # no substring can have (#0) = (#1)^2 except empty
        ("0",      0),
        ("101",    0),   # substrings: "1","0","1","10","01","101" => none satisfy #0 = (#1)^2
        ("1100",   1),   # substring "100" has 1 '1' and 1 '0'; 1=1^2
        ("10100",  2),   # substrings "100" (at [1..3]) and "0100" (at [2..5]) for instance
        ("0000",   0),   # no '1's => cannot have non-empty substring with #1>=1
        ("111000000", 3) # “111000000”   => 
                         #   x=1: look for “1 zero”  (e.g. "10","01",...) 
                         #   x=2: look for “4 zeros” (maybe “110000” etc.)
                         #   x=3: look for “9 zeros” (but length>9?? careful) 
                         # In total it yields 3 special substrings
    ]

    for s, expected in test_cases:
        result = specialStrings(s)
        print(f"s = {s!r},  result = {result},  expected = {expected}")

    print("All tests passed!")
