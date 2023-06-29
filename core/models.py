from django.db import models
from django.contrib.auth import get_user_model #here we are basically importing the model for getting the authenticated user
import uuid
from datetime import datetime 

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE) #this conne cts our profile model with user model of the django setup. 
    id_user = models.IntegerField() #the user id that will be generated is of integer type
    bio = models.TextField(blank=True) #the bio is a textual field
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png') # what this line of code does is that it makes a folder called profile pictures when the photo is added and if it is not added it gives the default profile picture
    location = models.CharField(max_length=100, blank=True) #character field with a maximum length of 100 characters and a blank field is allowed

    def __str__(self):
        return self.user.username # the following line of code is used to return this content as a string
    

    ## now we will migrate to this created model to our database. for this we use the command "python manage.py makemigrations"
    ## The above command will save the migrations locally. "python manage.py migrate" And this command on this line will make the migrations in the database.
    ## "python manage.py createsuperuser" the following line will create a super user which means that this user can access the admin panel. 
    ##

class Post(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    user=models.CharField(max_length=100)
    image=models.ImageField(upload_to='post_images')
    caption=models.TextField()
    created_at=models.DateTimeField(default=datetime.now)
    no_of_likes =models.IntegerField(default=0)

    def __str__(self):
        return self.user

class LikePost (models.Model):
    post_id=models.CharField(max_length=500)
    username=models.CharField(max_length=100)

    def __str__(self):
        return self.username