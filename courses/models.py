from django.db import models

class Course (models.Model):
    name = models.CharField(max_length=30)
    short_description = models.CharField(max_length=600)
    description = models.TextField()
    def  __unicode__(self):
	    return self.name
		
class Lesson (models.Model):
    subject = models.CharField(max_length=30)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()
    def  __unicode__(self):
	    return self.subject