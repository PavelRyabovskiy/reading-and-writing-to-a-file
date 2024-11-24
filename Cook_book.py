def get_shop_list_by_dishes(dishes, person_count):
    cook_book = {}
    shop_list = {}
    
    with open('recipes.txt', 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_line = file.readline().strip().split(' | ')
                ingredient_name = ingredient_line[0]
                quantity = int(ingredient_line[1])
                measure = ingredient_line[2]
                ingredients.append((ingredient_name, quantity, measure))
            cook_book[dish_name] = ingredients
            file.readline()
    
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient[0]
                quantity = ingredient[1] * person_count
                measure = ingredient[2]

                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {
                        'measure': measure,
                        'quantity': quantity
                    }
                else:
                    shop_list[ingredient_name]['quantity'] += quantity
       
    return shop_list
result = get_shop_list_by_dishes(['Утка по-пекински', 'Фахитос'], 2)

for ingredient, details in result.items():
        print(f"{ingredient}: {details['quantity']} {details['measure']}")