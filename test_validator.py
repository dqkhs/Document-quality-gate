from validator import validate_document


def test_valid_document():
    with open("samples/valid.md", "r", encoding="utf-8") as file:
        content = file.read()

    errors = validate_document(content)

    assert errors == []


def test_missing_acceptance_criteria():
    content = """
# Hotel Booking System

## Overview

This system allows users to book rooms.

## Requirements

### REQ-001

Users can book a room.
"""

    errors = validate_document(content)

    assert "Missing required section: ## Acceptance Criteria" in errors


def test_duplicate_requirement_id():
    content = """
# Hotel Booking System

## Overview

Hotel booking system.

## Requirements

### REQ-001

Users can book a room.

### REQ-001

Users can cancel a room.

## Acceptance Criteria

- Booking works.
"""

    errors = validate_document(content)

    assert "Duplicate Requirement ID found" in errors


def test_unclear_note():
    content = """
# Hotel Booking System

## Overview

Hotel booking system.

## Requirements

### REQ-001

TODO: Define booking requirement.

## Acceptance Criteria

- Booking works.
"""

    errors = validate_document(content)

    assert "Unclear note found: TODO" in errors


def test_no_requirement_id():
    content = """
# Hotel Booking System

## Overview

Hotel booking system.

## Requirements

Users can book a room.

## Acceptance Criteria

- Booking works.
"""

    errors = validate_document(content)

    assert "No valid Requirement ID found" in errors