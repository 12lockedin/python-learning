"""
8-15. Side document for exer-8-15
"""

def make_car(manufacturer, model, **extras):
    """Collect information about a car"""
    car_info = {}
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    for k,v in extras.items():
        car_info[k] = v
    return car_info


