import sqlite3


def get_score(conn: sqlite3.Connection, person_id: int) -> int:
    cur = conn.cursor()
    cur.execute("SELECT person_score FROM person WHERE person_id = ?", (person_id,))  # type: ignore
    res = cur.fetchall()
    if len(res) == 0:
        raise ValueError("person does not exist")
    return res[0][0]


def set_score(conn: sqlite3.Connection, person_id: int, person_score: int) -> None:
    cur = conn.cursor()
    cur.execute("UPDATE person SET person_score = ? WHERE person_id = ?", (person_score, person_id))  # type: ignore
    conn.commit()


def add_new(conn: sqlite3.Connection, person_id: int) -> None:
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO person(person_id, person_score) VALUES(?, 0)", (person_id,)
    )
    conn.commit()


def get_top_scores(conn: sqlite3.Connection, count: int) -> list[tuple[int, int]]:
    cur = conn.cursor()
    cur.execute("SELECT * FROM person ORDER BY person_score DESC LIMIT ?", (count,))
    res = cur.fetchall()
    if len(res) == 0:
        raise ValueError("person table contains 0 entries")
    return res
