def test_create_list_and_patch_notes(client):
    payload = {"title": "Test", "content": "Hello world"}
    r = client.post("/notes/", json=payload)
    assert r.status_code == 201, r.text
    data = r.json()
    assert data["title"] == "Test"
    assert "created_at" in data and "updated_at" in data

    r = client.get("/notes/")
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

    r = client.get("/notes/", params={"q": "Hello", "limit": 10, "sort": "-created_at"})
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1

    note_id = data["id"]
    r = client.patch(f"/notes/{note_id}", json={"title": "Updated"})
    assert r.status_code == 200
    patched = r.json()
    assert patched["title"] == "Updated"


def test_extract_from_note(client):
    r = client.post(
        "/notes/",
        json={"title": "Tasks", "content": "TODO: write tests\nACTION: review PR\nJust a note"},
    )
    assert r.status_code == 201
    note_id = r.json()["id"]

    r = client.post(f"/notes/{note_id}/extract")
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 2
    assert "TODO: write tests" in items
    assert "ACTION: review PR" in items


def test_extract_from_note_no_matches(client):
    r = client.post("/notes/", json={"title": "Plain", "content": "Nothing to see here"})
    assert r.status_code == 201
    note_id = r.json()["id"]

    r = client.post(f"/notes/{note_id}/extract")
    assert r.status_code == 200
    assert r.json() == []


def test_extract_from_note_not_found(client):
    r = client.post("/notes/99999/extract")
    assert r.status_code == 404


