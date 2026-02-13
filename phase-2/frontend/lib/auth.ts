import { betterAuth } from "better-auth";
import { Kysely } from "kysely";
import { PostgresJSDialect } from "kysely-postgres-js";
import postgres from "postgres";

const sql = postgres(process.env.DATABASE_URL!, {
  ssl: "require",
  max: 1,
});

const db = new Kysely<Record<string, Record<string, unknown>>>({
  dialect: new PostgresJSDialect({ postgres: sql }),
});

export const auth = betterAuth({
  database: db,
  emailAndPassword: {
    enabled: true,
  },
  secret: process.env.BETTER_AUTH_SECRET!,
  baseURL: process.env.NEXT_PUBLIC_APP_URL || "http://localhost:3000",
});
