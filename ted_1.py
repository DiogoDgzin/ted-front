alturas = []
alturas_homens = []
qtd_mulheres = 0

for pessoa in range(1, 16):
    print(f'nome {pessoa}: ')
    altura = float(input('digite a altura (em metros, ex: 1.30): '))
    genero = input('digite o genero ( (M) para MASCULINO / (F) para FEMININO): ')

    alturas.append(altura)

    if genero == 'M':
        alturas_homens.append(altura)
    elif genero == 'F':
        qtd_mulheres += 1
    else:
        print('Invalido, essa entrada não será contbilazda!')

maior_altura = max(alturas)
menor_altura = min(alturas)

if len(alturas_homens) > 0:
    media_homens = sum(alturas_homens) / len(alturas_homens)
else:
    media_homens = 0

print('   RESULTADOS!   ')
print(f'Maior altura do grupo: {maior_altura: .2f} m')
print(f'Menor altura do grupo: {menor_altura: .2f} m')
print(f'Media de altura dos homens: {media_homens: .2f} m')
print(f'Numero de mulheres: {qtd_mulheres} ')