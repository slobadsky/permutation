from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home,name='home-page'),
    path('mes-demandes/', views.mes_demandes,name='mes_demandes'),
    path('acceptation/', views.acceptation,name='acceptation'),
    path('pdf-view/<str:unique_ref>', views.html_to_pdf_view,name='pdf-view'),
    path('update-permutation-demande/<str:upd_ref>', views.update_permutation_demande,name='update-permutation-demande'),
    path('delete-permutation-demande/<str:upd_ref>', views.delete_permutation_demande,name='delete-permutation-demande'),
    path('update-permutation-accept/<str:upd_ref>', views.update_permutation_accept,name='update-permutation-accept'),
    path('liste-salaries/', views.liste_salaries,name='liste-salaries'),
    path('login/', views.login_page,name='login-page'),
    path('logout/', views.logout_page,name='logout-page'),
]