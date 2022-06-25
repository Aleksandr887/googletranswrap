from googletrans import Translator

content_words = "hello world peace sleep go home python"
content_words_list = ['hello', 'world', 'peace', 'sleep', 'go', 'home', 'python']
content_text = "Hello world. Peace. Sleep go home python."

# TODO: 1. split with multiple sepatators
#       2. split text to sentences
#       3. think about 15k sym limit

class Gtw:
    def __init__(self, content):
        self.words = []
        self.text = str()
        self.translator = Translator()
        if type(content) is list:
            self.words = content
            self.text = " ".join(self.words)
        elif type(content) == str:
            self.text = content
            self.words = content.split(' ')
        print(f'text = {self.text}')
        print(f'words = {self.words}')

    def translate_text(self):
        return self.translator.translate(self.text, dest='ru').text

    def translate_words(self):
        text_word = "\n".join(self.words)
        return self.translator.translate(text_word, dest='ru').text


gtw = Gtw(content_words_list)
print(gtw.translate_words())
