# PhotoDekh_DJango
The following is a website using DJango. I have earlier made it using MERN but I have used a different tech stack for this one. 

Earlier I made the similar website based on the MERN stack. But as an individual in info tech, we need to keep moving to tools which are more efficient and which are opening a new space in the market.
Based on those lines, I have decided to learn this tech skill via this project. 
It is a photo sharing website. 
The front end is essentially created using JS, HTML and CSS. 

The following will help you clone the given repo:

1) Download the zip files or clone this repositiory.
2) To run the server, you need to implement "python .\manage.py runserver" in your terminal.
3) You can use the following credentials to login and check the functionality:
   a) Username: Ganesh Patil
   b) Password: 123

About the Project:

Authentication:

1) It's implemented from the pre-developed "auth" model in the "django.contrib.auth.models".
2) We have developed the frontend for it using HTML templates and CSS for the styling.
3) Every model that has been created has been well-described in the "models.py" files.
4) To display the model on the admin panel, we register them on the "admin.py" file.

Models implemented:

1) User
2) Profile

The above two kinds of models are interlinked. The foreign key used is the "user_id". The user model is inbuilt and the Profile model is user-defined.

3) Post

The above model holds the details of a post. It answers all the questions related to a post. Like who made the post? What is the content of the posted image? What is the caption of the image? 

4) LikePost

This model is essentially used to hold the likes of a post. It holds the post_id and the "number of likes" associated with a post. 

5) FollowersCount

This model is of the type "followers:following" it has details of both the entities.

 
