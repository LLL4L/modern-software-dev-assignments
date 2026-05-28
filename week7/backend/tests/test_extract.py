from backend.app.services.extract import extract_action_items


def test_extract_todo():
    assert "TODO: write tests" in extract_action_items("TODO: write tests")


def test_extract_action():
    assert "ACTION: review PR" in extract_action_items("ACTION: review PR")


def test_extract_fixme():
    assert "FIXME: broken logic" in extract_action_items("FIXME: broken logic")


def test_extract_hack():
    assert "HACK: workaround" in extract_action_items("HACK: workaround")


def test_extract_bug():
    assert "BUG: crash on input" in extract_action_items("BUG: crash on input")


def test_extract_note_prefix():
    assert "NOTE: important" in extract_action_items("NOTE: important")


def test_extract_exclamation():
    assert "Ship it!" in extract_action_items("Ship it!")


def test_extract_checkbox_unchecked():
    result = extract_action_items("[ ] buy milk")
    assert any("buy milk" in r for r in result)


def test_extract_checkbox_checked():
    result = extract_action_items("[x] done already")
    assert any("done already" in r for r in result)


def test_extract_checkbox_dash_prefix():
    result = extract_action_items("- [ ] task item")
    assert any("task item" in r for r in result)


def test_extract_case_insensitive():
    assert extract_action_items("todo: lowercase")
    assert extract_action_items("TODO: uppercase")
    assert extract_action_items("Todo: mixed case")


def test_extract_no_match():
    assert extract_action_items("Just a regular line") == []


def test_extract_empty_input():
    assert extract_action_items("") == []


def test_extract_multiple_patterns():
    text = "TODO: first\nFIXME: second\nRegular line\nShip it!\n- [ ] checkbox"
    items = extract_action_items(text)
    assert len(items) == 4
    assert "TODO: first" in items
    assert "FIXME: second" in items
    assert "Ship it!" in items
    assert any("checkbox" in r for r in items)
