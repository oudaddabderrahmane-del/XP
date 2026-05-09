# DNA Platform 🧬

A futuristic gaming-tech platform combining marketplace, social media, PC builder, and AI assistant for gamers, developers, and PC builders.

## 🚀 Features

- **Marketplace**: Buy/sell PC hardware, gaming setups, and accessories
- **Social Media**: Communities, posts, discussions, user profiles with XP system
- **PC Builder**: PCPartPicker-style builder with compatibility checking
- **Real-time Chat**: WebSocket-based messaging system
- **AI System**: Smart recommendations, scam detection, price estimation
- **Admin Panel**: Moderation, analytics, and fraud detection

## 🏗️ Architecture

- **Frontend**: Next.js 15 + TypeScript + TailwindCSS + Framer Motion
- **Backend**: FastAPI + Django + WebSockets
- **Database**: PostgreSQL + Redis
- **Storage**: Cloudinary + Supabase
- **Deployment**: Vercel (Frontend) + Railway (Backend) + Supabase (Database)

## 📁 Project Structure

```
DNA/
├── client/              # Next.js frontend
│   ├── app/            # App router pages
│   ├── components/     # Reusable components
│   ├── hooks/          # Custom React hooks
│   ├── lib/            # Utility functions
│   ├── store/          # Zustand state management
│   ├── styles/         # Global styles
│   └── public/         # Static assets
├── server/             # FastAPI + Django backend
│   ├── api/            # API routes and endpoints
│   ├── models/         # Database models
│   ├── schemas/        # Pydantic schemas
│   ├── services/       # Business logic
│   ├── utils/          # Helper functions
│   ├── config/         # Configuration files
│   └── migrations/     # Database migrations
└── docs/               # Documentation
```

## 🛠️ Tech Stack

### Frontend
- Next.js 15
- TypeScript
- TailwindCSS
- Framer Motion
- ShadCN UI
- Zustand
- React Query

### Backend
- FastAPI (Primary APIs)
- Django (Admin & Auth)
- WebSockets (Real-time)
- SQLAlchemy (ORM)
- Alembic (Migrations)

### Database & Storage
- PostgreSQL (Primary Database)
- Redis (Caching & Sessions)
- Cloudinary (Image Storage)
- Supabase Storage (File Storage)

## 🎨 Design System

- **Colors**: Black (#000000), White (#FFFFFF), Gray (#7A7A7A)
- **Accent**: Neon Blue, RGB Purple
- **Style**: Dark mode, Glassmorphism, RGB effects
- **Fonts**: Orbitron (headings), Inter/Poppins (content)
- **Animations**: Framer Motion

## 🔐 Security

- JWT Authentication
- OAuth (Google, GitHub, Discord)
- Rate limiting
- CSRF protection
- XSS protection
- AI Moderation
- Scam detection
- Email verification

## 📦 Installation

### Prerequisites
- Node.js 18+
- Python 3.10+
- PostgreSQL 13+
- Redis 6+

### Frontend Setup
```bash
cd client
npm install
npm run dev
```

### Backend Setup
```bash
cd server
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
python main.py
```

## 🚀 Deployment

### Frontend
```bash
cd client
vercel deploy
```

### Backend
```bash
cd server
# Deploy to Railway
railway deploy
```

## 📄 License

MIT License

## 👨‍💻 Contributing

See CONTRIBUTING.md for guidelines.
