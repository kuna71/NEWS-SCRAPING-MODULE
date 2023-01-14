import langdetect as ld

text = """Aઆમિર ખાનના બીજા લગ્ન તૂટ્યા, 15 વર્ષ બાદ કિરણ રાવ સાથે લેશે છૂટાછેડા"""
c = (ld.detect(text))
print(c)

a = "this is english"
def IsEnglish(text):
    lang = (ld.detect(text))
    if lang=='en':
        return True
    else:
        return False
