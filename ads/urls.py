from django.conf.urls.static import static
from django.urls import path
from djangoProject2 import settings
from ads.views import (
    root, AdListView, CategoryDetailView, AdDetailView, CategoryListView, CategoryCreateView,
    CategoryUpdateView, CategoryDeleteView, AdCreateView, AdUpdateView, AdDeleteView, AdUploadImageView
)

urlpatterns = [
    path('cat/', CategoryListView.as_view()),
    path('cat/create/', CategoryCreateView.as_view()),
    path('cat/<int:pk>/', CategoryDetailView.as_view()),
    path('cat/<int:pk>/update/', CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete/', CategoryDeleteView.as_view()),
    path('ad/', AdListView.as_view()),
    path('ad/create/', AdCreateView.as_view()),
    path('ad/<int:pk>/', AdDetailView.as_view()),
    path('ad/<int:pk>/update/', AdUpdateView.as_view()),
    path('ad/<int:pk>/delete/', AdDeleteView.as_view()),
    path('ad/<int:pk>/upload_image/', AdUploadImageView.as_view()),
    path('', root),  # URL pattern for the root path should be defined last
]

# Adding static settings for serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("", include('ads.urls')),
#     path("user/", include('users.urls'))
# ]
#
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)