def contar_vogais(palavras):
    vogais = 'aeiouáéíóúãõâêîôûàèìòù'
    return sum(char.lower() in vogais for palavra in palavras for char in palavra)

print(contar_vogais("programação"))