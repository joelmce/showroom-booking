CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(80) UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    admin BOOLEAN,
);

CREATE TABLE bookings (
    booking_id SERIAL PRIMARY KEY,
    owner_id INT,
    date TIMESTAMP,
    CONSTRAINT fk_user
        FOREIGN KEY(owner_id)
            REFERENCES users(user_id)
);

INSERT INTO users (name, email, password) VALUES ('Joel', 'joelanthony.mac@gmail.com', 'TestPassword123', True);
INSERT INTO bookings (owner_id, date) VALUES (1, '2001-09-28 03:00:00');