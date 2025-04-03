"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""
### Funcion con Fors anidados
# def find_first_sum(nums, goal):
#   for n in range(len(nums)):
#     for i in range(n+1,len(nums)):
#       if nums[n] + nums[i] == goal:
#         print([n, i])
#         return ;
#   print(None)

### Funcion con diccionarios
def find_first_sum(nums, goal):
  revisados = {}
  for indice, valor in enumerate(nums):
    numero_buscado = goal - valor
    if numero_buscado in revisados: return [revisados[numero_buscado], indice ]
    revisados[valor] = indice
  return None


nums = [4, 5, 6, 2]
goal = 8

print(find_first_sum(nums, goal))

