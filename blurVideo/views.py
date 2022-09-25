from multiprocessing import reduction
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .tasks import blur_video_task


@csrf_exempt
def blur_video(request):
    if request.method == "POST":
        print("Json: \n", json.loads(request.body))
        body = json.loads(request.body)
        blur_video_task.delay(body["timestamps"], body["notification_email"])
        return HttpResponse("Request Received")
    else:
        response = HttpResponse()
        response.status_code = 405
        return response

# Create your views here.
