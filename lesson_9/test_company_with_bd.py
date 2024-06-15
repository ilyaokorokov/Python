from Company import Company
from Auth import Auth
from CompanyTable import CompanyTable

auth = Auth("https://x-clients-be.onrender.com")
company = Company("https://x-clients-be.onrender.com")

db = CompanyTable(
    "postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"
)


def test_get_companies():
    api_result = company.get_company_list()
    db_result = db.get_companies()
    assert len(api_result) == len(db_result) # В базе строка не удаляется, ей присваивается значение в поле Deleted_at


def test_get_active_companies():
    active_company_list = company.get_company_list(params_to_add={"active": "true"})
    db_list = db.get_active_companies()
    assert len(active_company_list) == len(db_list)


def test_add_new_company():
    full_company_list = company.get_company_list()
    len_before = len(full_company_list)
    name_company = "Test_name"
    description_company = "Test_description"
    new_company = company.create_company(name_company, description_company)
    new_id = new_company["id"]

    full_company_list = company.get_company_list()
    len_after = len(full_company_list)

    db.delete(new_id)
    assert len_after - len_before == 1
    for company_one in full_company_list:
        if company_one["id"] == new_id:
            assert full_company_list[-1]["name"] == name_company
            assert full_company_list[-1]["description"] == description_company
            assert full_company_list[-1]["id"] == new_id


def test_get_one_company_id():
    db.create("skypro", "nanana")
    max_id = db.get_max_id()

    new_company_get_id = company.get_company_id(max_id)

    db.delete(max_id)

    assert new_company_get_id["id"] == max_id
    assert new_company_get_id["name"] == "skypro"
    assert new_company_get_id["description"] == "nanana"
    assert new_company_get_id["isActive"] == True


def test_edit_company():
    db.create("skypro", "nanana")
    max_id = db.get_max_id()

    new_name_company = "Updated"
    new_description_company = "_upd_"
    edited_company = company.edit_company(
        max_id, new_name_company, new_description_company
    )
    db.delete(max_id)
    assert edited_company["id"] == max_id
    assert edited_company["name"] == new_name_company
    assert edited_company["description"] == new_description_company
    assert edited_company["isActive"] == True


def test_delete_company():
    db.create("TEST_DELETE", "DELETE")
    max_id = db.get_max_id()

    deleted_company = company.delete_company(max_id)

    assert deleted_company["id"] == max_id
    assert deleted_company["name"] == "TEST_DELETE"
    assert deleted_company["description"] == "DELETE"
    assert deleted_company["isActive"] == True

    rows = db.get_company_by_id(max_id)
    assert len(rows) == 1
    # assert rows[0]["deleted_at"] is None


def test_deactivate_company():
    db.create("skypro", "nanana")
    max_id = db.get_max_id()
    result_deactivate_company = company.set_active_state(max_id, False)

    db.delete(max_id)

    assert result_deactivate_company["isActive"] == False


def test_deactivate_and_activate_back():
    db.create("skypro", "nanana")
    max_id = db.get_max_id()
    result_deactivate_and_activate_company = company.set_active_state(max_id, True)

    company.set_active_state(max_id, False)

    db.delete(max_id)
    assert result_deactivate_and_activate_company["isActive"] == True
