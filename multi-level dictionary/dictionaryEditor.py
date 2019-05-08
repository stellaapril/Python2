#Dictionary Traversing

#Vending Machine

machine = {
    'Beverage':
        {
        'coke':{'id':'1','name':'Coca Cola','price':'1.75','size':'20 fl oz'},
        'diet coke':{'id':'2','name':'Diet Coke','price':'1.75','size':'20 fl oz'},
        'sprite':{'id':'3','name':'Sprite','price':'1.75','size':'20 fl oz'},
        'vitaminzero':{'id':'4','name':'Vitamin Water Zero pineapple coconut','price':'2.25'},
        },
    'Snack':
        {
        'Doritos':{'id':'5','name':'Doritos Cheese','price':'1.75','size':'1.25 oz'},
        'Lays':{'id':'6','name':'Lays Chip Classic','price':'1.5','size':'1.5 oz'},
        'Popcorn':{'id':'7','name':'Smartfood Popcorn','price':'1.25','size':'2 oz'},
        'Oreo':{'id':'8','name':'Oreo Cookies Vanilla Cream','price':'1.75','size':'20 fl oz'},

        }
}


def main():
    print('Welcome to Use Vending Machine')

    for type in machine:
        print(type)

    while True:
        userinput = input('Please choose a type')
        if userinput in machine:
            for i in machine[userinput].keys():
                for x in machine[userinput][i]['id']:
                    print(i, ' id: ', x)
            useritem = input('Choose the item')
            break

    while True:
        if useritem in machine[userinput].keys():
            print('--------------------------------------------')
            print('Item Name: ', machine[userinput][useritem]['name'])
            print('Item Price: ', machine[userinput][useritem]['price'])
            print('Item Size: ', machine[userinput][useritem]['size'])
            print('--------------------------------------------')
            break

main()










