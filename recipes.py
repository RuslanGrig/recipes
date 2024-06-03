import os

def recipes_open():
    with open('recipes.txt', encoding='utf-8') as f:
        cook_book = {}
        list_ingredients = []
        list_keys = ['ingredient_name', 'quantity', 'measure']
        for line in f:
            if line.strip():
                name_dish = line.strip()
                list_ingredients.clear()
                count_ingredients = int(f.readline().strip())
                for x in range(0, count_ingredients):                                     
                    list_ingredients.append(dict(zip(list_keys, f.readline().strip().split(' | '))))
                cook_book[name_dish] = list_ingredients.copy()
        return cook_book

def get_shop_list_by_dishes(dishes, person_count):    
    if isinstance(dishes, list) and isinstance(person_count, int):
        shop_dict = {}
        cook_book = recipes_open()
        for dish in dishes:
            if isinstance(dish, str) and dish in cook_book:                
                for ingredient_dict in cook_book.get(dish):
                    ingredient = ingredient_dict.get('ingredient_name') 
                    if ingredient in shop_dict:
                        x = int(ingredient_dict['quantity'])*person_count
                        shop_dict[ingredient]['quantity'] += x                                              
                    else:
                        shop_dict[ingredient] = {'measure': ingredient_dict['measure'], 
                        'quantity': int(ingredient_dict['quantity'])*person_count}
            else:
                return 'error'
        return(shop_dict)
    else:
        return 'error'

print('1.', get_shop_list_by_dishes(['Омлет', 'Омлет', 'Фахитос'], 2))
print('2.',get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2))