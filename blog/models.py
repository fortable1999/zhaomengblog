from django.db import models
import uuid

# Create your models here.

class Blog(models.Model):
	title = models.CharField(max_length = 100)
	postdate = models.DateTimeField(auto_now = True)
	text = models.TextField()

	def __unicode__(self):
		return "Blog: %s" % self.title

	class Meta:
		ordering = ['-postdate']

class ImageBlog(Blog):
	image = models.ImageField(upload_to = 'image/' + str(uuid.uuid4()))
