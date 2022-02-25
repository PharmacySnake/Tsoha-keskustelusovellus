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
    thread_id INTEGER REFERENCES threads,
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

CREATE TABLE threads (
    id SERIAL PRIMARY KEY,
    message_id INTEGER REFERENCES messages,
    visible BOOLEAN
);

CREATE TABLE importance (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    points INTEGER
);

