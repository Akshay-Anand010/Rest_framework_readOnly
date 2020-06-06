from django.db import models

# Create your models here.
DESCRIPTIONS = (
    (0,"Sunny"),
    (1,"Rain"),
    (2,"Cloudy"),
    (3,"Snow")
)

class Description(models.Model):
    #model to describe weather
    weather_description=models.IntegerField(choices=DESCRIPTIONS,default=0)
    temprature=models.FloatField()
    created_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created_on']

    def __str__(self):
        return str(self.created_on)
    