"""
Hai un'aiuola rappresentata da un array di interi chiamato flowerbed, dove:

1 indica che un fiore è già piantato in quella posizione.
0 indica che quella posizione è vuota.
Devi determinare se è possibile piantare n fiori nella lista senza violare le seguenti regole:

I fiori non possono essere piantati in posizioni adiacenti.
Una posizione è valida per piantare un fiore solo se è vuota (0) e se le posizioni immediatamente a sinistra e a destra (se esistono) sono anch'esse vuote o non esistono.

"""


def canPlaceFlowers(flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        found = 0

        for i in range(len(flowerbed)):
            # Quando il precedente buco è vuoto ?
            if flowerbed[i] == 0:
                # Se ho un buco, guardo il precedente e il next per vedere se sono vuoti e se ce li posso mettere
                if (i == 0 or flowerbed[i - 1] == 0):
                    prev_node_is_empty = True = True
                if (i == len(flowerbed) -1 or flowerbed[i+1]==0):
                    next_node_is_empty = True 

                if prev_node_is_empty and next_node_is_empty:
                    flowerbed[i] = 1
                    found += 1
                    if found >= n:
                        return True

        return found >= n

    
if __name__ == '__main__':

    flowerbed = [0,0,1,0,0,0,1,0,0,0,0,0,1,1,1,0] 
    n = 5
    val = canPlaceFlowers(flowerbed, n)
    print(val)
