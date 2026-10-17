import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pdfplumber.utils.exceptions import PdfminerException

from src.document_loader.document_loader import load_pdf, load_pdfs


class DocumentLoaderTests(unittest.TestCase):
    def test_load_pdf_preserves_page_numbers_and_string_source(self):
        with patch("src.document_loader.document_loader.pdfplumber.open") as open_pdf:
            open_pdf.return_value.__enter__.return_value.pages = [
                Mock(extract_text=Mock(return_value="第一页")),
                Mock(extract_text=Mock(return_value=None)),
                Mock(extract_text=Mock(return_value="第三页")),
            ]
            documents = load_pdf(Path("course.pdf"))

        self.assertEqual([doc.text for doc in documents], ["第一页", "第三页"])
        self.assertEqual(
            [doc.metadata for doc in documents],
            [{"source": "course.pdf", "page": 1}, {"source": "course.pdf", "page": 3}],
        )

    def test_nested_pdfs_uppercase_extension_and_pdf_named_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            nested = root / "test.pdf"
            nested.mkdir()
            (nested / "chapter.PDF").touch()
            (root / "intro.pdf").touch()
            (root / "notes.txt").touch()
            with patch("src.document_loader.document_loader.load_pdf", return_value=[]) as load:
                self.assertEqual(load_pdfs(root), [])

            self.assertEqual(
                [Path(call.args[0]).relative_to(root).as_posix() for call in load.call_args_list],
                ["intro.pdf", "test.pdf/chapter.PDF"],
            )

    def test_empty_directory_returns_empty_list(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(load_pdfs(tmp), [])

    def test_file_is_rejected_as_pdf_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "not-a-directory.pdf"
            path.touch()
            with self.assertRaises(NotADirectoryError):
                load_pdfs(path)

    def test_missing_pdf_raises_original_error(self):
        with (
            tempfile.TemporaryDirectory() as tmp,
            self.assertRaises(FileNotFoundError),
        ):
            load_pdf(Path(tmp) / "missing.pdf")

    def test_corrupt_pdf_does_not_turn_into_none_or_empty_success(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "broken.pdf").write_text("not a PDF", encoding="utf-8")
            with self.assertRaises(PdfminerException):
                load_pdfs(root)


if __name__ == "__main__":
    unittest.main()
