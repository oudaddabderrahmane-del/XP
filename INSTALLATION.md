# Installation Guide

## Prerequisites

- Node.js 18+ (https://nodejs.org/)
- Python 3.10+ (https://www.python.org/)
- PostgreSQL 13+ (https://www.postgresql.org/)
- Redis 6+ (https://redis.io/)
- Git (https://git-scm.com/)

## Frontend Setup (Next.js)

### 1. Navigate to client directory
```bash
cd client
```

### 2. Install dependencies
```bash
npm install
```

### 3. Create environment file
```bash
cp .env.example .env.local
```

Edit `.env.local` with your configuration:
```
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_GOOGLE_CLIENT_ID=your_google_id
NEXT_PUBLIC_GITHUB_CLIENT_ID=your_github_id
NEXT_PUBLIC_DISCORD_CLIENT_ID=your_discord_id
NEXT_PUBLIC_CLOUDINARY_CLOUD_NAME=your_cloudinary_name
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_key
NEXT_PUBLIC_WS_URL=ws://localhost:8000
```

### 4. Run development server
```bash
npm run dev
```

The app will be available at `http://localhost:3000`

## Backend Setup (FastAPI)

### 1. Navigate to server directory
```bash
cd server
```

### 2. Create virtual environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create environment file
```bash
cp .env.example .env
```

Edit `.env` with your configuration:
```
DATABASE_URL=postgresql://user:password@localhost:5432/dna
REDIS_URL=redis://localhost:6379
SECRET_KEY=your-secret-key-change-in-production
GOOGLE_CLIENT_ID=your_google_id
GITHUB_CLIENT_ID=your_github_id
DISCORD_CLIENT_ID=your_discord_id
CLOUDINARY_CLOUD_NAME=your_cloudinary_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### 5. Setup database

#### Option A: Using PostgreSQL directly
```bash
# Create database
createdb dna

# Run migrations
alembic upgrade head
```

#### Option B: Using Docker
```bash
docker run --name dna-postgres -e POSTGRES_PASSWORD=password -d postgres:15
docker run --name dna-redis -d redis:7
```

### 6. Run development server
```bash
python main.py
```

The API will be available at `http://localhost:8000`
API documentation at `http://localhost:8000/docs`

## Database Setup

### 1. Create database user (PostgreSQL)
```bash
psql -U postgres
CREATE USER dna_user WITH PASSWORD 'dna_password';
CREATE DATABASE dna OWNER dna_user;
GRANT ALL PRIVILEGES ON DATABASE dna TO dna_user;
```

### 2. Run migrations
```bash
# From server directory
alembic upgrade head
```

## Environment Variables Reference

### Frontend (.env.local)
| Variable | Description | Example |
|----------|-------------|---------|
| NEXT_PUBLIC_API_URL | Backend API URL | http://localhost:8000 |
| NEXT_PUBLIC_WS_URL | WebSocket URL | ws://localhost:8000 |
| NEXT_PUBLIC_GOOGLE_CLIENT_ID | Google OAuth ID | xxx.apps.googleusercontent.com |
| NEXT_PUBLIC_GITHUB_CLIENT_ID | GitHub OAuth ID | xxx |
| NEXT_PUBLIC_DISCORD_CLIENT_ID | Discord OAuth ID | xxx |
| NEXT_PUBLIC_CLOUDINARY_CLOUD_NAME | Cloudinary cloud name | xxx |
| NEXT_PUBLIC_SUPABASE_URL | Supabase URL | https://xxx.supabase.co |
| NEXT_PUBLIC_SUPABASE_ANON_KEY | Supabase anonymous key | xxx |

### Backend (.env)
| Variable | Description | Example |
|----------|-------------|---------|
| DATABASE_URL | PostgreSQL connection string | postgresql://user:pass@localhost/dna |
| REDIS_URL | Redis connection string | redis://localhost:6379 |
| SECRET_KEY | JWT secret key | your-secret-key |
| ALGORITHM | JWT algorithm | HS256 |
| ACCESS_TOKEN_EXPIRE_MINUTES | Token expiration | 30 |
| GOOGLE_CLIENT_ID | Google OAuth ID | xxx.apps.googleusercontent.com |
| GOOGLE_CLIENT_SECRET | Google OAuth secret | xxx |
| GITHUB_CLIENT_ID | GitHub OAuth ID | xxx |
| GITHUB_CLIENT_SECRET | GitHub OAuth secret | xxx |
| DISCORD_CLIENT_ID | Discord OAuth ID | xxx |
| DISCORD_CLIENT_SECRET | Discord OAuth secret | xxx |

## Running the Full Stack

### Terminal 1 - Database
```bash
redis-server
```

### Terminal 2 - Backend
```bash
cd server
source venv/bin/activate  # or venv\Scripts\activate on Windows
python main.py
```

### Terminal 3 - Frontend
```bash
cd client
npm run dev
```

Now you have the full stack running:
- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs

## Troubleshooting

### Port Already in Use
If port 3000 or 8000 is already in use:
```bash
# Frontend with different port
npm run dev -- -p 3001

# Backend with different port
python main.py --port 8001
```

### Database Connection Error
- Ensure PostgreSQL is running
- Check DATABASE_URL in .env
- Verify user credentials

### Module Not Found (Python)
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` again

### CORS Errors
- Check CORS_ORIGINS in server/config/settings.py
- Ensure frontend URL matches

## Next Steps

1. Set up OAuth providers (Google, GitHub, Discord)
2. Configure Cloudinary for image storage
3. Set up Supabase for file storage
4. Configure email service for notifications
5. Set up monitoring and logging
