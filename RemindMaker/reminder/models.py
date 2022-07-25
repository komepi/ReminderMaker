from django.db import models

# Create your models here.
class TimeStamp(models.Model):
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
class MileStone(TimeStamp):
    mile_list = models.JSONField()
    # mile_list={Reminder.id:sort_num}

class Reminder(TimeStamp):
    title = models.CharField(max_length=200)
    is_notification = models.BooleanField(
        default=False
    )
    notifications = models.JSONField(
        null=True
    )
    deadline = models.DateField(
        blank=True,
        null=True
    )
    detail = models.TextField(
        blank=True,
        null=True
    )
    milestones = models.ForeignKey(MileStone, on_delete=models.CASCADE, null=True)
    is_achieve = models.BooleanField(
        default=False
    )
    achieve_date = models.DateTimeField(
        blank=True,
        null=True
    )
    def __str__(self):
        return self.title

    