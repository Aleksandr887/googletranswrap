from googletrans import Translator
from re import sub

content_words = "hello world !peace, sleep? go home python???"
content_words_list = ['hello', 'world', 'peace', 'sleep', 'go', 'home', 'python']
content_text = "Hello world. Peace. Sleep go home python."
file = open("War_And_Peace.txt", 'r')
war_and_peace_text = file.read()
file.close()


# TODO: 1. split with multiple sepatators
#       2. split text to sentences
#       3. think about 15k sym limit

class Gtw:
    def __init__(self, content):
        self.__words = []
        self.__text = str()
        self.__translate = ""
        self.__translator = Translator()
        if type(content) is list:
            self.__words = content
            self.__text = " ".join(self.__words)
            self.__del_separators()
            self.__translate = self.__translate_words()
        elif type(content) is str:
            self.__text = content
            self.__del_separators()
            self.__words = content.split(' ')
            print(len(self.__text))
            if (len(self.__text) > 10_000):
                self.__translate = list()
                self.__translate_in_parts()
            else:
                self.__translate = self.__translate_text()
        print(f'text = {self.__text}')
        print(f'words = {self.__words}')

    def get_translate(self):
        if type(self.__translate) is list:
            return " ".join(self.__translate)
        else:
            return self.__translate

    def __translate_text(self):
        return self.__translator.translate(self.__text, dest='ru').text

    def __translate_words(self):
        text_word = "\n".join(self.__words)
        return self.__translator.translate(text_word, dest='ru').text.split('\n')

    def __del_separators(self, seps=None):
        self.__text = sub("[^a-zA-Z ]", "", self.__text)
        self.__words = [sub("[^a-zA-Z ]", "", i) for i in self.__words]

    def __translate_in_parts(self):
        l_ind = 0
        r_ind = 5_000

        while len(self.__text) - r_ind >= 0 and l_ind != r_ind:
            print(f"r_ind = {r_ind}\nl_ind = {l_ind}\n{len(self.__text[l_ind:r_ind])}")
            self.__translate.append(self.__translator.translate(self.__text[l_ind:r_ind], dest='ru').text)
            l_ind = r_ind
            r_ind = r_ind + 5_000
            if len(self.__text) - r_ind < 0:
                r_ind = len(self.__text)


gtw = Gtw(war_and_peace_text)
print(gtw.get_translate())
