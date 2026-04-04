def printing_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Печатается: {current_design}')
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print('\nНапечатаны: ')
    for completed_model in completed_models:
        print(completed_model)