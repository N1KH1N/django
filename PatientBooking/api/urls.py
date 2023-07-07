from rest_framework.urls import path
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework.authtoken.views import ObtainAuthToken


router=DefaultRouter()
router.register("account/doctor/user",views.UserDoctorView,basename="doc_user")
router.register("account/patient/user",views.UserPatientView,basename="user")
router.register("doctor/profile",views.DoctorProfileView,basename="profile")
router.register("doctor/department",views.DepartmentView,basename="department")
router.register("doctor/<int:pk>/leave/",views.DoctorLeaveListCreate,basename="doctor")

urlpatterns = [
    path("token/",ObtainAuthToken.as_view(),name="user_token"),
]+router.urls