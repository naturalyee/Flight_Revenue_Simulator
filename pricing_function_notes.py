def pricing_function_monte_carlo(days_left, tickets_left, demand_level,tickets_over_days):
    """Sample pricing function"""
    if days_left == 1:
        price = demand_level - tickets_left
    elif days_left == 2:
        if demand_level > 179: 
            price = demand_level - tickets_left
        else:
            price = demand_level - tickets_left/2 
    else:
        if days_left > 12: #check if 12 is the best number
            if demand_level > 186:
                price = demand_level - 8
            else:
                price = demand_level + 1
        elif days_left > 3:
            if tickets_left/days_left > tickets_over_days:
                if demand_level > 169:
                    price = demand_level - 17
                else:
                    price = demand_level + 1
            else:
                if demand_level > 180:
                    price = demand_level - 20
                else:
                    price = demand_level + 1
        #when does this case ever occur?
        else:
            if demand_level > 169:
                price = demand_level - 13 #doesn't consider the number of tickets left
            else:
                #price = demand_level - tickets_left/days_left
                price = demand_level - 1
    return price
