def _create_notes(client, count):
    notes = []
    for i in range(count):
        r = client.post("/notes/", json={"title": f"Note {i}", "content": f"Content {i}"})
        assert r.status_code == 201
        notes.append(r.json())
    return notes


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


def test_list_notes_pagination_skip(client):
    _create_notes(client, 5)
    r = client.get("/notes/", params={"skip": 2, "limit": 2, "sort": "-id"})
    assert r.status_code == 200
    assert len(r.json()) == 2


def test_list_notes_pagination_limit(client):
    _create_notes(client, 5)
    r = client.get("/notes/", params={"limit": 3, "sort": "-id"})
    assert r.status_code == 200
    assert len(r.json()) <= 3


def test_list_notes_pagination_skip_beyond(client):
    _create_notes(client, 2)
    r = client.get("/notes/", params={"skip": 100})
    assert r.status_code == 200
    assert r.json() == []


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


def test_list_notes_sort_descending(client):
    _create_notes(client, 3)
    r = client.get("/notes/", params={"sort": "-id"})
    assert r.status_code == 200
    ids = [n["id"] for n in r.json()]
    assert ids == sorted(ids, reverse=True)


def test_list_notes_sort_ascending(client):
    _create_notes(client, 3)
    r = client.get("/notes/", params={"sort": "id"})
    assert r.status_code == 200
    ids = [n["id"] for n in r.json()]
    assert ids == sorted(ids)


def test_list_notes_sort_by_title(client):
    _create_notes(client, 3)
    r = client.get("/notes/", params={"sort": "title"})
    assert r.status_code == 200
    titles = [n["title"] for n in r.json()]
    assert titles == sorted(titles)


def test_list_notes_invalid_sort_field(client):
    _create_notes(client, 2)
    r = client.get("/notes/", params={"sort": "nonexistent_field"})
    assert r.status_code == 200
    assert len(r.json()) >= 2


def test_list_notes_search_filter(client):
    _create_notes(client, 3)
    r = client.get("/notes/", params={"q": "Note 1"})
    assert r.status_code == 200
    for note in r.json():
        assert "Note 1" in note["title"] or "Note 1" in note["content"]


def test_list_notes_search_no_results(client):
    _create_notes(client, 2)
    r = client.get("/notes/", params={"q": "zzz_nonexistent"})
    assert r.status_code == 200
    assert r.json() == []


def test_extract_from_note_not_found(client):
    r = client.post("/notes/99999/extract")
    assert r.status_code == 404


def test_get_note(client):
    r = client.post("/notes/", json={"title": "Single", "content": "Fetch me"})
    assert r.status_code == 201
    note_id = r.json()["id"]

    r = client.get(f"/notes/{note_id}")
    assert r.status_code == 200
    assert r.json()["title"] == "Single"


def test_get_note_not_found(client):
    r = client.get("/notes/99999")
    assert r.status_code == 404


def test_delete_note(client):
    r = client.post("/notes/", json={"title": "Delete me", "content": "Bye"})
    assert r.status_code == 201
    note_id = r.json()["id"]

    r = client.delete(f"/notes/{note_id}")
    assert r.status_code == 204

    r = client.get(f"/notes/{note_id}")
    assert r.status_code == 404


def test_delete_note_not_found(client):
    r = client.delete("/notes/99999")
    assert r.status_code == 404


def test_patch_note_not_found(client):
    r = client.patch("/notes/99999", json={"title": "Nope"})
    assert r.status_code == 404


def test_create_note_validation_empty_title(client):
    r = client.post("/notes/", json={"title": "", "content": "valid"})
    assert r.status_code == 422


def test_create_note_validation_empty_content(client):
    r = client.post("/notes/", json={"title": "valid", "content": ""})
    assert r.status_code == 422


def test_create_note_validation_title_too_long(client):
    r = client.post("/notes/", json={"title": "x" * 201, "content": "valid"})
    assert r.status_code == 422


def test_create_note_validation_missing_fields(client):
    r = client.post("/notes/", json={})
    assert r.status_code == 422
