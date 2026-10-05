from hypothesis import given, strategies as st
from validator import validate_document


# Property 1: Hàm validate_document phải luôn trả về một list (dù input là bất kỳ chuỗi kỳ quặc nào)
@given(st.text())
def test_validator_never_crashes(content):
    result = validate_document(content)
    assert isinstance(result, list)


# Property 2: Nếu tài liệu chứa từ TODO (không phân biệt hoa thường), hàm PHẢI phát hiện ra lỗi TODO
@given(st.text())
def test_detects_todo_if_present(content):
    # Thêm từ TODO vào nội dung ngẫu nhiên do Hypothesis sinh ra
    content_with_todo = content + "\nTODO: fix this later"
    errors = validate_document(content_with_todo)

    assert "Unclear note found: TODO" in errors