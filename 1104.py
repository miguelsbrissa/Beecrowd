a, b = map(int, input().split())
diff = [0,0]
while a != 0 or b != 0:
    #Sets{} em python n permitem items repetidos dai n precisa lidar com eles
    cards_a = {int(card) for card in input().split()}
    cards_b = {int(card) for card in input().split()}
    
    #Conjuntos com as cartas  diferentes de A pra B e de B pra A
    diff_cards1 = cards_a.difference(cards_b)
    diff_cards2 = cards_b.difference(cards_a)
   
    #Imprime o tamanho do menor conjunto de cartas diferentes
    print(min(len(diff_cards1), len(diff_cards2)))
    
    a, b = map(int, input().split())
    diff = [0,0]