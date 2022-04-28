import controllers.controller as controller
import models.LinkedList as LinkedList

def main():

    lista = LinkedList()

    while True:
        comandos = input().split(" ")
        tamanho = len(comandos)
    
        if comandos[0].upper() == "RPI":
            if tamanho != 2:
                print("Não foram introduzidos todos os elementos de entrada. ")
            else:
                controller.registar_ao_inicio(comandos[1])
                controller.print_paises()


        elif comandos[0].upper() == "RPF":
            if tamanho !=2:
                print("Não foram introduzidos todos os elementos necessários. ")
            else:
                controller.registar_no_final(lista,comandos[1])
                controller.print_paises()


        elif comandos[0].upper() == "RPDE":
            if tamanho !=3:
                print("Não foram introduzidos todos os elementos necessários.")
            else:
                controller.registar_pais_depois_de_outro(comandos[2], comandos[1])
                print("Não foram introduzidos todos os elementos necessários.")

        
        elif comandos[0].upper() == "RPAE":
            if tamanho !=3:
              print("Não foram introduzidos todos os elementos necessários.") 
            else:
                  controller.registar_pais_antes_de_outro(comandos[2], comandos[1])
                  controller.print_paises()

        
        elif comandos[0].upper() == "RPII":
            if tamanho !=3:
                print("Nao foram introduzidos todos os elementos necessarios.") 
            else:
                controller.registar_pais_no_indice(comandos[2], comandos[1])
                controller.print_paises()


        elif comandos[0].upper() == "VNE":
            if tamanho <1:
               print("Nao foram introduzidos todos os elementos necessarios.") 
            else:
                numero_de_elementos = controller.verificar_numero_de_elementos_na_lista()
                print(f"O numero de elementos são {numero_de_elementos}")


        elif comandos[0].upper() == "VP":
            if tamanho <2:
                print("Nao foram introduzidos todos os elementos necessarios.") 
            else:
                pais = controller.verificar_pais(comandos[1])
                if pais == True:
                    print (f"O país {comandos[1]} encontra-se na lista. ")
                else:
                    print (f"O país {comandos[1]} nao se encontra-se na lista. ")


        elif comandos[0].upper() == "EPE":
            if tamanho <2:
                print("Nao foram introduzidos todos os elementos necessarios.")
            else:
                pais = controller.remover_primeiro_elemento()
                print(f"O pais {pais} foi eliminado da lista") 



        elif comandos[0].upper() == "EUE":
            if tamanho <2:
                print("Nao foram introduzidos todos os elementos necessarios. ")
            else:
                pais = controller.remover_ultimo_elemento()
                print(f"O pais {pais} foi eliminado da lista. ") 
                
        
        elif comandos[0].upper() == "EP":
            if tamanho <1:
                print("Não foram introduzidos todos os elementos necessarios. ")
            else:
                pais = controller.verificar_pais(comandos[1])
                if pais == True:
                    print(f"O pais {comandos[1]} foi eliminado da lista. ")
                else:
                    print(f"O pais {comandos[1]} não se encontra lista. ")
