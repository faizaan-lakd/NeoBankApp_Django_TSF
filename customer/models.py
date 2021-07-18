from django.db import models

# Create your models here.
class customerDetail(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    balance = models.FloatField()

    def __str__(self):
        return self.name


class transferDetail(models.Model):
    timestamp = models.DateTimeField(auto_now_add = True, null=True)
    sender = models.ForeignKey(customerDetail, on_delete=models.CASCADE, related_name='sender')
    reciever = models.ForeignKey(customerDetail, on_delete=models.CASCADE, related_name='reciever')
    amount = models.FloatField()