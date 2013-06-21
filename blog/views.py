from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy as reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
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
class LoginRequiredMixin(object):
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(LoginRequiredMixin, self).dispatch(*args,**kwargs)

#####IMAGE BLOG
class ImageBlogListView(ListView):
	template_name = 'blog/imageblog_list.html'
	model = ImageBlog

class ImageBlogDetailView(DetailView):
	template_name = 'blog/imageblog_detail.html'

	def get_object(self):
		return ImageBlog.objects.get(pk = self.kwargs['pk'])

class ImageBlogCreateView(LoginRequiredMixin, CreateView):
	template_name = 'blog/imageblog_create.html'
	form_class = ImageBlogForm

	def get_success_url(self):
		print self.object.pk
		return reverse('imageblog_detail', kwargs = {'pk':self.object.pk})

class ImageBlogUpdateView(LoginRequiredMixin, UpdateView):
	template_name = 'blog/imageblog_update.html'
	form_class = ImageBlogForm

	def get_object(self):
		return ImageBlog.objects.get(pk = self.kwargs['pk'])

	def get_success_url(self):
		return reverse('imageblog_detail', kwargs = {'pk':self.object.pk})

class ImageBlogDeleteView(LoginRequiredMixin, DeleteView):
	template_name = 'blog/imageblog_delete.html'

	def get_object(self):
		return ImageBlog.objects.get(pk = self.kwargs['pk'])

	def get_success_url(self):
		return reverse('imageblog_list')

