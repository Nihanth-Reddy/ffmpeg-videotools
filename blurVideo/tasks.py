from time import time
from celery import shared_task
from celery.utils.log import get_task_logger

from .blur import blur_video

logger = get_task_logger(__name__)

@shared_task(name="blur_video")
def blur_video_task(timestamps: list):
    logger.info(f"List of timestamps are: {timestamps}")
    return blur_video(timestamps)