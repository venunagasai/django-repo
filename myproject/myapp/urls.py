from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", views.hello),
    path("hi/", views.hello),
    path("bye/", views.bye),
    path("echo/", views.echo),
    path("update/", views.update_echo),  # PUT
    path("delete/", views.delete_echo),  # DELETE
    path("cbv-post/", views.SimplePostView.as_view()),
    path("drf-post/", views.UserAPI.as_view()),
    # Router for viewsets
    path("simple-products/", views.simple_page),
    path("newstudents/", views.student_api),
    path("login/", views.login_page),
    path("home/", views.home),
    path("profile/", views.ProfileAPI.as_view()),
    path("api-token-auth/", obtain_auth_token),
]

router = DefaultRouter()
router.register(r"students", views.StudentViewSet)

urlpatterns += [
    path("api/", include(router.urls)),
    # Also expose the same viewset at /students/ to match existing clients
    path("students/", include(router.urls)),
]
