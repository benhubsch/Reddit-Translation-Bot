from googletrans import Translator

def translate(text, target):
    translator = Translator()
    translation = translator.translate(text, dest=target)
    return translation.text

if __name__ == '__main__':
    # print(translate("Bob is a mean human being.", "es")
