from django.contrib.auth.models import AbstractUser
from django.db import models
#from .models import Room  # Make sure to import the Room model

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

class School(models.Model):
    name = models.CharField(max_length=255)
    gps_coordinates = models.CharField(max_length=100)
    working_hours = models.CharField(max_length=100)
    rules_policies = models.TextField()

class Class(models.Model):
    name = models.CharField(max_length=50)
    grade_level = models.CharField(max_length=50)
    academic_year = models.CharField(max_length=50)
    class_teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='classes')
    students = models.ManyToManyField('Student')

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    credit_hours = models.IntegerField()
    required_materials = models.TextField()

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)
    schedule = models.TextField()
    qualifications = models.TextField()
    contact_hours = models.CharField(max_length=100)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_class = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True)
    academic_records = models.TextField()
    attendance_records = models.TextField()
    parent_info = models.TextField()
    medical_info = models.TextField()

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    gps_location = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Late', 'Late'), ('Absent', 'Absent')])
    verification_method = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

# Continue?
class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    children = models.ManyToManyField(Student)
    contact_info = models.TextField()
    access_privileges = models.TextField()

# In app/models.py

# app/models.py

# app/models.py

class Schedule(models.Model):
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='schedules')
    class_name = models.ForeignKey('Class', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    room = models.ForeignKey('Room', on_delete=models.CASCADE, related_name='schedules')  # Use related_name here

    def __str__(self):
        return f"{self.teacher} - {self.class_name} - {self.subject}"




class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade_value = models.CharField(max_length=5)
    grade_type = models.CharField(max_length=50)
    semester = models.CharField(max_length=20)
    academic_year = models.CharField(max_length=20)
    comments = models.TextField(blank=True)

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    submission_status = models.TextField()
    grading_criteria = models.TextField()

class Exam(models.Model):
    title = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    duration = models.DurationField()
    room = models.CharField(max_length=50)
    supervisor = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    grade_weight = models.FloatField()

class Notification(models.Model):
    notification_type = models.CharField(max_length=50)
    content = models.TextField()
    recipients = models.ManyToManyField(User)
    priority = models.CharField(max_length=10, choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')])
    read_status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    read_status = models.BooleanField(default=False)
    attachments = models.FileField(upload_to='message_attachments/', null=True, blank=True)

class Calendar(models.Model):
    event_type = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    participants = models.ManyToManyField(User)
    reminders = models.TextField(blank=True)

class Document(models.Model):
    title = models.CharField(max_length=255)
    doc_type = models.CharField(max_length=50)
    content = models.FileField(upload_to='documents/')
    upload_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    access_permissions = models.TextField()

# app/models.py

class Room(models.Model):
    room_number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    # Other fields...

    schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE, related_name='rooms')  # Use related_name here

    def __str__(self):
        return self.room_number

