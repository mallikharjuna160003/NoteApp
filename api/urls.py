from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    # path('',views.getRoutes,name="routes"),
    path('notes/list/',views.getNotes,name="notes"),
    path('notes/<str:pk>/',views.getNote,name="note"),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
]


