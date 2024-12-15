from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Programmer

@csrf_exempt
def get_items(request):
    if request.method == 'GET':
        programmers = Programmer.objects.all().values()
        return JsonResponse(list(programmers), safe=False)

@csrf_exempt
def create_item(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nickname = data.get('nickname')
            if not nickname:
                return JsonResponse({"error": "Nickname is required."}, status=400)

            programmer = Programmer(
                fullname=data.get('fullname'),
                nickname=nickname,
                age=data.get('age'),
                is_active=data.get('is_active', True)
            )
            programmer.save()
            return JsonResponse({
                "id": programmer.id,
                "fullname": programmer.fullname,
                "nickname": programmer.nickname,
                "age": programmer.age,
                "is_active": programmer.is_active
            }, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def update_item(request, item_id):
    if request.method == 'PUT':
        try:
            programmer = Programmer.objects.get(id=item_id)
            data = json.loads(request.body)
            programmer.fullname = data.get('fullname', programmer.fullname)
            programmer.nickname = data.get('nickname', programmer.nickname)
            programmer.age = data.get('age', programmer.age)
            programmer.is_active = data.get('is_active', programmer.is_active)
            programmer.save()
            return JsonResponse({
                "id": programmer.id,
                "fullname": programmer.fullname,
                "nickname": programmer.nickname,
                "age": programmer.age,
                "is_active": programmer.is_active
            })
        except Programmer.DoesNotExist:
            return JsonResponse({"error": "Programmer not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def delete_item(request, item_id):
    if request.method == 'DELETE':
        try:
            programmer = Programmer.objects.get(id=item_id)
            programmer.delete()
            return JsonResponse({'message': 'Item deleted'}, status=204)
        except Programmer.DoesNotExist:
            return JsonResponse({"error": "Programmer not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
