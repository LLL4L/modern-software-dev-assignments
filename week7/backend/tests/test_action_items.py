def _create_items(client, count):
    items = []
    for i in range(count):
        r = client.post("/action-items/", json={"description": f"Item {i}"})
        assert r.status_code == 201
        items.append(r.json())
    return items


def test_create_complete_list_and_patch_action_item(client):
    payload = {"description": "Ship it"}
    r = client.post("/action-items/", json=payload)
    assert r.status_code == 201, r.text
    item = r.json()
    assert item["completed"] is False
    assert "created_at" in item and "updated_at" in item

    r = client.put(f"/action-items/{item['id']}/complete")
    assert r.status_code == 200
    done = r.json()
    assert done["completed"] is True

    r = client.get("/action-items/", params={"completed": True, "limit": 5, "sort": "-created_at"})
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

    r = client.patch(f"/action-items/{item['id']}", json={"description": "Updated"})
    assert r.status_code == 200
    patched = r.json()
    assert patched["description"] == "Updated"


def test_list_items_pagination_skip_limit(client):
    _create_items(client, 5)
    r = client.get("/action-items/", params={"skip": 2, "limit": 2, "sort": "-id"})
    assert r.status_code == 200
    assert len(r.json()) == 2


def test_list_items_pagination_limit(client):
    _create_items(client, 5)
    r = client.get("/action-items/", params={"limit": 3, "sort": "-id"})
    assert r.status_code == 200
    assert len(r.json()) <= 3


def test_list_items_pagination_skip_beyond(client):
    _create_items(client, 2)
    r = client.get("/action-items/", params={"skip": 100})
    assert r.status_code == 200
    assert r.json() == []


def test_list_items_sort_descending(client):
    _create_items(client, 3)
    r = client.get("/action-items/", params={"sort": "-id"})
    assert r.status_code == 200
    ids = [item["id"] for item in r.json()]
    assert ids == sorted(ids, reverse=True)


def test_list_items_sort_ascending(client):
    _create_items(client, 3)
    r = client.get("/action-items/", params={"sort": "id"})
    assert r.status_code == 200
    ids = [item["id"] for item in r.json()]
    assert ids == sorted(ids)


def test_list_items_sort_by_description(client):
    _create_items(client, 3)
    r = client.get("/action-items/", params={"sort": "description"})
    assert r.status_code == 200
    descs = [item["description"] for item in r.json()]
    assert descs == sorted(descs)


def test_list_items_invalid_sort(client):
    _create_items(client, 2)
    r = client.get("/action-items/", params={"sort": "nonexistent_field"})
    assert r.status_code == 200
    assert len(r.json()) >= 2


def test_list_items_filter_completed(client):
    _create_items(client, 2)
    client.put(f"/action-items/{1}/complete")

    r = client.get("/action-items/", params={"completed": True})
    assert r.status_code == 200
    assert all(item["completed"] for item in r.json())

    r = client.get("/action-items/", params={"completed": False})
    assert r.status_code == 200
    assert all(not item["completed"] for item in r.json())
