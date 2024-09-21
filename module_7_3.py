class WordsFinder:
    def __new__(cls, *args):
        cls.file_names = []
        cls.file_names.append(args)

    def get_all_words(self):
        spisok = WordsFinder.file_names
        for i in range(len(spisok)):
            print(spisok[i])

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
