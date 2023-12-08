from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from chat import views
from token_auth_app.views import loginView, loginViewPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path("chat/", include("chat.urls")),
    path("goto/", views.goToLogin, name="goto"),
    path("api/login/", loginView),
    path('login/', loginViewPage, name='login-page')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
