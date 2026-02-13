---
title: NestTask Backend API
emoji: ✅
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
license: mit
---

# NestTask Backend API

Multi-user task management API built with FastAPI, SQLModel, and Neon PostgreSQL.

## Features

- ✅ JWT Authentication
- ✅ User Isolation
- ✅ RESTful API
- ✅ CRUD Operations for Tasks
- ✅ PostgreSQL Database
- ✅ Automatic API Documentation

## API Documentation

Once deployed, visit `/docs` for interactive API documentation (Swagger UI).

## Environment Variables Required

- `DATABASE_URL` - Neon PostgreSQL connection string
- `BETTER_AUTH_SECRET` - JWT secret key
- `FRONTEND_URL` - Your frontend URL for CORS

## Endpoints

- `GET /health` - Health check
- `GET /docs` - API documentation
- `POST /api/tasks` - Create task
- `GET /api/tasks` - List tasks
- `PUT /api/tasks/{id}` - Update task
- `DELETE /api/tasks/{id}` - Delete task
