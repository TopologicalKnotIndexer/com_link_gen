from functools import cache
from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
import tomllib


@cache
def get_version_in_toml() -> str:
    path = Path(__file__).resolve().parent.parent / "pyproject.toml"
    if not path.is_file():
        return "unknown"
    with path.open("rb") as handle:
        return str(tomllib.load(handle).get("project", {}).get("version", "unknown"))


@cache
def get_version(pkg_name_now: str = "com-link-gen-10") -> str:
    try:
        return version(pkg_name_now)
    except PackageNotFoundError:
        return get_version_in_toml()
