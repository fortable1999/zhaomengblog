from django.core.urlresolvers import reverse_lazy as reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from models import Blog, ImageBlog
from forms import BlogForm, ImageBlogForm

# I need a generic view factory.
# the factory can generate:
#   - Create
#   - Update/Modify
#   - Delete
#   - Detail
#   - List
# with provided model and some simple controller.
# called as CULD2(CreateUpddateListDetailDelete) Factory
# MUST features:
# Usage:
# class BlogViewFactory(CuldFactory):
# 	blog_get_object = lambda v: v.self.object.pk
# 	
# 	class Meta:
# 		template_name_prefix = 'blog/blog'
# 		model = Blog
# 		form_class = BlogForm
# 		success_url_set = {'delete': reverse('blog_list'),
# 				'create': reverse('blog_detail', kwargs={'pk': }),
# 				'update': reverse('blog_detail', kwargs={'pk': 'self.object.pk'}),
# 				}
# 		object_set = {'delete': '',
# 				'update':"",
# 				'detail':"",}

class BlogListView(ListView):
	template_name = 'blog/blog_list.html'
	model = Blog

class BlogDetailView(DetailView):
	template_name = 'blog/blog_detail.html'

	def get_object(self):
		return Blog.objects.get(pk = self.kwargs['pk'])

class BlogCreateView(CreateView):
	template_name = 'blog/blog_create.html'
	form_class = BlogForm

	def get_success_url(self):
		print self.object.pk
		return reverse('blog_detail', kwargs = {'pk':self.object.pk})
		

class BlogUpdateView(UpdateView):
	template_name = 'blog/blog_update.html'
	form_class = BlogForm

	def get_object(self):
		return Blog.objects.get(pk = self.kwargs['pk'])

	def get_success_url(self):
		return reverse('blog_detail', kwargs = {'pk':self.object.pk})

class BlogDeleteView(DeleteView):
	template_name = 'blog/blog_delete.html'

	def get_object(self):
		return Blog.objects.get(pk = self.kwargs['pk'])

	def get_success_url(self):
		return reverse('blog_list')

#####IMAGE BLOG
class ImageBlogListView(ListView):
	template_name = 'blog/blog_list.html'
	model = ImageBlog

class ImageBlogDetailView(DetailView):
	template_name = 'blog/imageblog_detail.html'

	def get_object(self):
		return ImageBlog.objects.get(pk = self.kwargs['pk'])

class ImageBlogCreateView(CreateView):
	template_name = 'blog/imageblog_create.html'
	form_class = ImageBlogForm

	def get_success_url(self):
		print self.object.pk
		return reverse('imageblog_detail', kwargs = {'pk':self.object.pk})

class ImageBlogUpdateView(UpdateView):
	template_name = 'blog/blog_update.html'
	form_class = ImageBlogForm

	def get_object(self):
		return ImageBlog.objects.get(pk = self.kwargs['pk'])

	def get_success_url(self):
		return reverse('imageblog_detail', kwargs = {'pk':self.object.pk})

class ImageBlogDeleteView(DeleteView):
	template_name = 'blog/blog_delete.html'

	def get_object(self):
		return ImageBlog.objects.get(pk = self.kwargs['pk'])

	def get_success_url(self):
		return reverse('imageblog_list')
