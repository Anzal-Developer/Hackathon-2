# Deployment Instructions

## ✅ Completed

### GitHub Repository
- **Repository**: https://github.com/Anzal-Developer/Hackathon-2
- **Branch**: main
- **Git email configured**: anzalaideve@gmail.com
- **Status**: Phase-2 successfully pushed to GitHub

### Vercel Frontend Deployment
- **Production URL**: https://frontend-d6600go2w-muhammad-anzals-projects.vercel.app
- **Alias URL**: https://frontend-tau-sepia-80.vercel.app
- **Project**: muhammad-anzals-projects/frontend
- **Status**: Build successful (requires environment variables)

## 🔧 Required: Configure Environment Variables on Vercel

To make the app functional, you need to add the following environment variables in your Vercel project settings:

1. Go to: https://vercel.com/muhammad-anzals-projects/frontend/settings/environment-variables

2. Add these environment variables:

### DATABASE_URL
- **Name**: `DATABASE_URL`
- **Value**: Your Neon PostgreSQL connection string
- **Example**: `postgresql://user:password@ep-xxx.us-east-2.aws.neon.tech/neondb?sslmode=require`
- **Source**: Copy from `phase-2/backend/.env`

### BETTER_AUTH_SECRET
- **Name**: `BETTER_AUTH_SECRET`
- **Value**: Your authentication secret (MUST match backend)
- **Example**: `L69lniT8/KwPvktLcQton7pJmioGOQHCQdEdKGKToiQ=`
- **Source**: Copy from `phase-2/backend/.env`

### NEXT_PUBLIC_API_URL
- **Name**: `NEXT_PUBLIC_API_URL`
- **Value**: Your backend API URL (deployed separately)
- **For now**: `http://localhost:8000` (update when backend is deployed)
- **Production**: Update to your deployed backend URL (e.g., Railway, Render, or Vercel)

3. After adding environment variables, redeploy:
```bash
cd phase-2/frontend
vercel --prod
```

## 🚀 Next Steps

### 1. Deploy Backend API
The backend needs to be deployed separately. Options:

#### Option A: Railway
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
cd phase-2/backend
railway init
railway up
```

#### Option B: Render
1. Go to https://render.com
2. Create new Web Service
3. Connect GitHub repo: Anzal-Developer/Hackathon-2
4. Root directory: `phase-2/backend`
5. Build command: `pip install -r requirements.txt`
6. Start command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
7. Add environment variables:
   - `DATABASE_URL`
   - `BETTER_AUTH_SECRET`
   - `FRONTEND_URL` (your Vercel URL)

#### Option C: Vercel (FastAPI via Serverless)
This requires additional configuration with `vercel.json` in the backend directory.

### 2. Update Frontend Environment Variable
Once backend is deployed, update `NEXT_PUBLIC_API_URL` in Vercel:
1. Go to Vercel project settings → Environment Variables
2. Update `NEXT_PUBLIC_API_URL` to your deployed backend URL
3. Redeploy the frontend

### 3. Test the Application
1. Visit: https://frontend-d6600go2w-muhammad-anzals-projects.vercel.app
2. Sign up with a test account
3. Create tasks and verify functionality
4. Test user isolation with a second account in incognito mode

## 📋 Deployment Checklist

- [x] Push code to GitHub
- [x] Configure Git with anzalaideve@gmail.com
- [x] Deploy frontend to Vercel
- [ ] Add environment variables to Vercel (DATABASE_URL, BETTER_AUTH_SECRET, NEXT_PUBLIC_API_URL)
- [ ] Deploy backend API (Railway/Render/Vercel)
- [ ] Update NEXT_PUBLIC_API_URL in Vercel
- [ ] Test full application flow
- [ ] Verify user authentication works
- [ ] Verify task CRUD operations work
- [ ] Test user isolation

## 🔗 Important Links

- **GitHub Repo**: https://github.com/Anzal-Developer/Hackathon-2
- **Frontend (Vercel)**: https://frontend-d6600go2w-muhammad-anzals-projects.vercel.app
- **Vercel Dashboard**: https://vercel.com/muhammad-anzals-projects
- **Backend**: Not yet deployed (see Next Steps)

## 📝 Notes

- The frontend build shows a database initialization warning, which is expected without environment variables
- Environment variables are NOT committed to GitHub (they're in .gitignore)
- You need to copy them from your local `.env` files to Vercel
- The backend `.env` contains the values you need

## 🆘 Troubleshooting

### "Failed to initialize database adapter" error
**Solution**: Add `DATABASE_URL` and `BETTER_AUTH_SECRET` to Vercel environment variables

### "Cannot connect to API" error
**Solution**: Deploy the backend and update `NEXT_PUBLIC_API_URL`

### Authentication not working
**Solution**: Ensure `BETTER_AUTH_SECRET` is identical in both frontend and backend

### CORS errors
**Solution**: Update backend `FRONTEND_URL` to match your Vercel deployment URL
