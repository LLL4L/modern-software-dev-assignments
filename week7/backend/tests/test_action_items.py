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


def test_get_single_action_item(client):
    r = client.post("/action-items/", json={"description": "Fetch me"})
    assert r.status_code == 201
    item_id = r.json()["id"]

    r = client.get(f"/action-items/{item_id}")
    assert r.status_code == 200
    assert r.json()["description"] == "Fetch me"


def test_get_action_item_not_found(client):
    r = client.get("/action-items/99999")
    assert r.status_code == 404


def test_delete_action_item(client):
    r = client.post("/action-items/", json={"description": "Delete me"})
    assert r.status_code == 201
    item_id = r.json()["id"]

    r = client.delete(f"/action-items/{item_id}")
    assert r.status_code == 204

    r = client.get(f"/action-items/{item_id}")
    assert r.status_code == 404


def test_delete_action_item_not_found(client):
    r = client.delete("/action-items/99999")
    assert r.status_code == 404


def test_complete_action_item_not_found(client):
    r = client.put("/action-items/99999/complete")
    assert r.status_code == 404


def test_patch_action_item_not_found(client):
    r = client.patch("/action-items/99999", json={"description": "Nope"})
    assert r.status_code == 404


def test_create_action_item_validation_empty(client):
    r = client.post("/action-items/", json={"description": ""})
    assert r.status_code == 422


def test_create_action_item_validation_missing(client):
    r = client.post("/action-items/", json={})
    assert r.status_code == 422
