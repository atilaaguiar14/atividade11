# Desenvolva um programa que pergunte a distâcia de um
# viagem em Km. Calcule o preço da passagem, cobrando 0,50 por Km para
# viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = float(input("digite a distancia de sua viagem em Km"))
if distancia <= 200:
    passagem = 0.5 * distancia
    print(f"o preço da sua viagem sera {distancia * 0.50}.")
else:
    passagem = 0.45 * distancia
    print(f"o preço da sua passagem: R$ {distancia * 0.45}")