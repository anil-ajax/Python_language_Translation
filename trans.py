from googletrans import Translator
translator = Translator()
t = translator.translate('veritas lux mea', src='la', dest='en')
print(t) // t.text 