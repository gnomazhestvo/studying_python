def get_order(customer_name, *items, **details):
    """получение деталей заказа"""
    order = {
        'customer' : customer_name,
        'items' : items,
        'details' : details,
    }
    return order

def print_order(order):
    """вывод информации о заказе"""
    print(f'Заказ для {order['customer'].title()}:')
    
    print(' Позиции:', end = ' ')   
    order_items = order['items']
    for i in range(len(order_items)):
        if i == len(order_items) - 1:
            print(f'{order_items[i]}')
        else:
            print(f'{order_items[i]},', end = ' ')

    if order['details']:
        for key, value in order['details'].items():
            print(f' {key}: {value}')
    else:
        print(' без дополнительных параметров')
    print()