from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('parent', 'Parent'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    contact_info = models.TextField(null=True, blank=True)
    profile_data = models.JSONField(default=dict, blank=True)

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read_status = models.BooleanField(default=False)
    attachments = models.FileField(upload_to='message_attachments/', null=True, blank=True)

    def __str__(self):
        return f"{self.sender.username} -> {self.receiver.username}"
class Calendar(models.Model):
    event_type = models.CharField(max_length=50)  # e.g., Meeting, Holiday, Exam, etc.
    title = models.CharField(max_length=255)  # Event title
    description = models.TextField()  # Event description
    date_time = models.DateTimeField()  # Event date and time
    location = models.CharField(max_length=255)  # Event location
    participants = models.ManyToManyField(User, related_name='calendar_events')  # Users involved in the event
    reminders = models.TextField(blank=True)  # Additional reminders or notifications

    def __str__(self):
        return self.title
class Document(models.Model):
    title = models.CharField(max_length=255)  # Title of the document
    doc_type = models.CharField(max_length=50)  # Type of document (e.g., Report, Certificate, etc.)
    content = models.FileField(upload_to='documents/')  # File field for uploading documents
    upload_date = models.DateTimeField(auto_now_add=True)  # Automatically set the upload date/time
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Document owner (linked to a User)
    access_permissions = models.TextField()  # Information about who has access to the document

    def __str__(self):
        return self.title

class School(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    working_hours = models.CharField(max_length=100)
    rules_policies = models.TextField()

    def __str__(self):
        return self.name


class Room(models.Model):
    room_number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.room_number

class Class(models.Model):
    name = models.CharField(max_length=50)
    grade_level = models.CharField(max_length=50)
    academic_year = models.CharField(max_length=50)
    class_teacher = models.ForeignKey(
        'Teacher', 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='assigned_classes'
    )
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)  # Make the field nullable

    def __str__(self):
        return f"{self.name} - {self.grade_level}"



class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    credit_hours = models.IntegerField()
    required_materials = models.TextField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, related_name='teachers')
    qualifications = models.TextField()
    contact_hours = models.CharField(max_length=100)
    school = models.ForeignKey(School, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.user.get_full_name()


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    academic_records = models.TextField(blank=True)
    medical_info = models.TextField(blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE,null=True)
    classes = models.ManyToManyField(Class, related_name='students')
    streak_day = models.PositiveIntegerField(default=0)  # Tracks the number of consecutive days of activity
    exp = models.PositiveIntegerField(default=0)  # Total experience points accumulated by the student
    steps = models.PositiveIntegerField(default=0)  # Tracks the number of steps (can be any kind of metric)
    achievements = models.JSONField(default=list, blank=True)  # A list of achievements the student has unlocked
    is_leader = models.BooleanField(default=False)
    def __str__(self):
        return self.user.get_full_name()


class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    children = models.ManyToManyField(Student, related_name='parents')
    contact_info = models.TextField(blank=True)
    access_privileges = models.TextField(blank=True)

    def __str__(self):
        return self.user.get_full_name()


class Grade(models.Model):
    GRADES = [
        ('5', 'Excellent'),
        ('4', 'Good'),
        ('3', 'Satisfactory'),
        ('2', 'Unsatisfactory'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade_value = models.CharField(max_length=1, choices=GRADES)
    grade_type = models.CharField(max_length=50)  # Assignment, Test, Exam
    term = models.PositiveIntegerField(default=1)
    academic_year = models.CharField(max_length=20)
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.grade_value}"


class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    submission_status = models.TextField()
    grading_criteria = models.TextField()

    def __str__(self):
        return self.title


class Exam(models.Model):
    title = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    duration = models.DurationField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    grade_weight = models.FloatField()

    def __str__(self):
        return self.title


class Schedule(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='schedules')
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='schedules')

    def __str__(self):
        return f"{self.teacher} - {self.class_name} - {self.subject}"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_records')
    date_time = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    status = models.CharField(
        max_length=10,
        choices=[('Present', 'Present'), ('Late', 'Late'), ('Absent', 'Absent')]
    )
    verification_method = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student} - {self.status}"


class Notification(models.Model):
    notification_type = models.CharField(max_length=50)
    content = models.TextField()
    recipients = models.ManyToManyField(User)
    priority = models.CharField(
        max_length=10,
        choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')]
    )
    read_status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.notification_type} - {self.timestamp}"
