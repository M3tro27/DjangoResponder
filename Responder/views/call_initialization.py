import json
from django.http import JsonResponse
from Responder.models import Call, Machinery
from django.views.decorators.csrf import csrf_exempt


# Parsing JSON
def json_parsing(data):
    call = Call(
        inc_level=data['level'],
        date=data['date'],
        time=data['time'],
        inc_type=data['type'],
        inc_subtype=data['subtype'],
        city=data['city'],
        address=data['address'],
        place_desc=data['place_description'],
        inc_desc=data['call_description']
    )

    call.save()
    # Adding trucks to call object
    machinery = data['machinery']
    for machine_mark in machinery:
        truck = Machinery.objects.get(mark=machine_mark)
        call.trucks.add(truck)


# Receiving call
@csrf_exempt
def receive_call_initialization(request):
    if request.method == 'POST':
        try:
            received_data = json.loads(request.body)
            json_parsing(received_data)
            return JsonResponse({"status": "success", "message": "JSON received successfully"})
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON"})
    else:
        return JsonResponse({"status": "error", "message": "Only POST requests are allowed"})
