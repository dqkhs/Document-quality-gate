import re


REQUIRED_SECTIONS = [
    "## Overview",
    "## Requirements",
    "## Acceptance Criteria",
]


def validate_document(content: str) -> list[str]:
    errors = []

    # 1. Kiểm tra section bắt buộc
    for section in REQUIRED_SECTIONS:
        if section not in content:
            errors.append(f"Missing required section: {section}")

    # 2. Tìm Requirement ID
    requirement_ids = re.findall(r"\bREQ-\d+\b", content)

    if not requirement_ids:
        errors.append("No valid Requirement ID found")

    # 3. Kiểm tra Requirement ID bị trùng
    if len(requirement_ids) != len(set(requirement_ids)):
        errors.append("Duplicate Requirement ID found")

    # 4. Kiểm tra ghi chú chưa rõ
    unclear_notes = ["TODO", "TBD", "UNCLEAR"]

    for note in unclear_notes:
        if note in content.upper():
            errors.append(f"Unclear note found: {note}")

    return errors