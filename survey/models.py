from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100, blank=True)
    age = models.DateField(blank=True)
    specialite = models.CharField(max_length=100,blank=True)
    language = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.fullname




class Stimul_slov(models.Model):
    stimulus = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return "%s" % ( self.stimulus)

class Otvet(models.Model):
    answer = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(Profil, on_delete=models.CASCADE)
    stimul = models.ForeignKey(Stimul_slov, on_delete=models.CASCADE)
    def __str__(self):
        return  "%s: %s ----> %s" % (self.user ,self.stimul, self.answer)




