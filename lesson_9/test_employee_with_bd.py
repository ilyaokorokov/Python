from Company import Company
from Employee import Employee
from CompanyTable import CompanyTable

company = Company("https://x-clients-be.onrender.com")
employee = Employee("https://x-clients-be.onrender.com")

db = CompanyTable(
    "postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"
)


def test_get_employee_list():
    db.create("Skypro", "Employee")
    max_id_company = db.get_max_id()

    db.create_employee(
        "Илья", "Окороков", "ilyatest@tt.tt", max_id_company, "79892697070"
    )
    list_employee = db.get_employee(max_id_company)
    id_new_employee = list_employee[0]["id"]

    result_employee_list, status_code = employee.get_employee_list(max_id_company)

    assert status_code == 200
    assert len(list_employee) == len(result_employee_list)
    assert list_employee[-1][4] == "Илья"
    assert list_employee[-1]["last_name"] == result_employee_list[-1]["lastName"]
    assert list_employee[-1]["email"] == result_employee_list[-1]["email"]

    db.delete_employee(id_new_employee)
    db.delete(max_id_company)


def test_get_employee_list_negative():
    employee_list = db.get_employee("0")
    assert len(employee_list) == 0


def test_add_new_employee_negative():
    db.create("Skypro", "Employee")
    max_id_company = db.get_max_id()
    db.create_employee("", "", "", max_id_company, "")

    get_employee_list_bd = db.get_employee(max_id_company)
    id_employee = get_employee_list_bd[0]["id"]
    result_employee_list, status_code = employee.get_employee_list(max_id_company)

    assert status_code == 200
    assert len(get_employee_list_bd) == len(result_employee_list)  # 1
    assert (
        get_employee_list_bd[-1]["first_name"] == result_employee_list[-1]["firstName"]
    )
    db.delete_employee(id_employee)
    db.delete(max_id_company)


def test_get_employee_by_id():
    db.create("Skypro", "Employee")
    max_id_company = db.get_max_id()

    db.create_employee(
        "Илья", "Окороков", "ilyatest@tt.tt", max_id_company, "79892697070"
    )
    list_employee = db.get_employee(max_id_company)
    id_new_employee_bd = list_employee[0]["id"]

    id_employee_api, status_code_api = employee.get_employee_by_id(id_new_employee_bd)
    assert status_code_api == 200
    assert id_new_employee_bd == id_employee_api["id"]
    assert id_employee_api["firstName"] == "Илья"
    assert id_employee_api["lastName"] == "Окороков"
    assert id_employee_api["email"] == "ilyatest@tt.tt"
    assert id_employee_api["companyId"] == max_id_company
    db.delete_employee(id_new_employee_bd)
    db.delete(max_id_company)


def test_change_employee_info():
    db.create("First", "Company")
    first_company = db.get_max_id()
    db.create_employee(
        "Илья", "Окороков", "ilyatest@tt.tt", first_company, "79892697070"
    )
    list_employee = db.get_employee(first_company)
    id_new_employee_bd = list_employee[-1]["id"]
    api_result_employee_list_first_company, status_code_first = (
        employee.get_employee_list(first_company)
    )
    assert status_code_first == 200
    assert api_result_employee_list_first_company[0]["companyId"] == first_company

    db.create("Second", "Company")
    second_company = db.get_max_id()
    db.edit_employee_info(
        "Ольга",
        "Катамарановна",
        "test@te.te",
        "79899899899",
        second_company,
        id_new_employee_bd,
    )
    changed_employee = db.get_employee(second_company)
    api_result_employee_list_second_company, status_code_second = (
        employee.get_employee_list(second_company)
    )
    assert status_code_second == 200
    assert changed_employee[0]["first_name"] == "Ольга"
    assert changed_employee[0]["last_name"] == "Катамарановна"
    assert changed_employee[0]["email"] == "test@te.te"
    assert changed_employee[0]["phone"] == "79899899899"
    assert changed_employee[0]["company_id"] == second_company


def test_change_employee_info_negative():
    db.create("First", "Company")
    first_company = db.get_max_id()
    db.create_employee(
        "Илья", "Окороков", "ilyatest@tt.tt", first_company, "79892697070"
    )
    list_employee = db.get_employee(first_company)
    id_new_employee_bd = list_employee[-1]["id"]
    api_result_employee_list_first_company, status_code_first = (
        employee.get_employee_list(first_company)
    )
    assert status_code_first == 200
    assert api_result_employee_list_first_company[0]["companyId"] == first_company

    db.create("Second", "Company")
    second_company = db.get_max_id()
    db.edit_employee_info(
        "",
        "",
        "",
        "",
        second_company,
        id_new_employee_bd,
    )
    changed_employee = db.get_employee(second_company)
    
    api_result_employee_list_second_company, status_code_second = (
        employee.get_employee_list(second_company)
    )
    assert status_code_second == 200
    assert api_result_employee_list_second_company[0]["firstName"] == changed_employee[0]["first_name"]
    assert api_result_employee_list_second_company[0]["lastName"] == changed_employee[0]["last_name"]
    assert api_result_employee_list_second_company[0]["email"] == changed_employee[0]["email"]
    assert api_result_employee_list_second_company[0]["phone"] == changed_employee[0]["phone"]
    assert api_result_employee_list_second_company[0]["companyId"] == second_company