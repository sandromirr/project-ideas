from googletrans import Translator

file = open("words.txt","r")
words = file.read().split('\n')

translator = Translator()

translations = translator.translate(words, dest='ka')
for translation in translations:
    print(f"{translation.origin}-{translation.text}")