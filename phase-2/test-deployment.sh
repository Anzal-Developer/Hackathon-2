#!/bin/bash

# Deployment Testing Script
# Tests both frontend and backend are working correctly

BACKEND_URL="https://backend-dusky-mu-33.vercel.app"
FRONTEND_URL="https://frontend-tau-sepia-80.vercel.app"

echo "========================================="
echo "Testing NestTask Deployment"
echo "========================================="
echo ""

# Test 1: Backend Health Check
echo "1. Testing Backend Health..."
HEALTH=$(curl -s "$BACKEND_URL/health")
if echo "$HEALTH" | grep -q "ok"; then
    echo "✅ Backend health check passed: $HEALTH"
else
    echo "❌ Backend health check failed"
    exit 1
fi
echo ""

# Test 2: Backend Root Endpoint
echo "2. Testing Backend Root Endpoint..."
ROOT=$(curl -s "$BACKEND_URL/")
if echo "$ROOT" | grep -q "healthy"; then
    echo "✅ Backend root endpoint passed: $ROOT"
else
    echo "❌ Backend root endpoint failed"
    exit 1
fi
echo ""

# Test 3: Frontend Accessibility
echo "3. Testing Frontend Accessibility..."
FRONTEND_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$FRONTEND_URL")
if [ "$FRONTEND_STATUS" = "200" ]; then
    echo "✅ Frontend is accessible (HTTP 200)"
else
    echo "❌ Frontend returned HTTP $FRONTEND_STATUS"
    exit 1
fi
echo ""

# Test 4: Backend Auth Middleware (should return 401)
echo "4. Testing Backend Auth Middleware..."
AUTH_TEST=$(curl -s -w "\n%{http_code}" "$BACKEND_URL/api/tasks")
if echo "$AUTH_TEST" | grep -q "401"; then
    echo "✅ Auth middleware working (401 Unauthorized as expected)"
else
    echo "❌ Auth middleware not working properly"
    echo "Response: $AUTH_TEST"
fi
echo ""

# Test 5: CORS Headers
echo "5. Testing CORS Configuration..."
CORS_TEST=$(curl -s -I -H "Origin: $FRONTEND_URL" "$BACKEND_URL/health" | grep -i "access-control")
if [ -n "$CORS_TEST" ]; then
    echo "✅ CORS headers present:"
    echo "$CORS_TEST"
else
    echo "⚠️  No CORS headers found (might be ok for some endpoints)"
fi
echo ""

# Test 6: Better Auth Endpoint
echo "6. Testing Better Auth API..."
AUTH_API=$(curl -s -w "\n%{http_code}" "$FRONTEND_URL/api/auth/session")
AUTH_STATUS=$(echo "$AUTH_API" | tail -1)
if [ "$AUTH_STATUS" = "200" ] || [ "$AUTH_STATUS" = "401" ]; then
    echo "✅ Better Auth API responding (HTTP $AUTH_STATUS)"
else
    echo "⚠️  Better Auth API returned HTTP $AUTH_STATUS"
fi
echo ""

echo "========================================="
echo "Summary"
echo "========================================="
echo "Backend URL: $BACKEND_URL"
echo "Frontend URL: $FRONTEND_URL"
echo ""
echo "✅ All critical tests passed!"
echo ""
echo "Next Steps:"
echo "1. Visit: $FRONTEND_URL"
echo "2. Click 'Sign up' to create an account"
echo "3. Create, edit, and manage tasks"
echo "4. Test in incognito mode with a second user to verify isolation"
echo ""
