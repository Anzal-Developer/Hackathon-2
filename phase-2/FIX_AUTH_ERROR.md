# 🔧 Fix Better Auth Database Tables

## Problem
Better Auth needs specific database tables that might not exist yet:
- `session` - For managing user sessions
- `account` - For OAuth providers (optional)
- `verification` - For email verification

## Solution: Create Missing Tables

### Option 1: Via Neon Dashboard (Recommended)

1. Go to: https://console.neon.tech
2. Select your database: `neondb`
3. Click **SQL Editor**
4. Copy and paste this SQL:

```sql
-- Session table for Better Auth
CREATE TABLE IF NOT EXISTS session (
    id TEXT PRIMARY KEY,
    expires_at TIMESTAMP NOT NULL,
    token TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    ip_address TEXT,
    user_agent TEXT,
    user_id TEXT NOT NULL,
    CONSTRAINT session_user_id_fkey FOREIGN KEY (user_id) REFERENCES "user"(id) ON DELETE CASCADE
);

-- Account table for Better Auth
CREATE TABLE IF NOT EXISTS account (
    id TEXT PRIMARY KEY,
    account_id TEXT NOT NULL,
    provider_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    access_token TEXT,
    refresh_token TEXT,
    id_token TEXT,
    access_token_expires_at TIMESTAMP,
    refresh_token_expires_at TIMESTAMP,
    scope TEXT,
    password TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW(),
    CONSTRAINT account_user_id_fkey FOREIGN KEY (user_id) REFERENCES "user"(id) ON DELETE CASCADE
);

-- Verification table for Better Auth
CREATE TABLE IF NOT EXISTS verification (
    id TEXT PRIMARY KEY,
    identifier TEXT NOT NULL,
    value TEXT NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- Indexes
CREATE INDEX IF NOT EXISTS session_user_id_idx ON session(user_id);
CREATE INDEX IF NOT EXISTS session_token_idx ON session(token);
CREATE INDEX IF NOT EXISTS account_user_id_idx ON account(user_id);
CREATE INDEX IF NOT EXISTS verification_identifier_idx ON verification(identifier);
```

5. Click **Run** to execute

### Option 2: Via psql Command Line

```bash
# Connect to Neon database
psql "postgresql://neondb_owner:npg_q6fNnVGMktu2@ep-snowy-bush-aibnz1mh-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require"

# Then paste the SQL from above
```

## Verify Tables Exist

After creating tables, verify they exist:

```sql
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;
```

You should see:
- ✅ user
- ✅ tasks
- ✅ session
- ✅ account
- ✅ verification

## Test Authentication

After creating tables:

1. **Redeploy frontend** on Vercel (to ensure new code is deployed)
2. Visit: https://frontend-tau-sepia-80.vercel.app
3. Click **Sign up**
4. Enter email and password
5. Should work without errors! ✅

## Common Errors Fixed

### Error: relation "session" does not exist
**Fix**: Create the `session` table using SQL above

### Error: relation "account" does not exist
**Fix**: Create the `account` table using SQL above

### Error: Database connection failed
**Fix**: Check that `DATABASE_URL` in Vercel environment variables is correct

### Still Getting 404 on /api/auth/*
**Fix**:
1. Check that frontend was redeployed after code changes
2. Verify the Better Auth route exists at `app/api/auth/[...all]/route.ts`
3. Clear browser cache and try again

## Alternative: Simplified Auth (If Better Auth Doesn't Work)

If Better Auth continues to have issues, we can switch to a simpler JWT-based auth:

1. **Backend handles everything** (signup, login, JWT creation)
2. **Frontend just calls backend** endpoints
3. **No Better Auth dependency**

Let me know if you want this simpler approach!

---

**After fixing, your app flow will be:**

```
User → Sign Up → Frontend /api/auth/sign-up → Better Auth → Creates user in DB → Returns session
User → Login → Frontend /api/auth/sign-in → Better Auth → Verifies user → Returns session
User → Create Task → Backend HF Space /api/tasks → Verifies JWT → Creates task
```
