from bisseccao import *
from newton_raphson import *
from falsa_posicao import *

print("metodo da bisseccao [1]\nmetodo da falsa posicao [2]\nmetodo de newton raphson [3]\n")
metodo = int(input('escolha um metodo: '))

if metodo == 1:
    bisseccao.main()
    
elif metodo == 2:
    falsa_posicao.main()

elif metodo == 3:
    newton_raphson.main()

