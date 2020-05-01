from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    #client Views
    path('clients', views.ClientList.as_view(), name='client_list'),
    path('clientview/<pk>', views.ClientView.as_view(), name='client_view'),
    path('clientnew', views.ClientCreate.as_view(), name='client_new'),
    path('clientview/<pk>', views.ClientView.as_view(), name='client_view'),
    path('clientedit/<pk>', views.ClientUpdate.as_view(), name='client_edit'),
    path('clientdelete/<pk>', views.ClientDelete.as_view(), name='client_delete'),
    #location Views
    path('locations', views.LocationList.as_view(), name='location_list'),
    path('locationview/<pk>', views.LocationView.as_view(), name='location_view'),
    path('locationnew', views.LocationCreate.as_view(), name='location_new'),
    path('locationview/<pk>', views.LocationView.as_view(), name='location_view'),
    path('locationedit/<pk>', views.LocationUpdate.as_view(), name='location_edit'),
    path('locationdelete/<pk>', views.LocationDelete.as_view(), name='location_delete'),
    #product Views
    path('products', views.ProductList.as_view(), name='product_list'),
    path('productview/<pk>', views.ProductView.as_view(), name='product_view'),
    path('productnew', views.ProductCreate.as_view(), name='product_new'),
    path('productview/<pk>', views.ProductView.as_view(), name='product_view'),
    path('productedit/<pk>', views.ProductUpdate.as_view(), name='product_edit'),
    path('productdelete/<pk>', views.ProductDelete.as_view(), name='product_delete'),
    #test standard views
    path('teststandards', views.TestStandardList.as_view(), name='teststandard_list'),
    path('teststandardview/<pk>', views.TestStandardView.as_view(), name='teststandard_view'),
    path('teststandardnew', views.TestStandardCreate.as_view(), name='teststandard_new'),
    path('teststandardview/<pk>', views.TestStandardView.as_view(), name='teststandard_view'),
    path('teststandardedit/<pk>', views.TestStandardUpdate.as_view(), name='teststandard_edit'),
    path('teststandarddelete/<pk>', views.TestStandardDelete.as_view(), name='teststandard_delete'),
    #sertificate Views
    path('certificates', views.CertificateList.as_view(), name='certificate_list'),
    path('certificateview/<pk>', views.CertificateView.as_view(), name='certificate_view'),
    path('certificatenew', views.CertificateCreate.as_view(), name='certificate_new'),
    path('certificateview/<pk>', views.CertificateView.as_view(), name='certificate_view'),
    path('certificateedit/<pk>', views.CertificateUpdate.as_view(), name='certificate_edit'),
    path('certificatedelete/<pk>', views.CertificateDelete.as_view(), name='certificate_delete'),
]
