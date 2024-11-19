from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, SchoolViewSet, ClassViewSet, SubjectViewSet, TeacherViewSet, StudentViewSet,
    AttendanceViewSet, ParentViewSet, ScheduleViewSet, GradeViewSet, AssignmentViewSet,
    ExamViewSet, NotificationViewSet, MessageViewSet, CalendarViewSet, DocumentViewSet, RoomViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'schools', SchoolViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'parents', ParentViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'assignments', AssignmentViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'calendar', CalendarViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'rooms', RoomViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
