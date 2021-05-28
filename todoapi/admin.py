from django.contrib import admin
from .models import Task
from .models import Ticket
from .models import note
from .models import piece
admin.site.register(Ticket)
admin.site.register(Task)
admin.site.register(note)
admin.site.register(piece)

