from itertools import combinations
def all_variants(text):
    for length in range(len(text) + 1):
        for combination in combinations(text, length):
            yield ''.join(combination)

text = "abc"
generator = all_variants(text)

for variant in generator:
    print(variant)
