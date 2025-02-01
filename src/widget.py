import masks
from typing import Union


def mask_account_card(tip_number_cart:Union[str,int]) -> str:
    digit_card = ''
    alpha_card = ''
    list_number = tip_number_cart.split()
    #print(list_number)

    #if 'Maestro' in list_number or 'Visa' in list_number:
    if ' '.join(list_number[:2]) == 'Visa Platinum' or 'Maestro' in list_number:
        for i in list_number:
            if i.isalpha():
                alpha_card += i + ' '
                #alpha_card.append(i)

            elif i.isdigit():
                digit_card += i
            shifr_card = masks.get_mask_card_number(digit_card)

    elif 'Счет' in list_number:
        for i in list_number:
            if i.isalpha():
                alpha_card += i
            elif i.isdigit():
                digit_card += i
            shifr_card = masks.get_mask_account(digit_card)


    return f'{alpha_card} {shifr_card}'

print(mask_account_card('Visa Platinum 7000792289606361'))
