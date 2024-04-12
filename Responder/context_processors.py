from .models import Unit, Call


# Context processors made to sent object from database to web page
def unit(request):
    unit_obj = Unit.objects.first()
    return {'unit': unit_obj}


def call(request):
    call_obj = Call.objects.last()
    return {'call': call_obj}
