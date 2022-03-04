from typing import List, Optional


def osa_distance(a: str, b: str) -> int:
    """
    Implements [optimal string alignment distance](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)
    """
    length_a = len(a)
    length_b = len(b)
    # Builds 2d "Array" with 0 except for [i, 0] = i and [0, j] = j
    d: List[List[int]] = [[0] * (length_b + 1) for _ in range(0, length_a + 1)]
    for i in range(0, length_a+1):
        d[i][0] = i
    for j in range(1, length_b+1):
        d[0][j] = j

    for i in range(1, length_a + 1):
        for j in range(1, length_b + 1):
            if a[i-1] == b[j-1]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(d[i-1][j] + 1, # deletion
                          d[i][j-1] + 1, # insertion
                          d[i-1][j-1] + cost) # substitution
            if i > 1 and j > 1 and a[i-1] == b[j-2] and a[i-2] == b[j-1]:
                d[i][j] = min(d[i][j],
                              d[i-2][j-2] + 1) # transposition

    return d[length_a][length_b]

if __name__=='__main__':

    distance = osa_distance('haj', 'kaj')
    print(f'osa-distance("haj", "kaj") = {distance}')
    assert distance == 1

    distance = osa_distance('mig', 'dig')
    print(f'osa-distance("mig", "dig") = {distance}')
    assert distance == 1

    distance = osa_distance('hej', 'dejen')
    print(f'osa-distance("hej", "dejen") = {distance}')
    assert distance == 3

    # Test case from Wikipedia
    distance = osa_distance('ca', 'abc')
    print(f'osa-distance("ca", "abc") = {distance}')
    assert distance == 3
