import sys
from validator import validate_document


def main():
    if len(sys.argv) < 2:
        print("Usage: python cli.py <path_to_markdown_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ Error: File '{file_path}' not found.")
        sys.exit(1)

    errors = validate_document(content)

    if not errors:
        print(f"✅ QUALITY GATE PASSED: '{file_path}' satisfies all requirements!")
        sys.exit(0)
    else:
        print(f"❌ QUALITY GATE FAILED: '{file_path}' has errors:")
        for err in errors:
            print(f"   - {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()