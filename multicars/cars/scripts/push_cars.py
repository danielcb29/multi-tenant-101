from django_tenants.utils import schema_context
from cars.models import Car

cars_by_company_info = [
    {
        'domain': 'ford',
        'cars': [
            {
                'model': 'Fiesta',
                'year': '2018',
                'color': 'Red',
                'stock': 10
            },
            {
                'model': 'Fusion',
                'year': '2018',
                'color': 'Blue',
                'stock': 2

            },
            {
                'model': 'Escape',
                'year': '2017',
                'color': 'Black',
                'stock': 5

            },
            
        ]
    },
    {
        'domain': 'mazda',
        'cars': [
            {
                'model': 'Mazda 3',
                'year': '2019',
                'color': 'Red',
                'stock': 20

            },
            {
                'model': 'CX5',
                'year': '2018',
                'color': 'White',
                'stock': 9

            },
            {
                'model': 'Mazda 2',
                'year': '2019',
                'color': 'Blue',
                'stock': 6

            },
        ]
    },
    {
        'domain': 'chevrolet',
        'cars': [
            {
                'model': 'Spark GT',
                'year': '2019',
                'color': 'Grey',
                'stock': 50

            },
        ]
    },
    {
        'domain': 'bmw',
        'cars': [
            {
                'model': 'BMW Serie 1',
                'year': '2019',
                'color': 'Blue',
                'stock': 5

            },
            {
                'model': 'BMW X6',
                'year': '2019',
                'color': 'Green',
                'stock': 2

            },
        ]
    }
]

for company_cars_info in cars_by_company_info:
    with schema_context(company_cars_info['domain']):
        for car_info in company_cars_info['cars']:
            car = Car(model=car_info['model'], year=car_info['year'], color=car_info['color'], stock=car_info['stock'])
            car.save()