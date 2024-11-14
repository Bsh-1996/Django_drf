from django.urls import path
from . import views

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegister.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', views.UserApi.as_view()),
    path('users_list/', views.UserListApi.as_view()),
]


router = routers.SimpleRouter()
router.register('user', views.UserViewSet)
urlpatterns += router.urls






'''
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMTYyNTM0MiwiaWF0IjoxNzMxNTM4OTQyLCJqdGkiOiI4Njg4YjI4MjE2NWQ0MTVmOWI5OWIwNTBmZWZlMGZlZCIsInVzZXJfaWQiOjF9.gOzLJtNnrUJNtncGdiGlpOIG0ZY-Wz4m3fD3zhql-ow",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxNTM5MjQyLCJpYXQiOjE3MzE1Mzg5NDIsImp0aSI6ImY2OTFjZjA5OTM3NjRjZWQ4MDBmYzhhMmQyOGE3MzhlIiwidXNlcl9pZCI6MX0.m6Cq8Fee-Xm6IdXcpVdeX1mG5znCa-I2NNBN8U112yw"
}
'''