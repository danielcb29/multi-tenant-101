from companies.models import Company, Domain

# create your public tenant
tenant = Company(schema_name='public',
                name='Colombia Cars')
tenant.save()

# Add one or more domains for the tenant
domain = Domain()
domain.domain = 'localhost'
domain.tenant = tenant
domain.is_primary = True
domain.save()