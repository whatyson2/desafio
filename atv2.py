def verificar(texto):
   
    texto_minusculo = texto.lower()

    cont = texto_minusculo.count('a')

    if cont > 0:
        return f"A letra 'a' aparece {cont} vez(es) na palavra."
    else:
        return "A letra 'a' não aparece na palavra."

# Exemplo
string_informada = input("Informe uma palavra: ")
resultado = verificar(string_informada)
print(resultado)
