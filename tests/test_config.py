import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "backend"))

from app.core.config import Settings


def test_cors_origins_from_string():
    s = Settings(BACKEND_CORS_ORIGINS="http://example.com, https://example.org")
    assert [str(u) for u in s.BACKEND_CORS_ORIGINS] == [
        "http://example.com/",
        "https://example.org/",
    ]


def test_cors_origins_from_list():
    origins = ["http://foo.com", "https://bar.org"]
    s = Settings(BACKEND_CORS_ORIGINS=origins)
    assert [str(u) for u in s.BACKEND_CORS_ORIGINS] == [
        "http://foo.com/",
        "https://bar.org/",
    ]
