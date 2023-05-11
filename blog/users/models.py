import datetime
from django.db import models
import jwt

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=500)
    profile_image_url = models.CharField(max_length=500)
    profile_image = models.ImageField(upload_to='images/profile_images/', blank=True, null=True)
    role = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def check_password(self, password):
        return self.password == password
    
    def get_jwt(self):
        exp = str(datetime.datetime.now() + datetime.timedelta(minutes=60))

        encoded_jwt = str(jwt.encode({"uid": self.id, "username": self.username, "password": self.password, "jwt_exp": exp}, "secret", algorithm="HS256"))
        encoded_jwt = str.replace(encoded_jwt, "b'", "")
        encoded_jwt = str.replace(encoded_jwt, "'", "")        
        
        return encoded_jwt
    
    @staticmethod
    def get_uid_from_token(token):
        payload = jwt.decode(token, "secret", algorithms=["HS256"])
        return payload["uid"]
    
    #Revisar esto
    # def check_jwt(self, token):
    #     try:
    #         payload = jwt.decode(token, "secret", algorithms=["HS256"])
    #     except:
    #         return False
    #     return True
    
    def __str__(self):
        return self.username