# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Device(models.Model):
    deviceid = models.IntegerField(primary_key=True)
    operatingsystem = models.CharField(max_length=50, blank=True, null=True)
    modelmodelid = models.IntegerField(blank=True, null=True)
    devicetype = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'device'


class Manager(models.Model):
    managerid = models.IntegerField(primary_key=True)
    techdepartment = models.CharField(max_length=150, blank=True, null=True)
    managername = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manager'


class Room(models.Model):
    roomid = models.IntegerField(primary_key=True)
    roomnumber = models.CharField(max_length=20, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    buildingnumber = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'room'


class Technician(models.Model):
    techid = models.CharField(primary_key=True, max_length=15)
    techname = models.CharField(max_length=100, blank=True, null=True)
    techemail = models.CharField(unique=True, max_length=100, blank=True, null=True)
    managermanagerid = models.ForeignKey(Manager, models.DO_NOTHING, db_column='managermanagerid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'technician'


class Ticket(models.Model):
    ticketid = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    issuetype = models.CharField(max_length=50, blank=True, null=True)
    priority = models.CharField(max_length=20, blank=True, null=True)
    issuedescription = models.CharField(max_length=200, blank=True, null=True)
    dateissued = models.DateField(blank=True, null=True)
    technicianid = models.ForeignKey(Technician, models.DO_NOTHING, db_column='technicianid', blank=True, null=True)
    devicedeviceid = models.ForeignKey(Device, models.DO_NOTHING, db_column='devicedeviceid', blank=True, null=True)
    roomroomid = models.ForeignKey(Room, models.DO_NOTHING, db_column='roomroomid', blank=True, null=True)
    useruserid = models.ForeignKey('Users', models.DO_NOTHING, db_column='useruserid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ticket'


class Users(models.Model):
    userid = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
