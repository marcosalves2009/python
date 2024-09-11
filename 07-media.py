# elaborar um algotimo que solicita 4 notas ao usuario.
# o programa deve calcular a media e
# verificar se media é igual ou maior que 80.
# se a media for igual ou maior que 80, o programa deve exibir a mensagem 
# "Aprovado" caso contrario exibir a mensagem "Reprovado"


nota1 = float ( input (" digite a nota 1: "))
nota2 = float ( input (" digite a nota 2: "))
nota3 = float ( input (" digite a nota 3: "))
nota4 = float ( input (" digite a nota 4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print (f" a media final obtida {media}")

if (media >= 80):
   print ("aprovado") 
else:
   print ("reprovado")

