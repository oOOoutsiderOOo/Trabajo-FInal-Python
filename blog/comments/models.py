from django.db import models

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    response_to = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    is_response = models.BooleanField(default=False)
    
    def __str__(self):
        return self.content