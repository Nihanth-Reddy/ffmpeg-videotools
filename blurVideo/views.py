from multiprocessing import reduction
import time
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .tasks import blur_video_task


@csrf_exempt
def blur_video(request):
    if request.method == "POST":
        # Handles the Post request
        body = json.loads(request.body)
        
        timestamps = body.get("timestamps")
        file_path = body.get("file_path")
        notification_email = body.get("notification_email")

        if timestamps and file_path and notification_email:
            # Creates a celery task for blurring the video
            response = blur_video_task.delay(timestamps, file_path, notification_email)
            return HttpResponse(f"Request is being proceed with id: {response.id}")
        else:
            # Returns Bad request error if any of the required parameters are missing
            response = HttpResponse("Please pass all required parameters")
            response.status_code = 400
            return response
    else:
        # Rejects all other Http Methods
        response = HttpResponse("Request method is not supported")
        response.status_code = 405
        return response
