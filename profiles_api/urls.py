from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)
#(name of url, view, retrieving URLs in our router)
#Api Root page will only show routes registered via DefaultRouter().
#Only need to specify the base_name if the ViewSet doesn't have a queryset.
#Django takes queryset as basename otherwise.

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]