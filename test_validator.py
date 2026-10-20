from validator import validate_document


def test_valid_document():
    with open("samples/valid.md", "r", encoding="utf-8") as file:
        content = file.read()

    errors = validate_document(content)

    assert errors == []


def test_invalid_document():
    with open("samples/invalid.md", "r", encoding="utf-8") as file:
        content = file.read()

    errors = validate_document(content)

    assert "Missing required section: ## Acceptance Criteria" in errors
    assert "Duplicate Requirement ID found" in errors
    assert "Unclear note found: TODO" in errors