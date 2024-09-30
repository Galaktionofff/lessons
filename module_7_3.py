class WordsFinder:
    def __init__(self, *args:str):
        self.file_names = []
        for i in range(len(args)):
            s = str(args[i])
            self.file_names.append(s)

    def get_all_words(self):
        all_words = {}
        for i in range(len(self.file_names)):
            text = self.file_names[i]
            with open(text, 'r') as file:
                text1 = file.read()
                isk = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for x in range(len(isk)):
                    iskl = isk[x]
                    text1 = text1.replace(iskl, '')
                text1 = text1.lower()
                text1 = text1.split()
                all_words[text]=text1
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = WordsFinder.get_all_words(self)
        find = {}
        for i in range(len(self.file_names)):
            for val in range(len(all_words[self.file_names[i]])):
                values = all_words[self.file_names[i]]
                if values[val] == word:
                    find[self.file_names[i]]=val+1
                    break
                else:
                    continue
        return find

    def count(self, word):
        word = word.lower()
        all_words = WordsFinder.get_all_words(self)
        count = {}
        c = 0
        for i in range(len(self.file_names)):
            for val in range(len(all_words[self.file_names[i]])):
                values = all_words[self.file_names[i]]
                if values[val] == word:
                    c += 1
                    continue
                else:
                    continue
            count[self.file_names[i]] = c
        return count

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))
