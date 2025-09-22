from celery import Celery
import os 


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjRedCleDockerJenkins2.settings")


app=Celery("DjRedCleDockerJenkins2")
app.config_from_object('django.conf:settings',namespace='CELERY')
app.autodiscover_tasks()

# 
from datetime import timedelta
from celery.schedules import crontab


app.conf.beat_schedule={
    "call-every-10-seconds":{
        "task":"app.tasks.visit_cache",
        # "schedule":crontab(minute='*/1') 
        "schedule":timedelta(seconds=10)
    }
}