# Deployment Guide

## Production Deployment Architecture

```
Frontend (Vercel)
       ↓
Load Balancer (Cloudflare)
       ↓
Backend (Railway)
       ↓
Database (Supabase PostgreSQL)
Cache (Redis Cloud)
Storage (Cloudinary, Supabase Storage)
```

## Frontend Deployment (Vercel)

### 1. Prepare Repository
```bash
cd client
git init
git add .
git commit -m "Initial commit"
```

### 2. Push to GitHub
```bash
git remote add origin https://github.com/yourusername/dna-client.git
git push -u origin main
```

### 3. Deploy to Vercel
- Go to https://vercel.com
- Click "New Project"
- Import your GitHub repository
- Configure environment variables:
  - `NEXT_PUBLIC_API_URL=https://api.dnaplatform.com`
  - `NEXT_PUBLIC_WS_URL=wss://api.dnaplatform.com`
  - Other OAuth and service keys
- Click "Deploy"

### 4. Configure Custom Domain
- In Vercel project settings
- Add your custom domain
- Update DNS records

## Backend Deployment (Railway)

### 1. Prepare Repository
```bash
cd server
git init
git add .
git commit -m "Initial commit"
```

### 2. Create Railway Account
- Go to https://railway.app
- Sign up with GitHub

### 3. Deploy
```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Set environment variables
railway variable set DATABASE_URL postgresql://...
railway variable set REDIS_URL redis://...
railway variable set SECRET_KEY your-secret-key
# Add other variables...

# Deploy
railway up
```

### 4. Configure Database

Use Supabase for PostgreSQL:
- Go to https://supabase.com
- Create new project
- Get connection string
- Set DATABASE_URL in Railway

### 5. Configure Redis

Use Redis Cloud:
- Go to https://redis.com/try-free
- Create free cluster
- Get connection string
- Set REDIS_URL in Railway

## Database Setup (Supabase)

### 1. Create Project
- Go to https://supabase.com/dashboard
- Click "New Project"
- Configure region (choose closest to users)

### 2. Create Tables
```sql
-- Run migrations or SQL scripts
-- Use Alembic migrations:
alembic upgrade head
```

### 3. Set Up Storage Buckets
- Go to Storage section
- Create buckets for:
  - `product-images`
  - `user-avatars`
  - `community-banners`
  - `builds`

### 4. Configure Backups
- Enable automated daily backups
- Set retention policy

## Environment Variables (Production)

### Backend (.env)
```
# Database
DATABASE_URL=postgresql://user:password@db.supabase.co:5432/postgres

# Redis
REDIS_URL=redis://:password@redis.cloud.com:10000

# Server
ENVIRONMENT=production
DEBUG=False
SECRET_KEY=your-very-secure-secret-key-min-32-chars
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
CORS_ORIGINS=["https://dnaplatform.com", "https://www.dnaplatform.com"]
ALLOWED_HOSTS=["dnaplatform.com", "www.dnaplatform.com", "api.dnaplatform.com"]

# OAuth
GOOGLE_CLIENT_ID=your-production-google-id
GOOGLE_CLIENT_SECRET=your-production-google-secret
GITHUB_CLIENT_ID=your-production-github-id
GITHUB_CLIENT_SECRET=your-production-github-secret
DISCORD_CLIENT_ID=your-production-discord-id
DISCORD_CLIENT_SECRET=your-production-discord-secret

# Email
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
SMTP_FROM_EMAIL=noreply@dnaplatform.com

# Storage
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret

# Supabase
SUPABASE_URL=https://xxxx.supabase.co
SUPABASE_KEY=your-supabase-key
```

### Frontend (.env.production)
```
NEXT_PUBLIC_API_URL=https://api.dnaplatform.com
NEXT_PUBLIC_WS_URL=wss://api.dnaplatform.com
NEXT_PUBLIC_GOOGLE_CLIENT_ID=your-production-id
NEXT_PUBLIC_GITHUB_CLIENT_ID=your-production-id
NEXT_PUBLIC_DISCORD_CLIENT_ID=your-production-id
NEXT_PUBLIC_CLOUDINARY_CLOUD_NAME=your-cloud-name
NEXT_PUBLIC_SUPABASE_URL=https://xxxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
```

## SSL/TLS Certificate

### Using Cloudflare (Recommended)
1. Add domain to Cloudflare
2. Change nameservers at domain registrar
3. Enable "Flexible SSL" or "Full SSL"
4. Cloudflare will automatically provision certificate

### Using Let's Encrypt
1. Install Certbot
2. Run `certbot certonly --standalone -d dnaplatform.com -d www.dnaplatform.com`
3. Configure web server to use certificate

## Performance Optimization

### Frontend
```bash
# Build optimization
npm run build

# Analyze bundle size
npm run analyze

# Enable compression in next.config.js
compression: true

# Use CDN for images (Cloudinary/Supabase)
# Implement caching headers
```

### Backend
```python
# Enable gzip compression
from fastapi.middleware.gzip import GZIPMiddleware
app.add_middleware(GZIPMiddleware, minimum_size=1000)

# Enable caching
from slowapi import Limiter
limiter = Limiter(key_func=get_remote_address)

# Database connection pooling
pool_size=20
max_overflow=40
```

## Monitoring & Logging

### Frontend Monitoring
- Vercel Analytics (built-in)
- Sentry for error tracking
- Google Analytics for user behavior

### Backend Monitoring
```bash
# Install Sentry
pip install sentry-sdk

# Initialize in main.py
import sentry_sdk
sentry_sdk.init("your-sentry-dsn")
```

## Backup & Recovery

### Database Backups
- Supabase: Automated daily backups (30-day retention)
- Manual backup: `pg_dump` for PostgreSQL

### Code Backup
- GitHub repositories (version control)
- Regular commits

### Disaster Recovery Plan
1. Maintain database backups
2. Keep .env files secured
3. Document all API keys
4. Have rollback procedure

## Security Checklist

- [ ] HTTPS/SSL enabled
- [ ] Environment variables secured
- [ ] Database password strong
- [ ] OAuth secrets stored safely
- [ ] Rate limiting enabled
- [ ] CORS properly configured
- [ ] Input validation implemented
- [ ] SQL injection prevention
- [ ] XSS protection enabled
- [ ] CSRF tokens implemented
- [ ] API keys rotated regularly
- [ ] Monitoring alerts set up

## Post-Deployment

1. Run smoke tests
2. Verify all API endpoints
3. Check database connectivity
4. Monitor error logs
5. Test OAuth flows
6. Verify file uploads
7. Check WebSocket connections
8. Monitor performance metrics

## Rollback Procedure

### Frontend
```bash
# Revert to previous version in Vercel
# Click "Deployments" → Select previous version → Click "Restore"
```

### Backend
```bash
# Railway automatic rollback
# Go to Dashboard → Deployments → Select previous → Trigger
```

## Continuous Integration/Deployment (CI/CD)

### GitHub Actions Example
```yaml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Vercel
        uses: vercel/action@master
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
```

## Support & Escalation

- Monitor uptime: https://status.dnaplatform.com
- Review logs: Railway dashboard, Supabase logs
- Check performance: Vercel analytics
- Contact hosting providers for outages
