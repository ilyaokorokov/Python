from Company import Company
from Employee import Employee
from CompanyTable import CompanyTable
from faker import Faker
import pytest
import allure

fake = Faker()

company = Company("https://x-clients-be.onrender.com")
employee = Employee("https://x-clients-be.onrender.com")

db = CompanyTable(
    "postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"
)


@pytest.fixture
def fake_info():
    return {
        "company_name": fake.company(),
        "company_description": fake.word(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone_number": fake.phone_number()[:15],
    }


def delete_employee_and_company(employee_id, company_id):
    db.delete_employee(employee_id)
    db.delete_company(company_id)


def create_company(fake_info):
    db.create_company(fake_info["company_name"], fake_info["company_description"])
    id_company = db.get_max_id()
    return id_company


def create_employee(fake_info, id_company):
    db.create_employee(
        fake_info["first_name"],
        fake_info["last_name"],
        fake_info["email"],
        id_company,
        fake_info["phone_number"],
    )

@allure.feature("Сотрудники")
@allure.title("Получение списка сотрудников")
@allure.description(
    "Создаем компанию, добавляем в нее сотрудника, выполняем проверки, удаляем сотрудника и компанию"
)
@allure.severity("Blocker")
def test_get_employee_list(fake_info):
    max_id_company = create_company(fake_info)
    create_employee(fake_info, max_id_company)
    list_employee = db.get_employee(max_id_company)
    with allure.step("Получаем id номер созданного сотрудника через БД"):
        id_new_employee = list_employee[0]["id"]
    result_employee_list, status_code = employee.get_employee_list(max_id_company)
    with allure.step(
        "Проверяем, что размер списков в Апи и БД одинаков, данные сотрудника совпадают"
    ):
        assert status_code == 200
        assert len(list_employee) == len(result_employee_list)
        assert list_employee[-1][4] == fake_info["first_name"]
        assert list_employee[-1]["last_name"] == result_employee_list[-1]["lastName"]
        assert list_employee[-1]["email"] == result_employee_list[-1]["email"]
    with allure.step("Удаляем сотрудника и компанию"):
        delete_employee_and_company(id_new_employee, max_id_company)


@allure.feature("Сотрудники")
@allure.title("Получение списка сотрудников при id компании 0")
@allure.description("Получаем список сотрудников по несуществующему id номеру компании")
@allure.severity("Blocker")
def test_get_employee_list_negative():
    employee_list = db.get_employee("0")
    with allure.step("Проверяем длину списка"):
        assert len(employee_list) == 0


@allure.feature("Сотрудники")
@allure.title("Добавить сотрудника с пустыми данными")
@allure.description(
    "Создаем компанию, добавляем в нее сотрудника с пустыми полями, выполняем проверки, удаляем сотрудника и компанию"
)
@allure.severity("Blocker")
def test_add_new_employee_negative(fake_info):
    empty_field = ""
    max_id_company = create_company(fake_info)
    db.create_employee(
        empty_field, empty_field, empty_field, max_id_company, empty_field
    )
    get_employee_list_bd = db.get_employee(max_id_company)
    with allure.step("Получаем id номер созданного сотрудника через БД"):
        id_employee = get_employee_list_bd[0]["id"]
    result_employee_list, status_code = employee.get_employee_list(max_id_company)
    with allure.step(
        "Проверяем, что размер списков в Апи и БД одинаков, данные сотрудника совпадают"
    ):
        assert status_code == 200
        assert len(get_employee_list_bd) == len(result_employee_list)  # 1
        assert (
            get_employee_list_bd[-1]["first_name"]
            == result_employee_list[-1]["firstName"]
        )
    with allure.step("Удаляем сотрудника и компанию"):
        delete_employee_and_company(id_employee, max_id_company)


@allure.feature("Сотрудники")
@allure.title("Получить информацию о сотруднике по его id")
@allure.description(
    "Создаем компанию, добавляем в нее сотрудника, получаем информацию о сотруднике по его id номеру, выполняем проверки, удаляем сотрудника и компанию"
)
@allure.severity("Blocker")
def test_get_employee_by_id(fake_info):
    max_id_company = create_company(fake_info)
    create_employee(fake_info, max_id_company)
    list_employee = db.get_employee(max_id_company)
    with allure.step("Получаем id номер созданного сотрудника через БД"):
        id_new_employee_bd = list_employee[0]["id"]
    id_employee_api, status_code_api = employee.get_employee_by_id(id_new_employee_bd)
    with allure.step(
        "Проверяем, id номер сотрудника в Апи и БД одинаков, данные сотрудника совпадают, id компании идентичен"
    ):
        assert status_code_api == 200
        assert id_new_employee_bd == id_employee_api["id"]
        assert id_employee_api["firstName"] == fake_info["first_name"]
        assert id_employee_api["lastName"] == fake_info["last_name"]
        assert id_employee_api["email"] == fake_info["email"]
        assert id_employee_api["companyId"] == max_id_company
    with allure.step("Удаляем сотрудника и компанию"):
        delete_employee_and_company(id_new_employee_bd, max_id_company)


@allure.feature("Сотрудники")
@allure.title("Изменить информацию о сотруднике по его id")
@allure.description(
    "Создаем компанию, добавляем в нее сотрудника, создаем вторую компанию, вносим изменения в данные сотруднкиа, выполняем проверки, удаляем сотрудника и компании"
)
@allure.severity("Blocker")
def test_change_employee_info(fake_info):
    employee_name = "Ольга"
    employee_last_name = "Катамарановна"
    employee_email = "test@te.te"
    employee_phone = "79899899899"
    first_company = create_company(fake_info)
    db.create_employee(
        fake_info["first_name"],
        fake_info["last_name"],
        fake_info["email"],
        first_company,
        fake_info["phone_number"],
    )
    list_employee = db.get_employee(first_company)
    with allure.step("Получаем id номер созданного сотрудника через БД"):
        id_new_employee_bd = list_employee[-1]["id"]
    second_company = create_company(fake_info)
    db.edit_employee_info(
        employee_name,
        employee_last_name,
        employee_email,
        employee_phone,
        second_company,
        id_new_employee_bd,
    )
    changed_employee = db.get_employee(second_company)
    with allure.step("Проверяем, что изменения в данных сотрудника были внесены"):
        assert changed_employee[0]["first_name"] == employee_name
        assert changed_employee[0]["last_name"] == employee_last_name
        assert changed_employee[0]["email"] == employee_email
        assert changed_employee[0]["phone"] == employee_phone
        assert changed_employee[0]["company_id"] == second_company
    with allure.step("Удаляем сотрудника и компании"):
        db.delete_employee(id_new_employee_bd)
        db.delete_company(first_company)
        db.delete_company(second_company)


@allure.feature("Сотрудники")
@allure.title(
    "Изменить информацию о сотруднике по его id, оставить обязательные поля пустыми"
)
@allure.description(
    "Создаем компанию, добавляем в нее сотрудника, создаем вторую компанию, вносим изменения в данные сотруднкиа, выполняем проверки, удаляем сотрудника и компании"
)
@allure.severity("Blocker")
def test_change_employee_info_negative(fake_info):
    empty_field = ""
    first_company = create_company(fake_info)
    db.create_employee(
        fake_info["first_name"],
        fake_info["last_name"],
        fake_info["email"],
        first_company,
        fake_info["phone_number"],
    )
    list_employee = db.get_employee(first_company)
    with allure.step("Получаем id номер созданного сотрудника через БД"):
        id_new_employee_bd = list_employee[-1]["id"]
    db.create_company("Second", "Company")
    second_company = db.get_max_id()
    db.edit_employee_info(
        empty_field,
        empty_field,
        empty_field,
        empty_field,
        second_company,
        id_new_employee_bd,
    )
    changed_employee = db.get_employee(second_company)
    api_result_employee_list_second_company, status_code_second = (
        employee.get_employee_list(second_company)
    )
    with allure.step("Проверяем через Апи, что обязательные поля пустые"):
        assert status_code_second == 200
        assert (
            api_result_employee_list_second_company[0]["firstName"]
            == changed_employee[0]["first_name"]
        )
        assert (
            api_result_employee_list_second_company[0]["lastName"]
            == changed_employee[0]["last_name"]
        )
        assert (
            api_result_employee_list_second_company[0]["email"]
            == changed_employee[0]["email"]
        )
        assert (
            api_result_employee_list_second_company[0]["phone"]
            == changed_employee[0]["phone"]
        )
        assert api_result_employee_list_second_company[0]["companyId"] == second_company
    with allure.step("Удаляем сотрудника и компании"):
        db.delete_employee(id_new_employee_bd)
        db.delete_company(first_company)
        db.delete_company(second_company)
