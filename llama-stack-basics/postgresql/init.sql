DO
$$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'llamastack') THEN
        CREATE DATABASE llamastack OWNER citrus;
    END IF;
END
$$;

CREATE EXTENSION IF NOT EXISTS vector;
