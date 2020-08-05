from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Car_Model(models.Model):
    """Model representing a car."""
    name = models.CharField(max_length=200, help_text='Enter a car model name(e.g. Benz)')
    img = models.ImageField()
    code = models.CharField(max_length=50, blank=True)
    state = models.BooleanField(help_text='Enter 0 or 1.(1=normal,0=delete)')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Car_User(models.Model):
    """Model representing the a instance of car model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    carModel = models.OneToOneField(Car_Model, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    mac = models.CharField(max_length=50)
    state = models.IntegerField()

    class Meta:
        ordering = ['date', 'id']

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('car-user', args=[str(self.id)])

class Riding_Info(models.Model):
    car = models.ForeignKey(Car_User, on_delete=models.CASCADE)
    startDate = models.DateTimeField(auto_now_add=True)
    endDate = models.DateTimeField()
    speed = models.CharField(max_length=50)
    mileage = models.CharField(max_length=50)
    electric = models.CharField(max_length=50)
    lat = models.CharField(max_length=50)
    lon = models.CharField(max_length=50)
    CAR_STATUS = (
        ('s', 'Start'),
        ('e', 'End')
    )
    state = models.CharField(
        max_length=1,
        choices=CAR_STATUS,
        blank=True,
        default='s',
        help_text='State of Car',
    )
    averageSpeed = models.IntegerField(default=0)
    time = models.DateTimeField(help_text="riding time")
    highSpeed = models.CharField(max_length=50)

    class Meta:
        ordering = ['startDate', 'endDate']
    
    def __str__(self):
        return '%d %s' % (self.id, self.car.user.username)

class Riding_His_Info(models.Model):
    riding = models.OneToOneField(Riding_Info, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return '%d %s' % (self.id, self.riding.car.user.username)

class Car_Check(models.Model):
    car = models.OneToOneField(Car_User, on_delete=models.CASCADE)
    type = models.CharField
    date = models.DateTimeField()
    result = models.CharField(max_length=50)

    class Meta:
        ordering = ['date', 'id']
    
    def __str__(self):
        return '%d %s' % (self.id, self.car.user.username)

class Startup_Img(models.Model):
    img = models.ImageField()
    type = models.CharField(max_length=10)
    date = models.DateField(auto_now=True)
    state = models.CharField(max_length=10)

    class Meta:
        ordering = ['date', 'id']

    def __str__(self):
        return '%d' % (self.id)

class Riding_Statistics(models.Model):
    car = models.OneToOneField(Car_User, on_delete=models.CASCADE)
    average_speed = models.IntegerField()
    duration = models.DurationField()
    max_speed = models.CharField(max_length=50)
    date = models.DateTimeField()

    class Meta:
        ordering = ['car', 'date']
    
    def __str__(self):
        return f'Riding Statistics of {self.car.user.username} created at {self.date}'

class Sms_Codes(models.Model):
    phone_number = PhoneNumberField(primary_key=True)
    code = models.CharField(max_length=10)
    send_date = models.DateTimeField()
    status = models.IntegerField()

    def __str__(self):
        return f'send {code} to {phone_number} at {send_date}'

class System_Config(models.Model):
    name = models.CharField(max_length=64)
    value = models.CharField(max_length=255)
    express = models.CharField(max_length=4096, blank=True)
    type = models.IntegerField()
    note = models.CharField(max_length=4096, blank=True)
    status = models.BooleanField()

    def __str__(self):
        return f'{name}:{value}'



