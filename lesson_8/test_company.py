from Company import Company
from Auth import Auth

auth = Auth("https://x-clients-be.onrender.com")
company = Company("https://x-clients-be.onrender.com")


def test_get_companies():
    body = company.get_company_list()
    assert len(body) > 0


def test_get_active_companies():
    full_company_list = company.get_company_list()
    active_company_list = company.get_company_list(params_to_add={"active": "true"})
    assert len(full_company_list) > len(active_company_list)


def test_add_new_company():
    full_company_list = company.get_company_list()
    len_before = len(full_company_list)
    name_company = "Test_name"
    description_company = "Test_description"
    new_company = company.create_company(name_company, description_company)
    new_id = new_company["id"]
    full_company_list = company.get_company_list()
    len_after = len(full_company_list)
    assert len_after - len_before == 1
    assert full_company_list[-1]["name"] == name_company
    assert full_company_list[-1]["description"] == description_company
    assert full_company_list[-1]["id"] == new_id


def test_get_one_company_id():
    name_company = "VS Code"
    description_company = "IDE"
    new_company = company.create_company(name_company, description_company)
    new_id = new_company["id"]
    new_company_get_id = company.get_company_id(new_id)
    assert new_company_get_id["id"] == new_id
    assert new_company_get_id["name"] == name_company
    assert new_company_get_id["description"] == description_company
    assert new_company_get_id["isActive"] == True


def test_edit_company():
    name_company = "Company to be edited"
    description_company = "Edit me"
    new_company = company.create_company(name_company, description_company)
    new_id = new_company["id"]
    new_name_company = "Updated"
    new_description_company = "_upd_"
    edited_company = company.edit_company(
        new_id, new_name_company, new_description_company
    )
    assert edited_company["id"] == new_id
    assert edited_company["name"] == new_name_company
    assert edited_company["description"] == new_description_company
    assert edited_company["isActive"] == True


def test_delete_company():
    name_company = "Company to be deleted"
    description_company = "Delete me"
    new_company = company.create_company(name_company, description_company)
    new_id = new_company["id"]
    deleted_company = company.delete_company(new_id)
    assert deleted_company["id"] == new_id
    assert deleted_company["name"] == name_company
    assert deleted_company["description"] == description_company
    assert deleted_company["isActive"] == True
    new_company_list = company.get_company_list()
    assert new_company_list[-1]["id"] != new_id


def test_deactivate_company():
    name_company = "Company to be deactivated"
    description_company = "Diactivate me!"
    new_company = company.create_company(name_company, description_company)
    new_id = new_company["id"]
    result_deactivate_company = company.set_active_state(new_id, False)
    assert result_deactivate_company["isActive"] == False


def test_deactivate_and_activate_back():
    name_company = "Company to be deactivated and activated"
    description_company = "Activate me!"
    new_company = company.create_company(name_company, description_company)
    new_id = new_company["id"]
    company.set_active_state(new_id, False)
    result_deactivate_and_activate_company = company.set_active_state(new_id, True)
    assert result_deactivate_and_activate_company["isActive"] == True
