import allure
from sqlalchemy import create_engine
from sqlalchemy.sql import text


class CompanyTable:

    __scripts = {
        "select": "select * from company where deleted_at is NULL",
        "select_by_id": text("select * from company where id = :select_id"),
        "select_only_active": 'select * from company where "is_active" = True and "deleted_at" is NULL',
        "delete_by_id": text("delete from company where id = :id_to_delete"),
        "insert_new": text(
            'INSERT INTO company ("name", "description") VALUES (:new_name, :description)'
        ),
        "get_max_id": "select MAX(id) from company",
        "get_employee": text('select * from employee where "company_id" = :id_company'),
        "create_employee": text(
            'insert into employee ("first_name", "last_name", "email", "company_id", "phone") VALUES (:new_name, :new_last_name, :new_email, :id_company, :phone_number)'
        ),
        "delete_employee": text(
            'delete from employee where "id" = :to_delete_employee'
        ),
        "get_employee_by_id": text('select * from employee where "id" = :id_employee'),
        "edit_employee_info": text(
            "UPDATE employee SET first_name = :first_name_employee, last_name = :last_name_employee, email = :email_employee, phone = :phone_employee, company_id = :id_company WHERE id = :id_employee"
        ),
    }

    def __init__(self, connection_string: str):
        self.__db = create_engine(connection_string)

    @allure.step("База данных. Получить список компаний.")
    def get_companies(self) -> list:
        """
        Получение списка компаний через отправку запроса в базу данных.

        Returns:
            list: Список компаний
        """
        query = self.__db.execute(self.__scripts["select"])
        allure.attach(
            str(query.context.cursor.query), "SQL", allure.attachment_type.TEXT
        )
        return query.fetchall()

    @allure.step("База данных. Получить компанию по id номеру - {id}")
    def get_company_by_id(self, id: int) -> list:
        """Получение информации о компании по её id номеру
        через отправку запроса в базу данных.

        Args:
            id (int): id номер компании

        Returns:
            list: список из 1-ой компании
        """
        query = self.__db.execute(self.__scripts["select_by_id"], select_id=id)
        allure.attach(
            str(query.context.cursor.query), "SQL", allure.attachment_type.TEXT
        )
        return query.fetchall()

    @allure.step("База данных. Получить список активных компаний.")
    def get_active_companies(self) -> list:
        """Получить список активных компаний через отправку запроса в базу данных.

        Returns:
            list: Список активных компаний
        """
        query = self.__db.execute(self.__scripts["select_only_active"])
        allure.attach(
            str(query.context.cursor.query), "SQL", allure.attachment_type.TEXT
        )
        return query.fetchall()

    @allure.step("База данных. Удалить компанию по её id номеру - {id}")
    def delete_company(self, id: int):
        """Удалить компанию по её id номеру через отправку запроса в базу данных.

        Args:
            id (int): id номер компании
        """
        self.__db.execute(self.__scripts["delete_by_id"], id_to_delete=id)

    @allure.step("База данных. Создать компанию: название - {name}, описание - {descr}")
    def create_company(self, name: str, descr: str):
        """Создать новую компанию через отправку запроса в базу данных.

        Args:
            name (str): название компании
            descr (str): описание компании
        """
        self.__db.execute(
            self.__scripts["insert_new"], {"new_name": name, "description": descr}
        )

    @allure.step("База данных. Получить максимальный id номер")
    def get_max_id(self) -> int:
        """Получить id номер последней созданной компании
        через отправку запроса в базу данных.

        Returns:
            int: id номер последней созданной компании
        """
        return self.__db.execute(self.__scripts["get_max_id"]).fetchall()[0][0]

    @allure.step(
        "База данных. Добавить сотрудника в компанию. Имя - {first_name}, фамилия - {last_name}, электронная почта - {email}, id номер компании - {company_id}, номер телефона - {phone}"
    )
    def create_employee(
        self, first_name: str, last_name: str, email: str, company_id: int, phone: str
    ) -> list:
        """Добавить сотрудника в компанию через отправку запроса в базу данных.

        Args:
            first_name (str): имя
            last_name (str): фамилия
            email (str): адрес электронной почты
            company_id (int): id номер компании
            phone (str): номер телефона

        Returns:
            list: список сотрудников
        """
        return self.__db.execute(
            self.__scripts["create_employee"],
            new_name=first_name,
            new_last_name=last_name,
            new_email=email,
            id_company=company_id,
            phone_number=phone,
        )

    @allure.step("База данных. Получить список сотрудников по id номеру компании.")
    def get_employee(self, company_id: int) -> list:
        """Получить список сотрудников по id номеру компании
        через отправку запроса в базу данных.

        Args:
            company_id (int): id номер компании

        Returns:
            list: список сотрудников компании
        """
        return self.__db.execute(
            self.__scripts["get_employee"], id_company=company_id
        ).fetchall()

    @allure.step("База данных. Удалить сотрудника по его id номеру.")
    def delete_employee(self, id: int):
        """Удалить сотрудника по его id номеру
        через отправку запроса в базу данных.

        Args:
            id (int): id номер сотрудника
        """
        self.__db.execute(self.__scripts["delete_employee"], to_delete_employee=id)

    @allure.step("База данных. Получить информацию о сотруднике по его id номеру")
    def get_employee_by_id(self, employee_id: int) -> list:
        """Получить информацию о сотруднике по его id номеру
        через отправку запроса в базу данных

        Args:
            employee_id (int): id номер сотрудника

        Returns:
            list: список сотрудников
        """
        return self.__db.execute(
            self.__scripts["get_employee_by_id"], id_employee=employee_id
        ).fetchall()

    @allure.step("База данных. Изменить информацию о сотруднике.")
    def edit_employee_info(
        self,
        first_name: str,
        last_name: str,
        email: str,
        phone: str,
        company_id: int,
        employee_id: int,
    ) -> list:
        """Изменить информацию о сотруднике через отправку запроса в базу данных.

        Args:
            first_name (str): имя
            last_name (str): фамилия
            email (str): адрес электронной почты
            phone (str): номер телефона
            company_id (int): id номер компании
            employee_id (int): id номер сотрудника

        Returns:
            list: список сотрудников
        """
        self.__db.execute(
            self.__scripts["edit_employee_info"],
            first_name_employee=first_name,
            last_name_employee=last_name,
            email_employee=email,
            phone_employee=phone,
            id_company=company_id,
            id_employee=employee_id,
        )
