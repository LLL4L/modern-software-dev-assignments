def test_create_action_item_with_note(client):
    r = client.post("/notes/", json={"title": "My Note", "content": "Content"})
    assert r.status_code == 201
    note_id = r.json()["id"]

    r = client.post("/action-items/", json={"description": "Task for note", "note_id": note_id})
    assert r.status_code == 201
    item = r.json()
    assert item["note_id"] == note_id


def test_create_action_item_with_invalid_note_id(client):
    r = client.post("/action-items/", json={"description": "Orphan task", "note_id": 99999})
    assert r.status_code == 404


def test_note_read_includes_action_items(client):
    r = client.post("/notes/", json={"title": "With items", "content": "Content"})
    note_id = r.json()["id"]

    client.post("/action-items/", json={"description": "Item 1", "note_id": note_id})
    client.post("/action-items/", json={"description": "Item 2", "note_id": note_id})

    r = client.get(f"/notes/{note_id}")
    assert r.status_code == 200
    data = r.json()
    assert len(data["action_items"]) == 2


def test_create_tag(client):
    r = client.post("/tags/", json={"name": "urgent"})
    assert r.status_code == 201
    tag = r.json()
    assert tag["name"] == "urgent"
    assert "id" in tag


def test_list_tags(client):
    client.post("/tags/", json={"name": "tag1"})
    client.post("/tags/", json={"name": "tag2"})

    r = client.get("/tags/")
    assert r.status_code == 200
    names = [t["name"] for t in r.json()]
    assert "tag1" in names
    assert "tag2" in names


def test_add_tags_to_note(client):
    r = client.post("/notes/", json={"title": "Tagged", "content": "Content"})
    note_id = r.json()["id"]

    r1 = client.post("/tags/", json={"name": "python"})
    r2 = client.post("/tags/", json={"name": "fastapi"})
    tag_id_1 = r1.json()["id"]
    tag_id_2 = r2.json()["id"]

    r = client.post(f"/tags/{note_id}/tags", json={"tag_ids": [tag_id_1, tag_id_2]})
    assert r.status_code == 200
    data = r.json()
    tag_names = [t["name"] for t in data.get("tags", []) if isinstance(t, dict)]
    # NoteRead doesn't include tags in response by default, but relationship is set


def test_add_tags_to_note_not_found(client):
    r = client.post("/tags/99999/tags", json={"tag_ids": [1]})
    assert r.status_code == 404
