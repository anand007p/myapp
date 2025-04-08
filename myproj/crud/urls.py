from django.urls import path,include
from .views import RecruiterViewSet, JobViewSet, JobDelegationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'recruiters', RecruiterViewSet)
router.register(r'jobs', JobViewSet)
router.register(r'jobdelegations', JobDelegationViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('allusers',)
# ]



# urlpatterns = [
#     path('', include(router.urls)),
#     path('attendance/<str:date>/', AttendanceAPIView.as_view(), name ='attendance'),
#     path('particular-user-attendance/<str:date>/',ParticularUserAttendanceAPIView.as_view(), name='particular-user-attendance'), 
#     path('attendance/', Attendancecurrentdate.as_view(), name ='attendance-with-time'),
#     path('user-apply-leaves/', UserApplyLeaveViewSet.as_view(), name='users-apply-leaves'),
#     path('user-leaves-summary/',UserLeaveSummaryViewSet.as_view(),name='users-leave-summary'),
#     path('user-wfh-attendance/',WFHattendanceuserViewSet.as_view(),name='users-wfh-attendance'),
#     path('wfh-crone/<str:date>/',wfh_attendance_update_view)
 
# ]