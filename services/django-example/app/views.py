from django.http import JsonResponse, HttpRequest


def view_root(request: HttpRequest) -> JsonResponse:
    return JsonResponse({
        'service': 'django-example',
        'version': '0.1.0',
    })
