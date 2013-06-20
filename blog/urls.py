from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
import views

urlpatterns = patterns('',
    url(r'^$', views.ImageBlogListView.as_view(), name='imageblog_list'),
    url(r'^create/$', views.ImageBlogCreateView.as_view(), name='imageblog_create'),
    url(r'^update/(?P<pk>\d+)/$', views.ImageBlogUpdateView.as_view(), name='imageblog_update'),
    url(r'^detail/(?P<pk>\d+)/$', views.ImageBlogDetailView.as_view(), name='imageblog_detail'),
    url(r'^delete/(?P<pk>\d+)/$', views.ImageBlogDeleteView.as_view(), name='imageblog_delete'),
	url(r'^logout/(?P<next_page>.*)/$', 'django.contrib.auth.views.logout', name='auth_logout_next'),

    # url(r'^create/$', views.BlogCreateView.as_view(), name='blog_create'),
    # url(r'^update/(?P<pk>\d+)/$', views.BlogUpdateView.as_view(), name='blog_update'),
    # url(r'^detail/(?P<pk>\d+)/$', views.BlogDetailView.as_view(), name='blog_detail'),
    # url(r'^delete/(?P<pk>\d+)/$', views.BlogDeleteView.as_view(), name='blog_delete'),
    # url(r'^$', views.BlogListView.as_view(), name='blog_list'),
    # url(r'^image/create/$', views.ImageBlogCreateView.as_view(), name='imageblog_create'),
    # url(r'^image/update/(?P<pk>\d+)/$', views.ImageBlogUpdateView.as_view(), name='imageblog_update'),
    # url(r'^image/detail/(?P<pk>\d+)/$', views.ImageBlogDetailView.as_view(), name='imageblog_detail'),
    # url(r'^image/delete/(?P<pk>\d+)/$', views.ImageBlogDeleteView.as_view(), name='imageblog_delete'),
    # url(r'^image/$', views.ImageBlogListView.as_view(), name='imageblog_list'),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
