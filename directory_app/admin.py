from django.contrib import admin
from .models import Device, Manager, Room, Technician, Ticket, Users
admin.site.register([
    Device,
    Manager,
    Room,
    Technician,
    Ticket,
    Users
])