def all_variants(text):
    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            yield text[i:j]


text = "abc"
generator = all_variants(text)

for variant in generator:
    print(variant)
