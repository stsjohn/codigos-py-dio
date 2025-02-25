nota1 = float (5.5)
nota2 = float (9.4)
nota3 = float (6.8)
somaNotas= nota1 + nota2 + nota3

mediaFinal = somaNotas / 3
print(f"A média das notas {nota1}, {nota2} e {nota3} é {mediaFinal:.2f}")
 
if mediaFinal >= 6:
    print('o aluno esta APROVADO')

else:
    print('o aluno esta REPROVADO')