from Company import Company
from Auth import Auth
from Employee import Employee
import pytest

auth = Auth("https://x-clients-be.onrender.com")
company = Company("https://x-clients-be.onrender.com")
employee = Employee("https://x-clients-be.onrender.com")


@pytest.fixture()
def company_id():
    auth.auth_user()
    create_company = company.create_company("Lesson8", "Homework")
    id_company = create_company["id"]
    yield id_company


def test_get_employee_list(company_id):
    id_company = company_id
    result_employee_list, status_code = employee.get_employee_list(id_company)
    assert status_code == 200
    assert len(result_employee_list) == 0
    result_add_employee, status_code_employee = employee.add_new_employee(
        "Илья", "Окороков", id_company, "ilyaok_krd@mail.ru"
    )
    assert status_code_employee == 201
    id_employee = result_add_employee["id"]
    result_employee_list_update, _ = employee.get_employee_list(id_company)
    assert len(result_employee_list_update) == len(result_employee_list) + 1
    assert id_employee == result_employee_list_update[-1]["id"]


def test_get_employee_list_negative():
    result_employee_list, status_code = employee.get_employee_list("0")
    assert status_code == 200
    assert len(result_employee_list) == 0


def test_add_new_employee_negative(company_id):
    id_company = company_id
    result_add_employee, status_code_employee = employee.add_new_employee(
        "", "", id_company, ""
    )
    assert status_code_employee == 400
    assert result_add_employee["message"] == [
        "firstName should not be empty",
        "lastName should not be empty",
        "email must be an email",
    ]
    assert result_add_employee["error"] == "Bad Request"


def test_get_employee_by_id(company_id):
    id_company = company_id
    result_add_employee, status_code_employee = employee.add_new_employee(
        "Илья", "Окороков", id_company, "ilyaok_krd@mail.ru"
    )
    assert status_code_employee == 201
    id_employee = result_add_employee["id"]

    result_get_employee, status_code_get_employee = employee.get_employee_by_id(
        id_employee
    )
    assert status_code_get_employee == 200
    assert result_get_employee["id"] == id_employee
    assert result_get_employee["firstName"] == "Илья"
    assert result_get_employee["lastName"] == "Окороков"
    print(result_get_employee)
    assert result_get_employee["email"] == "ilyaok_krd@mail.ru"
    assert result_get_employee["companyId"] == id_company


def test_change_employee_info(company_id):
    id_company = company_id
    result_add_employee, status_code_employee = employee.add_new_employee(
        "Екатерина", "Катамаранова", id_company, "katkat@ka.ka"
    )
    assert status_code_employee == 201
    id_employee = result_add_employee["id"]
    print(result_add_employee)
    result_change_employee_info, change_employee_status_code = (
        employee.edit_employee_info(id_employee, "Каштанова", "kashakatka@kas.ka")
    )
    print(result_change_employee_info)
    assert change_employee_status_code == 200
    assert result_change_employee_info["id"] == id_employee
    assert result_change_employee_info["email"] == "kashakatka@kas.ka"
    assert result_change_employee_info["url"] == ""

    result_get_employee, status_code_get_employee = employee.get_employee_by_id(
        id_employee
    )
    print(result_get_employee)
    print(status_code_get_employee)
    assert status_code_get_employee == 200
    assert result_get_employee["lastName"] == "Каштанова"


def test_change_employee_info_negative(company_id):
    id_company = company_id
    result_add_employee, status_code_employee = employee.add_new_employee(
        "Мрак", "Карловиц", id_company, "carlovick@ka.ka"
    )
    assert status_code_employee == 201
    id_employee = result_add_employee["id"]

    result_change_employee_info_negative, change_employee_status_code_negative = (
        employee.edit_employee_info(id_employee, "", "str")
    )
    assert change_employee_status_code_negative == 400
    assert result_change_employee_info_negative["message"] == [
        "lastName should not be empty",
        "email must be an email",
    ]
    assert result_change_employee_info_negative["error"] == "Bad Request"
