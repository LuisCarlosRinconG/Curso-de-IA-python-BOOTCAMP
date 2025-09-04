#Uso de split

sentence="python,is,fun"

words=sentence.split(",")

print(words)

# uso del join
sentence=["Python","is","fun"]

new_sentence=" ".join(sentence)

print(new_sentence)


#uso de replace

text="Este es un texto de prueba con fraces repetidas en donde se busca remplzar las fraces" \
" repetidas"

new_text=text.replace("fraces","cosas")

print(new_text)


#Uso de strip

prueba="       texto de prueba para limpiar espacios            "

cleaned_prueba=prueba.strip()

print(cleaned_prueba)


#------------------------------------------Expresiones regulares------------------------------------------

import re

texto = "Contact me at 123-456-7890"

digits = re.findall(r"\d+",texto)

print("Estos son tus digitos",digits)


update_text = re.sub(r"\d","X",texto)

print(update_text)