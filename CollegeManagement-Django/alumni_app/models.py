from django.db import models

# Create your models here.


from django.db import models

class Registration(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=50)
    profile_pic = models.ImageField()
    address = models.TextField()
    rollno = models.CharField(max_length=10)
    graduation_year = models.IntegerField()
    major = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    current_employer = models.CharField(max_length=50)
    current_job_title = models.CharField(max_length=50)
    contact = models.CharField(max_length=20, blank=True)
    email = models.EmailField(verbose_name="email address", max_length=60, unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()


class Meeting(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    link = models.URLField()



class JobNotification(models.Model):
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    posted_date = models.DateField()
    description = models.TextField()
    apply_link = models.URLField()

    def __str__(self):
        return self.job_title



class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name



class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comments = models.TextField()

    def __str__(self):
        return self.name  # This is just for a human-readable representation in the admin panel
