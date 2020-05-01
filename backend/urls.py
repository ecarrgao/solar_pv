from django.urls import path
from . import views

urlpatterns = [
    path('', views.TestStandardList.as_view(), name='teststandard_list'),
    path('view/<int:pk>', views.TestStandardView.as_view(), name='teststandard_view'),
    path('new', views.TestStandardCreate.as_view(), name='teststandard_new'),
    path('view/<int:pk>', views.TestStandardView.as_view(), name='teststandard_view'),
    path('edit/<int:pk>', views.TestStandardUpdate.as_view(), name='teststandard_edit'),
    path('delete/<int:pk>', views.TestStandardDelete.as_view(), name='teststandard_delete'),
]
