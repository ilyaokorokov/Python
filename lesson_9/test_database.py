from sqlalchemy import create_engine
from sqlalchemy import text

db_connection_string = "postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"


def test_db_connection():
    db = create_engine(db_connection_string)
    names = db.table_names()
    assert names[1] == "company"


def test_select():
    db = create_engine(db_connection_string)
    rows = db.execute("select * from company").fetchall()
    row1 = rows[0]
    assert row1[0] == 8123
    assert row1["name"] == "Lesson8"
    rowlast = rows[-1]
    assert rowlast[0] == 8121
    assert rowlast["name"] == "Муж на час"


def test_select_1_row():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where id = :company_id")

    rows = db.execute(sql_statement, company_id=8121).fetchall()

    assert len(rows) == 1
    assert rows[0]["name"] == "Муж на час"


def test_select_1_row_with_two_filters():
    db = create_engine(db_connection_string)
    sql_statement = text(
        'select * from company where "is_active" = :is_active and id >= :id'
    )

    # rows = db.execute(sql_statement, id=8134, is_active=True).fetchall()

    params = {"id": 8134, "is_active": True}
    rows = db.execute(sql_statement, params).fetchall()

    assert len(rows) == 3
    assert rows[0]["name"] == "Lesson8"


def test_insert():
    db = create_engine(db_connection_string)
    sql = text('insert into company ("name") values :NEW_NAME')
    rows = db.execute(sql, NEW_NAME="SKYPRO_TEST")


def test_update():
    db = create_engine(db_connection_string)
    sql = text("update company set name = :newest_name where id = :id")
    rows = db.execute(sql, newest_name="LALALALA", id=8138)


def test_delete():
    db = create_engine(db_connection_string)
    sql = text("delete from company where id = :id")
    rows = db.execute(sql, id=8138)
