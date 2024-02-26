import random 


def get_numbers_ticket(min: int, max: int, quantity: int):

    if type(min) == int and type(max) == int and type(quantity) == int:
        if min >= 1 and max <= 1000 and min < quantity < max:
            set_num = set()
            while len(set_num) < quantity:
                set_num.add(random.randint(min, max))
                
            return sorted(set_num) 
        else:
            print('Невірні дані,' \
            '"min" має бути більшим або рівним 1,' \
            '"max" має бути меншим або рівним 1000 та більшим за "min",' \
            '"quantity" має бути більшим за "min" та меншим за "max"')
            return []
    else:
        print(f'Невірні дані, значення "min", "max" та "quantity" повинні бути цілими числами')
        return []

lottery_numbers = get_numbers_ticket(5, 49, 8)
print("Ваші лотерейні числа:", lottery_numbers)