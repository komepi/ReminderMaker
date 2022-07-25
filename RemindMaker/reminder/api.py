from .models import Reminder as _Reminder
from .models import MileStone as _MileStone

class Reminder():
    @classmethod
    def create(cls, **data):
        reminder = _Reminder(**data)
        reminder.save()

class MileStone():
    @classmethod
    def create(cls):
        pass