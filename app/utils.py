from __future__ import annotations

from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import shutil


def ensure_clean_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def unzip_pack(zip_path: Path, extract_to: Path) -> None:
    ensure_clean_dir(extract_to)
    with ZipFile(zip_path, "r") as zf:
        zf.extractall(extract_to)


def zip_folder(folder: Path, output_zip: Path) -> None:
    if output_zip.exists():
        output_zip.unlink()

    with ZipFile(output_zip, "w", compression=ZIP_DEFLATED) as zf:
        for file_path in folder.rglob("*"):
            if file_path.is_file():
                arcname = file_path.relative_to(folder)
                zf.write(file_path, arcname)