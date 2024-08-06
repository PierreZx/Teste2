def capitalizar_string(s):
    return s.capitalize()
def inverter_string(s):
    return s[:: -1]
def contar_vogais(s):
    vogais = 'aeiouAEIOU'
    return sum(1 for caractere in s if caractere in vogais)