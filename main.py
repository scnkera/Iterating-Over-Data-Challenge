# sales_totals = {
#     "Junior Mints": { "quantity": 100, "price": 2.0 },
#     "Red Vines": { "quantity": 50, "price": 2.5 },
#     "Candy Corn": { "quantity": 0, "price": 0.5 },
#     "Butterfinger": { "quantity": 20, "price": 3.5 },
#     }

def calculate_total_sales(sales_totals):
    total_sum = 0

    if not sales_totals:
        return 0.0

    for candy in sales_totals.values():
        total_sum += candy['quantity'] * candy['price']

    return float(total_sum)
       
def calculate_average_sales(sales_totals):
    candy_quantity = 0

    if not sales_totals:
        return 0.0
    
    calculated_total_sales = calculate_total_sales(sales_totals)

    number_of_candies = len(sales_totals.keys())

    candy_avg_sales = calculated_total_sales / number_of_candies

    return candy_avg_sales



def filter_to_better_than_average_sales(sales_totals):
    pass
    
def ninety_nine_bottles(count, beverage):
    pass
