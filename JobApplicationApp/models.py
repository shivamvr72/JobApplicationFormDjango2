from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Create your models here.
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number format: '+999999999'. Up to 15 digits allowed.")
class User(AbstractUser):
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    def __str__(self):
        return f"{self.username}"
    

# form models
class BasicDetails(models.Model):
    rel_status = (
        ("single", "single"),
        ("married", "married")
    )
    GENDER_CHOICES =( 
        ('male','Male'),
        ('female','Female'),
    )
 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    birth_date = models.DateField()
    relationship = models.CharField(max_length=15, choices=rel_status, null=True, blank=True)
    city = models.CharField(max_length=50)
    address1 = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150, null=True, blank=True)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.user_id} {self.first_name} {self.last_name}"


class EducationDetails(models.Model):
    form_id = models.ForeignKey(BasicDetails, on_delete=models.CASCADE)
    education_authority = models.CharField(max_length=100)
    course = models.CharField(max_length=30)
    passing_year = models.CharField(max_length=4)
    percentage = models.FloatField()

    def __str__(self):
        return f"{self.form_id}"


class WorkExperienceDetails(models.Model):
    form_id = models.ForeignKey(BasicDetails, on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    desingnation = models.CharField(max_length=50)
    from_year = models.CharField(max_length=4)
    to_year = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.form_id}"

# class Languages(models.Model):
#     name = models.CharField(max_length=50)
#     def __str__(self):
#         return f"{self.name}"
    
# class LangaugeAbility(models.Model):
#     isread = models.BooleanField()
#     isspeak = models.BooleanField()
#     iswrite = models.BooleanField()
#     def __str__(self):
#         return f"{self.isread} {self.isspeak} {self.iswrite} "

class LanguagesKnown(models.Model):
    form_id = models.ForeignKey(BasicDetails, on_delete=models.CASCADE)
    langauage = models.CharField(max_length=30)
    isread = models.BooleanField()
    isspeak = models.BooleanField()
    iswrite = models.BooleanField()

    def __str__(self):
        return f"{self.form_id}"


class TechnologiesKnown(models.Model):
    STATUS_CHOICE = (
        ("begginer", "Begginer"),
        ("mediator", "Mediator"),
        ("expert", "Expert")
    )

    form_id = models.ForeignKey(BasicDetails, on_delete=models.CASCADE)
    technology = models.CharField(max_length=30)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, null=True, blank=True)

    def __str__(self):
        return f"{self.form_id}"


class References(models.Model):
    form_id = models.ForeignKey(BasicDetails, on_delete=models.CASCADE)
    rname = models.CharField(max_length=30)
    rphone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    relation = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.form_id}"


class Preferences(models.Model):
    form_id = models.OneToOneField(BasicDetails, on_delete=models.CASCADE)
    pref_location = models.CharField(max_length=50)
    notice_period = models.CharField(max_length=10)
    department = models.CharField(max_length=50)
    expected_ctc = models.IntegerField()
    actual_ctc = models.IntegerField()

    def __str__(self):
        return f"{self.form_id}"


class State(models.Model):
    name = models.CharField(max_length=100)

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')
