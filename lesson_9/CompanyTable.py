from sqlalchemy import create_engine
from sqlalchemy import text


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
        )
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_companies(self):
        return self.__db.execute(self.__scripts["select"]).fetchall()

    def get_company_by_id(self, id):
        return self.__db.execute(
            self.__scripts["select_by_id"], select_id=id
        ).fetchall()

    def get_active_companies(self):
        return self.__db.execute(self.__scripts["select_only_active"]).fetchall()

    def delete(self, id):
        self.__db.execute(self.__scripts["delete_by_id"], id_to_delete=id)

    def create(self, name, descr=""):
        self.__db.execute(
            self.__scripts["insert_new"], {"new_name": name, "description": descr}
        )

    def get_max_id(self):
        return self.__db.execute(self.__scripts["get_max_id"]).fetchall()[0][0]

    def create_employee(self, first_name, last_name, email, company_id, phone):
        return self.__db.execute(
            self.__scripts["create_employee"],
            new_name=first_name,
            new_last_name=last_name,
            new_email=email,
            id_company=company_id,
            phone_number=phone,
        )

    def get_employee(self, company_id):
        return self.__db.execute(
            self.__scripts["get_employee"], id_company=company_id
        ).fetchall()

    def delete_employee(self, id):
        self.__db.execute(self.__scripts["delete_employee"], to_delete_employee=id)

    def get_employee_by_id(self, employee_id):
        return self.__db.execute(
            self.__scripts["get_employee_by_id"], id_employee=employee_id
        ).fetchall()

    def edit_employee_info(
        self, first_name, last_name, email, phone, company_id, employee_id
    ):
        self.__db.execute(
            self.__scripts["edit_employee_info"],
            first_name_employee=first_name,
            last_name_employee=last_name,
            email_employee=email,
            phone_employee=phone,
            id_company=company_id,
            id_employee=employee_id,
        )
