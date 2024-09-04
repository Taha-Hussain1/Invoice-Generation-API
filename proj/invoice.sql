CREATE TABLE Invoice (
    invoice_id          SERIAL PRIMARY KEY,
    issued_date         TEXT NOT NULL,
    due_date            TEXT NOT NULL,
    sender_name         TEXT NOT NULL,
    sender_company      TEXT,
    sender_address      TEXT,
    sender_email        TEXT,
    sender_number       TEXT,
    recipient_name      TEXT NOT NULL,
    recipient_company   TEXT,
    recipient_address   TEXT,
    recipient_email     TEXT,
    recipient_number    TEXT
);
CREATE TABLE Product (
    product_id      SERIAL PRIMARY KEY,
    invoice_id      INT REFERENCES Invoice(invoice_id) ON DELETE CASCADE,
    name            TEXT NOT NULL,
    QTY             INT CHECK (QTY >= 0),
    tax             INT CHECK (tax >= 0),
    unit_price      INT CHECK (unit_price >= 0),
    subtotal        INT CHECK (subtotal >= 0)
);