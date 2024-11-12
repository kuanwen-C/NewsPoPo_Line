from django.http import JsonResponse

# Create your views here.


def test_analysis(request):
    return JsonResponse({"message": "Test analysis endpoint is working!"})
