from django.utils import timezone
from django.contrib.auth.middleware import get_user
from django.http import JsonResponse

class GPSAttendanceMiddleware:
    """
    Middleware that automatically checks student attendance every 15 minutes.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = get_user(request)
        if user.is_authenticated and user.role == 'student':
            # This logic can be extended for GPS-based checking
            now = timezone.now()
            last_check = request.session.get('last_attendance_check')
            
            if not last_check or (now - last_check).total_seconds() > 900:  # 15 minutes
                # Implement attendance checking logic
                self.mark_attendance(user)
                request.session['last_attendance_check'] = now

        response = self.get_response(request)
        return response

    def mark_attendance(self, student_user):
        # Logic to mark attendance based on GPS location
        from .models import Attendance, Student

        student = Student.objects.get(user=student_user)
        Attendance.objects.create(
            student=student,
            gps_location="Captured GPS Coordinates",
            status='Present',
            verification_method='Automatic GPS check'
        )
