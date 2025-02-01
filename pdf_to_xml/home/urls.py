from django.urls import path
from . import views

urlpatterns = [
   path('',views.welcome,name='home'),
   path("upload/", views.upload_pdf, name="upload_pdf"),
    path("save-transaction/", views.save_transaction, name="save_transaction"),
]
