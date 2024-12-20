# TaskManager

# Real-Time Collaborative Task Management System

A full-stack task management application featuring real-time collaboration, built with FastAPI, React, and PostgreSQL.

## Features

### Core Functionality
- 🔄 Real-time task updates using WebSocket
- 👥 Multi-user collaboration
- 🔐 JWT-based authentication
- 📱 Responsive design
- 📊 Task status tracking and filtering

### Task Management
- ✏️ Create, read, update, and delete tasks
- 👤 Assign tasks to team members
- 💬 Comment on tasks
- 📅 Set due dates
- 📝 Activity logging for all task changes

### Technical Features
- TypeScript support
- Database optimization with proper indexing
- Async/await patterns for improved performance
- Comprehensive error handling
- Secure password hashing
- CORS support

## Tech Stack

### Backend
- FastAPI (Python 3.8+)
- PostgreSQL
- MongoDB (for real-time features)
- JWT for authentication
- WebSockets for real-time updates

### Frontend
- React 18
- TypeScript
- Chakra UI
- React Query
- Recoil
- React Router

## Prerequisites

- Python 3.8+
- Node.js 16+
- PostgreSQL 12+
- MongoDB 4.4+

## Installation

### Backend Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/task-management-system.git
cd task-management-system
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
```bash
psql -U postgres -f database/schema.sql
```

5. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Configure environment variables:
```bash
cp .env.example .env.local
# Edit .env.local with your configuration
```

## Running the Application

### Start the Backend Server

```bash
# From the root directory
python main.py
```

The API will be available at `http://localhost:8000`

### Start the Frontend Development Server

```bash
# From the frontend directory
npm run dev
```

The application will be available at `http://localhost:3000`

## API Documentation

Once the backend server is running, visit `http://localhost:8000/docs` for the interactive API documentation.

### Key Endpoints

- `POST /token` - Obtain JWT token
- `POST /tasks/` - Create a new task
- `GET /tasks/` - List all tasks
- `PUT /tasks/{task_id}` - Update a task
- `DELETE /tasks/{task_id}` - Delete a task
- `WS /ws/{client_id}` - WebSocket endpoint for real-time updates

## Testing

### Backend Tests
```bash
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## Project Structure

```
task-management-system/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── tests/
├── frontend/
│   ├── src/
│   ├── package.json
│   └── tests/
├── database/
│   └── schema.sql
└── README.md
```

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

## Security Considerations

- All passwords are hashed using bcrypt
- JWT tokens expire after 30 minutes
- CORS is configured for security
- Input validation on both frontend and backend
- Prepared statements for SQL queries
- Rate limiting on API endpoints

## Performance Optimizations

- Database indexing for frequent queries
- Efficient WebSocket message handling
- React Query for optimal data fetching
- Lazy loading of components
- Proper connection pooling


## Support

For support, please open an issue in the GitHub repository

## Acknowledgments

- FastAPI documentation
- React documentation
- Chakra UI team
- PostgreSQL documentation
- MongoDB documentation
