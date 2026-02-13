# 🤗 Hugging Face Deployment Guide

## Deployment Strategy

We'll deploy the NestTask application to Hugging Face Spaces:
- **Backend**: FastAPI Docker Space
- **Frontend**: Static Space or separate Next.js deployment

---

## Backend Deployment to Hugging Face

### Step 1: Create Space via Web Interface

1. Go to: https://huggingface.co/new-space
2. Fill in details:
   - **Owner**: anzal-developer
   - **Space name**: nesttask-backend
   - **License**: MIT
   - **SDK**: Docker
   - **Visibility**: Public

### Step 2: Clone and Push Code

```bash
# Clone your new space
git clone https://huggingface.co/spaces/anzal-developer/nesttask-backend
cd nesttask-backend

# Copy backend files
cp -r ../Hackathon-2/phase-2/backend/* .

# Copy README for Space
cp README_HF.md README.md

# Add files
git add .
git commit -m "Initial backend deployment"
git push
```

### Step 3: Add Secrets (Environment Variables)

Go to: https://huggingface.co/spaces/anzal-developer/nesttask-backend/settings

Add these secrets:
- `DATABASE_URL` - Your Neon PostgreSQL URL
- `BETTER_AUTH_SECRET` - Your auth secret
- `FRONTEND_URL` - Your frontend URL

### Step 4: Wait for Build

The Space will automatically build from the Dockerfile. Check build logs at:
https://huggingface.co/spaces/anzal-developer/nesttask-backend/logs

### Step 5: Test Backend

Once deployed, test:
```bash
curl https://anzal-developer-nesttask-backend.hf.space/health
```

---

## Frontend Deployment Options

### Option 1: Vercel (Current)
Keep frontend on Vercel, update `NEXT_PUBLIC_API_URL` to point to HF backend:
```
https://anzal-developer-nesttask-backend.hf.space
```

### Option 2: Hugging Face Static Space
Deploy frontend as a static site to HF Spaces.

### Option 3: Combined Gradio App
Create a Gradio interface that wraps both frontend and backend.

---

## Files Structure for HF Backend

```
nesttask-backend/
├── Dockerfile              # Container configuration
├── requirements.txt        # Python dependencies
├── README.md              # Space description
├── app/                   # FastAPI application
│   ├── __init__.py
│   ├── main.py           # Main app
│   ├── config.py         # Settings
│   ├── db.py             # Database
│   ├── models/           # SQLModel entities
│   ├── routes/           # API endpoints
│   └── middleware/       # Auth middleware
└── .dockerignore         # Files to exclude
```

---

## Environment Variables Required

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | Neon PostgreSQL connection | `postgresql://user:pass@host/db?sslmode=require` |
| `BETTER_AUTH_SECRET` | JWT secret (must match frontend) | `your-secret-key` |
| `FRONTEND_URL` | Frontend URL for CORS | `https://frontend.vercel.app` |

---

## Advantages of Hugging Face Deployment

✅ **No Deployment Protection** - Public API access by default
✅ **Docker Support** - Full control over environment
✅ **Free Tier** - Good for demos and small projects
✅ **Built-in Logs** - Easy debugging
✅ **Auto HTTPS** - Secure by default
✅ **Community** - ML-friendly ecosystem

---

## Testing After Deployment

### 1. Health Check
```bash
curl https://anzal-developer-nesttask-backend.hf.space/health
# Expected: {"status":"ok"}
```

### 2. API Documentation
Visit: https://anzal-developer-nesttask-backend.hf.space/docs

### 3. Auth Test
```bash
curl https://anzal-developer-nesttask-backend.hf.space/api/tasks
# Expected: {"detail":"Not authenticated"}
```

### 4. Full App Test
1. Update frontend `NEXT_PUBLIC_API_URL` to HF backend
2. Redeploy frontend
3. Visit frontend and sign up
4. Create tasks

---

## Troubleshooting

### Build Fails
- Check Dockerfile syntax
- Verify requirements.txt has all dependencies
- Check build logs in HF Space settings

### Runtime Errors
- Check environment variables are set in Secrets
- View logs: https://huggingface.co/spaces/anzal-developer/nesttask-backend/logs
- Ensure DATABASE_URL is accessible from HF servers

### CORS Errors
- Verify `FRONTEND_URL` in HF Secrets matches your frontend domain
- Check CORS middleware in `app/main.py`

---

## Alternative: Manual CLI Deployment

```bash
# Install Hugging Face CLI
pip install huggingface_hub

# Login
huggingface-cli login

# Create space
huggingface-cli repo create nesttask-backend --type space --space_sdk docker

# Push code
cd backend
git init
git remote add space https://huggingface.co/spaces/anzal-developer/nesttask-backend
git add .
git commit -m "Deploy backend"
git push space main
```

---

## Next Steps

1. ✅ Clean up Vercel deployments (optional)
2. ✅ Update frontend to use HF backend URL
3. ✅ Test full application flow
4. ✅ Update README with new deployment URLs
5. ✅ Share your deployed app!

---

**Backend Space**: https://huggingface.co/spaces/anzal-developer/nesttask-backend (to be created)
**Frontend**: https://frontend-tau-sepia-80.vercel.app (existing)
