from googletrans import Translator
from re import sub

content_words = "hello world !peace, sleep? go home python???"
content_words_list = ['hello', 'world', 'peace', 'sleep', 'go', 'home', 'python']
content_text = "Hello world. Peace. Sleep go home python."


# TODO: 1. split with multiple sepatators
#       2. split text to sentences
#       3. think about 15k sym limit

class Gtw:
    def __init__(self, content, sep=" "):
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
            self.__translate = self.__translate_text()
        print(f'text = {self.__text}')
        print(f'words = {self.__words}')

    def get_translate(self):
        return self.__translate

    def __translate_text(self):
        return self.__translator.translate(self.__text, dest='ru').text

    def __translate_words(self):
        text_word = "\n".join(self.__words)
        return self.__translator.translate(text_word, dest='ru').text.split('\n')

    def __del_separators(self, seps=None):
        self.__text = sub("[^a-zA-Z ]", "", self.__text)
        self.__words = [sub("[^a-zA-Z ]", "", i) for i in self.__words]


gtw = Gtw(content_words)
print(gtw.get_translate())
