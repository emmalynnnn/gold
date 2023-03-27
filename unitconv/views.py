from django.shortcuts import render
from django.http import JsonResponse

from unitconv.models import ConversionFactor

def index(request):
    fromParam = request.GET.get('from', '')
    toParam = request.GET.get('to', '')
    valueParam = request.GET.get('value', -1)

    val = validate(fromParam, toParam, valueParam)
    if val == -1:
        response = {
            "error": "Invalid unit conversion request"
        }
        response = JsonResponse(response)
        response['Access-Control-Allow-Origin'] = '*'
        return response

    result = convert(fromParam, toParam, val)
    response = {
        "units": toParam,
        "value": result
    }
    response = JsonResponse(response)
    response['Access-Control-Allow-Origin'] = '*'
    return response

def validate(frm, to, val):
    validUnits = ["T", "g", "t_oz", "kg", "lb", "oz"]
    if not frm in validUnits or not to in validUnits:
        return -1
    if val == "":
        return -1
    try:
        val = float(val)
        return val
    except ValueError:
        return -1

def convert(frm, to, val):
    conFactFrm = ConversionFactor.objects.get(name=frm).to_pounds
    conFactTo = 1 / ConversionFactor.objects.get(name=to).to_pounds

    # print(f"Converting {val} {frm} to {to}")
    lbs = val * conFactFrm
    # print(f"{val} {frm} is {lbs} lbs - with conversion factor {conFactFrm}")
    result = lbs * conFactTo
    # print(f"{lbs} lbs is {result} {to} - with conversion factor {conFactTo}")

    return result
