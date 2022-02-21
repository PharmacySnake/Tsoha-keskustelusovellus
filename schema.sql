CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    is_admin TEXT
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INTEGER REFERENCES users,
    topic_id INTEGER REFERENCES topics,
    sent_at TIMESTAMP,
    visible BOOLEAN
);

CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    title TEXT,
    user_id INTEGER REFERENCES users,
    creation_time TIMESTAMP,
    visible BOOLEAN
);
