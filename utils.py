import random

def create_random_list(_length):
    if(type(_length) != int):
        raise TypeError('Input must be a positive integer')
    if(_length < 0):
        raise ValueError('Input must be a positive integer')
    in_list = list()
    for i in range(_length):
        in_list.append(random.randint(-1000,1000))
    return in_list




def apply_gestform_processing_to_list(_list):                              #Fonction permettant à partir d'une liste de nombres de tester la divisibilité par 3 et par 5 
    if(type(_list) != list):
        raise TypeError('Input must be a list of integers')
    out_list = list()
    for number in _list:
        if(type(number) != int):
            raise TypeError('Input list must be composed only with integers')
        if(number%3 == 0):                              
            if(number%5 == 0):                          
                out_list.append("Gestform")
            else:
                out_list.append("Geste")
        elif(number%5 == 0):                            
            out_list.append("Forme")
        else:
            out_list.append(str(number))                
    return ', '.join(out_list)                          #On renvoie la liste traitée en séparant les termes par une virgule et un espace
