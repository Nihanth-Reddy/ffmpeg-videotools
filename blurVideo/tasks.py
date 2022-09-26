from time import time
from celery import shared_task
from celery.utils.log import get_task_logger

from .blur import blur_video
from .email import send_email

logger = get_task_logger(__name__)

@shared_task(name="blur_video")
def blur_video_task(timestamps: list, file_path:str, email: str):
    logger.info(f"List of timestamps are: {timestamps}")
    blur_video(timestamps, file_path)
    logger.info("Video processing is completed. Initiating email notification")
    send_email(email)
    logger.info("Email notification is sent")
