-- =============================================
-- schema.sql - Flexible Version (Best for your CSVs)
-- Creating Tables with Referential Integrity
-- =============================================

CREATE TABLE IF NOT EXISTS course_info (
    course_id      INTEGER PRIMARY KEY,
    course_title   TEXT NOT NULL,
    created_at     TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at     TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS quiz_info (
    quiz_id         INTEGER NOT NULL,
    question_id     INTEGER NOT NULL,
    answer_id       INTEGER NOT NULL,
    answer_correct  INTEGER NOT NULL,
    created_at      TEXT DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (quiz_id, question_id, answer_id)
);

CREATE TABLE IF NOT EXISTS course_exam_info (
    exam_id          INTEGER PRIMARY KEY,
    exam_category    TEXT,
    exam_duration    INTEGER,
    created_at       TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS student_info (
    student_id        INTEGER PRIMARY KEY,
    student_country   TEXT,
    date_registered   TEXT,
    created_at        TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at        TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS student_purchases (
    purchase_id     INTEGER PRIMARY KEY,
    student_id      INTEGER NOT NULL,
    purchase_type   TEXT,
    date_purchased  TEXT NOT NULL,
    amount_paid     REAL,
    payment_method  TEXT,
    created_at      TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES student_info(student_id) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS student_learning (
    learning_id       INTEGER PRIMARY KEY,
    student_id        INTEGER NOT NULL,
    course_id         INTEGER NOT NULL,
    minutes_watched   REAL,
    date_watched      TEXT NOT NULL,
    created_at        TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES student_info(student_id) ON DELETE RESTRICT,
    FOREIGN KEY (course_id)  REFERENCES course_info(course_id) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS student_engagement (
    engagement_id       INTEGER PRIMARY KEY,
    student_id          INTEGER NOT NULL,
    engagement_quizzes  INTEGER DEFAULT 0,
    engagement_exams    INTEGER DEFAULT 0,
    engagement_lessons  INTEGER DEFAULT 0,
    date_engaged        TEXT NOT NULL,
    engagement_score    REAL,
    created_at          TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES student_info(student_id) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS student_quizzes (
    student_id     INTEGER NOT NULL,
    quiz_id        INTEGER NOT NULL,
    question_id    INTEGER NOT NULL,
    answer_id      INTEGER NOT NULL,
    attempt_date   TEXT,
    score          REAL,
    created_at     TEXT DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (student_id, quiz_id, question_id, answer_id),
    FOREIGN KEY (student_id) REFERENCES student_info(student_id) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS student_exam (
    exam_attempt_id      INTEGER PRIMARY KEY,
    student_id           INTEGER NOT NULL,
    exam_id              INTEGER NOT NULL,
    exam_result          REAL,
    exam_completion_time INTEGER,
    date_exam_completed  TEXT NOT NULL,
    created_at           TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES student_info(student_id) ON DELETE RESTRICT,
    FOREIGN KEY (exam_id)    REFERENCES course_exam_info(exam_id) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS course_ratings (
    rating_id      INTEGER PRIMARY KEY,
    course_id      INTEGER NOT NULL,
    student_id     INTEGER NOT NULL,
    course_rating  INTEGER CHECK (course_rating BETWEEN 1 AND 5),
    review_text    TEXT,
    date_rated     TEXT NOT NULL,
    created_at     TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id)  REFERENCES course_info(course_id) ON DELETE RESTRICT,
    FOREIGN KEY (student_id) REFERENCES student_info(student_id) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS student_hub_questions (
    hub_question_id     INTEGER PRIMARY KEY,
    student_id          INTEGER NOT NULL,
    course_id           INTEGER,
    question_text       TEXT,
    posted_date         TEXT,
    answer_count        INTEGER DEFAULT 0,
    is_resolved         INTEGER DEFAULT 0,
    date_question_asked TEXT NOT NULL,
    created_at          TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES student_info(student_id) ON DELETE RESTRICT,
    FOREIGN KEY (course_id)  REFERENCES course_info(course_id) ON DELETE RESTRICT
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_student_purchases_student ON student_purchases(student_id);
CREATE INDEX IF NOT EXISTS idx_student_learning_student_course ON student_learning(student_id, course_id);
CREATE INDEX IF NOT EXISTS idx_student_engagement_student_date ON student_engagement(student_id, date_engaged);
CREATE INDEX IF NOT EXISTS idx_course_ratings_course ON course_ratings(course_id);

PRAGMA foreign_keys = ON;