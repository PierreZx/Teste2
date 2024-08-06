from operacoes_matematicas import soma, subtrair, nultiplicar, dividir
from manipulacao_strings import capitalizar_string, inverter_string, contar_vogais
from utilitarios_data_hora import data_hora_atual, formatar_data

def principal():
    print('Operações matemáticas: ')
    print('somar: 2 + 3 =', soma(2, 3))
    print('Subtrair: 5 - 2 =', subtrair(5,2))
    print('Multiplicar: 4 * 3 =', nultiplicar(4, 3))
    print('Dividir: 10 / 2 = ', dividir(10, 2))

print('\nManipulação de Strings: ')
print('Capitalizar: ola =', capitalizar_string('ola'))
print('Inverter: "python" =', inverter_string('python'))
print('Contar vogais: "ola mundo" =', contar_vogais('ola mundo'))

print('\nUtilitários de data e hora: ')
agora = data_hora_atual()
print('data e hora atual:', agora)
print('Data formatada:', formatar_data(agora, '%d/%m/%y'))

if __name__ == '__main__':
    principal()