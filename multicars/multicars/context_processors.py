def company(request):
    if hasattr(request, 'tenant'):
        return { 'company': request.tenant }
    return {}
