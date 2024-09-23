from cola import Queue
def remove_vowels(queue):
    """
    Elimina todas las vocales de una cola de caracteres.
    
    Args:
        queue (Queue): Una cola de caracteres.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_queue = Queue()

    while queue.size() > 0:
        char = queue.attention()
        if char.lower() not in vowels:
            new_queue.arrive(char)

    return new_queue
# Creamos una cola de caracteres
my_queue = Queue()
my_queue.arrive('H')
my_queue.arrive('o')
my_queue.arrive('l')
my_queue.arrive('a')

#Imprimir la cola original
print("Cola original:")
while my_queue.size() > 0:
    print (my_queue.on_front(), end=" ")
    my_queue.move_to_end()
print()

# Eliminamos las vocales de la cola
new_queue = remove_vowels(my_queue)

# Imprimimos los elementos de la nueva cola
print ("Cola sin vocales:")
while new_queue.size() > 0:
    print(new_queue.attention(), end=" ")
print()
