from django.forms import ModelForm
from models import Blog, ImageBlog

class BlogForm(ModelForm):
	class Meta:
		model = Blog
		exclude = ['postdate']

class ImageBlogForm(ModelForm):
	class Meta:
		model = ImageBlog
		exclude = ['postdate']
