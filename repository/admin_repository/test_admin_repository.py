from repository.admin_repository.admin_repository import AdminRepository

def create_admin_repo():
    repo = AdminRepository()
    repo.create_admin_table()
    return repo

def test_create_admin_table():
    repo = create_admin_repo()
    result = repo.create_admin_table()
    assert result['success'] is True

def test_save_admin():
    repo = create_admin_repo()
    result = repo.save_admin("Engineer eze 1", "0101", "tambe147")
    assert result['success'] is True

def test_fetch_all_admins():
    repo = create_admin_repo()
    repo.save_admin("Engineer eze 2", "0102", "tambe147")
    result = repo.fetch_all_admins()
    assert result['success'] is True
    assert isinstance(result['data'], list)

def test_fetch_admin_by_batch_id():
    repo = create_admin_repo()
    repo.save_admin("Engineer eze 3", "0103", "tambe147")
    result = repo.fetch_admin_by_batch_id("0103")
    assert result['success'] is True
    assert result['data']['batch_id'] == "0103"

def test_update_admin():
    repo = create_admin_repo()
    repo.save_admin("Engineer eze 4", "0104", "tambe147")
    result = repo.update_admin("Engineer Tataw", "tambe", "0104")
    assert result['success'] is True