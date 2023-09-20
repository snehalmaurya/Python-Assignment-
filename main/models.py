from django.db import models

# Create your models here.
class user(models.Model):

    ROLE_CHOICES = [
        ("Commissioner", "Commissioner"),
        ("Citizen", "Citizen"),
        ("Inspector", "Inspector"),
        ("SubInspector", "SubInspector"),
        ("Constable", "Constable"),
    ]

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other")
    ]

    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='Citizen')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    otp = models.IntegerField(default=1467)
    def __str__(self):
        return f"{self.email} - {self.role}"


class complaint(models.Model):
    FIR_STATUS = [
        ("Done", "Done"),
        ("Pending", "Pending"),
        ("Continue", "Continue")
    ]
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    complaint_msg = models.TextField(null=False)
    status = models.CharField(max_length=50, choices=FIR_STATUS, default="Pending")



class policeStation(models.Model):
    image = models.FileField(upload_to='polices-stations')
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    city = models.CharField(max_length=100)
    pin = models.CharField(max_length=20)
    Address = models.CharField(max_length=500)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class emergency(models.Model):
    image = models.FileField(upload_to='Emergency-logo', default='media\call-default.png')
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)

    def __str__(self):
        return self.name