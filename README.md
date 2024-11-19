# TalimPage API Documentation

## Authentication
- **Login**: `POST /api/login/`
  - Request: `{"username": "user1", "password": "password123"}`
  - Response: `{"token": "your-token-value"}`

- **Logout**: `POST /api/logout/`
  - Headers: `Authorization: Token your-token-value`
  - Response: `{"message": "Logged out successfully"}`

## Endpoints
- **Users**: `GET /api/users/`
- **Schools**: `GET /api/schools/`
- **Classes**: `GET /api/classes/`
- **Subjects**: `GET /api/subjects/`
- **Teachers**: `GET /api/teachers/`
- **Students**: `GET /api/students/`
- **Attendance**: `GET /api/attendance/`
- **Parents**: `GET /api/parents/`
- **Schedules**: `GET /api/schedules/`
- **Grades**: `GET /api/grades/`
- **Assignments**: `GET /api/assignments/`
- **Exams**: `GET /api/exams/`
- **Notifications**: `GET /api/notifications/`
- **Messages**: `GET /api/messages/`
- **Calendar**: `GET /api/calendar/`
- **Documents**: `GET /api/documents/`
- **Rooms**: `GET /api/rooms/`
