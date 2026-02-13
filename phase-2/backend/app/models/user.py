from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    """
    User model matching Better Auth schema.

    IMPORTANT: This table is managed by Better Auth on the frontend (Next.js).
    DO NOT create, update, or delete users through the backend API.

    This model exists ONLY to:
    1. Allow SQLModel to understand the table structure for foreign keys
    2. Enable tasks.user_id to reference user.id
    3. Allow read-only queries if needed (e.g., for admin features)

    Better Auth manages:
    - User creation (sign-up)
    - Password hashing and verification
    - Session management
    - Email verification
    - All user table writes
    """

    __tablename__ = "user"  # Better Auth uses singular "user" not "users"

    id: str = Field(primary_key=True, description="User ID from Better Auth")
    email: str = Field(unique=True, nullable=False, description="User email address")
    email_verified: bool = Field(default=False, description="Email verification status")
    name: Optional[str] = Field(default=None, description="User display name")
    image: Optional[str] = Field(default=None, description="User profile image URL")
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        description="Account creation timestamp"
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        description="Last update timestamp"
    )

    # Note: Better Auth stores password in a separate field that we don't access from backend
    # The backend only verifies JWT tokens, never handles passwords directly
