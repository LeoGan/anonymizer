import json
from pathlib import Path
import pdf_anonymizer_core.utils
from pdf_anonymizer_core.utils import save_results


def test_save_results_pdf(tmp_path: Path, monkeypatch):
    # Create temp directories
    temp_anonymized = tmp_path / "anonymized"
    temp_mappings = tmp_path / "mappings"

    # Monkeypatch the module level constants
    monkeypatch.setattr(pdf_anonymizer_core.utils, "DEFAULT_ANONYMIZED_DIR", str(temp_anonymized))
    monkeypatch.setattr(pdf_anonymizer_core.utils, "DEFAULT_MAPPINGS_DIR", str(temp_mappings))

    text = "Hello PERSON_1"
    mapping = {"PERSON_1": "John Doe"}
    file_path = "document.pdf"

    anonymized_output_file, mapping_file = save_results(text, mapping, file_path)

    # Assert return values
    assert Path(anonymized_output_file).name == "document.anonymized.md"
    assert Path(mapping_file).name == "document.mapping.json"

    # Assert directories were created and files exist
    assert temp_anonymized.exists()
    assert temp_mappings.exists()

    # Assert file contents
    assert Path(anonymized_output_file).read_text(encoding="utf-8") == text
    with open(mapping_file, "r", encoding="utf-8") as f:
        loaded_mapping = json.load(f)
    assert loaded_mapping == mapping


def test_save_results_txt(tmp_path: Path, monkeypatch):
    # Create temp directories
    temp_anonymized = tmp_path / "anonymized"
    temp_mappings = tmp_path / "mappings"

    # Monkeypatch the module level constants
    monkeypatch.setattr(pdf_anonymizer_core.utils, "DEFAULT_ANONYMIZED_DIR", str(temp_anonymized))
    monkeypatch.setattr(pdf_anonymizer_core.utils, "DEFAULT_MAPPINGS_DIR", str(temp_mappings))

    text = "Hello PERSON_1"
    mapping = {"PERSON_1": "John Doe"}
    file_path = "doc.txt"

    anonymized_output_file, mapping_file = save_results(text, mapping, file_path)

    # Assert return values
    assert Path(anonymized_output_file).name == "doc.anonymized.txt"
    assert Path(mapping_file).name == "doc.mapping.json"

    # Assert file contents
    assert Path(anonymized_output_file).read_text(encoding="utf-8") == text
