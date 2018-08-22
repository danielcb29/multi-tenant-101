from companies.models import Company, Domain

companies_info = [
    {
        'schema_name': 'ford',
        'name': 'Ford',
    },
    {
        'schema_name': 'mazda',
        'name': 'Mazda',
    },
    {
        'schema_name': 'chevrolet',
        'name': 'Chevrolet',
    },
    {
        'schema_name': 'bmw',
        'name': 'BMW',
    }
]

for company in companies_info:
    company_object = Company(schema_name=company['schema_name'], name=company['name'])
    company_object.save()

    domain = Domain()
    domain.domain = '%s.localhost' % company['schema_name']
    domain.tenant = company_object
    domain.is_primary = True
    domain.save()