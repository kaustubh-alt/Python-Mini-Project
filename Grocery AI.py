#remove non-ess items from cart and save money

essential = ['Wheat',"Rice",'Sugar','Salt','Jowar','Tea','Peanuts','Spices','Vegetable','Fruit','Poha']
Cart = ['Wheat','Nutella','Jam','Biscute','juice','Vegetable','Spices','Fruit','Poha','Sugar','Rice','Jowar']
Cart_prize = 5790


def sort(list, prize):
    empty = []
    for i in list:
        for j in essential:
            if i == j:
                empty.append(i)
    Dict ={
        "Wheat" : 200,
        'Jowar' : 170,
        'Sugar' : 30,
        'Salt'  : 20,
        'Tea'   : 55,
        'Peanuts':35,
        'Spices': 90,
        'Vegetable':500,
        'Poha'  : 25
    }
    cost = 0
    for i in empty:
        for j in Dict:
            if i == j:
                cost += Dict[j]
    return empty,cost

ess_cart,ess_cost = sort(Cart,Cart_prize)

print('Your Essentials Items :')
for i in ess_cart:
    print(i)
print('\n')
print('Your Expense : '+str(ess_cost)+'\n''Your savings :'+ str(Cart_prize-ess_cost))






