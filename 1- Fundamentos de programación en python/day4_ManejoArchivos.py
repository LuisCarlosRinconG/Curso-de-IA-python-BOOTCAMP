
with open("sample.txt","w") as file:
    file.write("Hello world ")
    file.writelines(["Alice ","Bob ","Cherry "]) #Escribira en diferentes lineas


try:
    with open("sample.txt","r") as file:
        content=file.read()
except FileNotFoundError:
    print('Archivo no encontrado')


#Ejercicio

# Contar palabras y lineas en iun archivo

def count_words_and_lines(filename):
    try:
        with open(filename,"r") as file:
            lines=file.readlines()
            linecount=len(lines)
            word_count=sum(len(line.split()) for line in lines)
            print(f"Number of lines:{linecount}")
            print(f"Number of words:{word_count}")
    except FileNotFoundError:
        print(f"File {filename} not found")
    
count_words_and_lines("sample.txt")

