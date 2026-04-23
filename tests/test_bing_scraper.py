# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from pathlib import Path

import bing_scraper


class FakeResponse:
    """Minimal urllib response stub for download tests."""

    def __init__(self, content_type):
        """Initialize the fake response with a content type."""
        self.headers = {"Content-Type": content_type}

    def read(self):
        """Return fake image bytes."""
        return b"image-bytes"

    def close(self):
        """Close the fake response."""
        return None


def test_python_search_argument_uses_bing(monkeypatch):
    """Direct Python use of `search` should not require `keywords` or fall back to Google."""
    scraper = bing_scraper.googleimagesdownload()
    urls = []

    monkeypatch.setattr(scraper, "download_page", lambda url: urls.append(url) or "")
    monkeypatch.setattr(scraper, "_get_all_items", lambda *args, **kwargs: ([], 0, []))

    paths, errors = scraper.download({"search": "honeybees on flowers", "limit": 1, "download": False})

    assert errors == 0
    assert list(paths) == ["honeybees on flowers"]
    assert urls == ["https://www.bing.com/images/search?q=honeybees%20on%20flowers"]


def test_url_argument_strips_shell_quotes(monkeypatch):
    """Quoted URLs copied from shell examples should be cleaned before browser or HTTP use."""
    scraper = bing_scraper.googleimagesdownload()
    urls = []

    monkeypatch.setattr(scraper, "download_page", lambda url: urls.append(url) or "")
    monkeypatch.setattr(scraper, "_get_all_items", lambda *args, **kwargs: ([], 0, []))

    scraper.download(
        {
            "url": "'https://www.bing.com/images/search?q=parcel'",
            "limit": 1,
            "download": False,
            "silent_mode": True,
        }
    )

    assert urls == ["https://www.bing.com/images/search?q=parcel"]


def test_search_preserves_filter_params(monkeypatch):
    """Bing search URLs should retain existing format/filter parameters."""
    scraper = bing_scraper.googleimagesdownload()
    urls = []

    monkeypatch.setattr(scraper, "download_page", lambda url: urls.append(url) or "")
    monkeypatch.setattr(scraper, "_get_all_items", lambda *args, **kwargs: ([], 0, []))

    scraper.download({"search": "cats", "limit": 1, "download": False, "format": "jpg"})

    assert urls == ["https://www.bing.com/images/search?q=cats&tbs=ift:jpg"]


def test_comma_search_keeps_per_keyword_directories(monkeypatch):
    """Direct Python `search` aliases should match `keywords` directory behavior for comma-separated terms."""
    scraper = bing_scraper.googleimagesdownload()
    directories = []

    monkeypatch.setattr(scraper, "create_directories", lambda main_directory, dir_name: directories.append(dir_name))
    monkeypatch.setattr(scraper, "download_page", lambda url: "")
    monkeypatch.setattr(scraper, "_get_all_items", lambda *args, **kwargs: ([], 0, []))

    scraper.download({"search": "cats,dogs", "limit": 1, "download": True})

    assert directories == ["cats", "dogs"]


def test_download_image_uses_content_type_for_extensionless_urls(monkeypatch, tmp_path):
    """Image URLs without filename extensions should use the HTTP Content-Type extension."""
    scraper = bing_scraper.googleimagesdownload()
    output_dir = tmp_path / "images"
    (output_dir / "sample").mkdir(parents=True)

    monkeypatch.setattr(bing_scraper, "urlopen", lambda *args, **kwargs: FakeResponse("image/jpeg"))

    status, _, image_name, absolute_path = scraper.download_image(
        "https://example.com/revision/latest",
        "",
        str(output_dir),
        "sample",
        1,
        False,
        1,
        None,
        False,
        False,
        True,
        None,
        "",
        True,
        None,
        None,
    )

    assert status == "success"
    assert image_name == "1.latest.jpg"
    assert Path(absolute_path).read_bytes() == b"image-bytes"


def test_download_image_quotes_unicode_urls(monkeypatch, tmp_path):
    """Non-ASCII image URLs should be percent-encoded for urllib while preserving Unicode filenames."""
    scraper = bing_scraper.googleimagesdownload()
    output_dir = tmp_path / "images"
    (output_dir / "unicode").mkdir(parents=True)
    requested_urls = []

    def fake_urlopen(request, *args, **kwargs):
        requested_urls.append(request.full_url)
        return FakeResponse("image/png")

    monkeypatch.setattr(bing_scraper, "urlopen", fake_urlopen)

    status, _, image_name, absolute_path = scraper.download_image(
        "https://example.com/изображение",
        "",
        str(output_dir),
        "unicode",
        1,
        False,
        1,
        None,
        False,
        False,
        True,
        None,
        "",
        True,
        None,
        None,
    )

    assert status == "success"
    assert requested_urls == ["https://example.com/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5"]
    assert image_name == "1.изображение.png"
    assert Path(absolute_path).exists()
