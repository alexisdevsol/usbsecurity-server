from django.http import JsonResponse, HttpResponseBadRequest


def geocode(request):
    if not request.is_ajax():
        return HttpResponseBadRequest()

    hour = request.GET.get('hour')

    appearance = request.session.get('appearance')
    if hour and (not appearance or appearance == 'auto'):
        if not appearance:
            request.session['appearance'] = 'auto'
        request.session['appearance_auto'] = 'light' if 6 < int(hour) < 19 else 'dark'

    return JsonResponse({})
