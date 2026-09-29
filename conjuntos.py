# O que são conjuntos?
# O conjunto é uma estrutura de dados que armazena elementos únicos e sem nenhuma ordem fixa. 
# Ele funciona como um filtro automático que impede a entrada de dados
# duplicados e foca apenas em saber se um item existe ou não na coleção.
# Graças a um mecanismo interno de busca instantânea, ele encontra, adiciona 
# ou remove informações de forma muito mais rápida do que uma lista tradicional,
# sendo a escolha ideal para eliminar repetições e realizar cruzamentos lógicos de dados.


# Alunos matriculados em cada curso
python = {"Ana", "Bruno", "Carlos"}
data_science = {"Carlos", "Daniela", "Eduardo"}

#1. União
# (| ou .union())Junta todos os elementos, eliminando as duplicatas automaticamente.
#  Serve para descobrir todas as pessoas únicas matriculadas em pelo menos um dos cursos.

# Usando o operador |
todos_alunos = python | data_science
print(todos_alunos)

# Resultado: {'Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo'}

# 2. Interseção (& ou .intersection())
# Retorna apenas os elementos que estão presentes em ambos os conjuntos.
#  Serve para descobrir quem está fazendo os dois cursos ao mesmo tempo.

# Usando o operador &
ambos_cursos = python & data_science
print(ambos_cursos)
# Resultado: {'Carlos'}

# 3. Diferença (- ou .difference())
# Retorna os elementos que estão no primeiro conjunto, mas não estão no segundo. 
# Serve para descobrir, por exemplo, quem estuda Python mas não estuda Data Science.

# Usando o operador -
# apenas_python = python - data_science
print(apenas_python)
Resultado: {'Ana', 'Bruno'}

# 4. Diferença Simétrica (^ ou .symmetric_difference())
# Retorna os elementos que estão em um dos conjuntos, mas não em ambos. 
# Ou seja, é o oposto da interseção: mostra os alunos que estão matriculados em apenas um curso.

# Usando o operador ^
um_unico_curso = python ^ data_science
print(um_unico_curso)
# Resultado: {'Ana', 'Bruno', 'Daniela', 'Eduardo'}