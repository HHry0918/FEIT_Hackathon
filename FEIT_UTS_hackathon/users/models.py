from django.db import models

# class User(models.Model):
    
#     item_name = models.CharField(max_length=120)
#     seller = models.ForeignKey(User, on_delete=models.CASCADE)
#     student_id = models.CharField(max_length=10, default=False)
#     description = models.TextField()
#     date = models.DateTimeField(default=timezone.now)
#     status_verified = models.BooleanField(default=False)
#     price = models.FloatField(default=round(float(0.00),2))
    
#     def __str__(self):
#         return self.item_name
