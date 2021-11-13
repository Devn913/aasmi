from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'WomReport Portal Admin'
admin.site.index_title = 'WomReport Admin'
admin.site.site_title = 'WomReport'


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls',
         'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('accounts/login/',
         LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),

    # App Routes
    path('', include('safety.urls',
         namespace='safety')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
