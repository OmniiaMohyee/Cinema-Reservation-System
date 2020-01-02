from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if (postData['first_name'].isalpha()) == False:
            if len(postData['first_name']) < 2:
                errors['first_name'] = "First name can not be shorter than 2 characters"

        if (postData['last_name'].isalpha()) == False:
            if len(postData['last_name']) < 2:
                errors['last_name'] = "Last name can not be shorter than 2 characters"

        if (postData['user_name'].isalpha()) == False:
            if len(postData['user_name']) < 2:
                errors['user_name'] = "user name can not be shorter than 2 characters"
        
        if (postData['user_type'] != "admin" and postData['user_type'] != "customer"):
            errors['user_type'] = "user type can be either admin or customer, all in lower-case."

        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"

        if len(postData['password']) < 8:
            errors['password'] = "Password is too short!"

        return errors

class User(models.Model):

    user_name = models.CharField(unique= True,max_length=30, default= "")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(primary_key= True,max_length=255, unique = True)
    password = models.CharField(max_length=255)
    birthdate = models.DateField(null = True)
    user_type = models.CharField(max_length=5, default="customer")
    is_anonymous = models.BooleanField(default= False)
    is_authenticated = models.BooleanField(default= True)
    

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()



    REQUIRED_FIELDS = ["birthdate","user_type"]
    USERNAME_FIELD = 'user_name'

    

    def __getitem__(self,key):
        return getattr(self,key)

    def __str__(self):
        return self.user_name


class Screen(models.Model):
    screen_number = models.IntegerField(primary_key= True,unique = True)
    rows = models.IntegerField(default = 0)
    columns = models.IntegerField(default = 0)

class Movie(models.Model):
    movie_name = models.CharField(max_length=255)
    duration = models.IntegerField(default = 0)
    genre = models.CharField(max_length=30, null = True)
    movie_id = models.IntegerField(unique= True, primary_key= True, default= 0)
    screen_number = models.IntegerField(default = 0)

class Movie_screenTime(models.Model):
    moviee_id = models.IntegerField(default= 0 )
    screen_time_id = models.IntegerField(default = 0,primary_key=True)
    
    time = models.TimeField(null = True)

class screeing_seats(models.Model):
    screen_time_id = models.IntegerField(default=0 )
    seat_number = models.IntegerField(default = 0)
    taken = models.BooleanField(default = False)



    
