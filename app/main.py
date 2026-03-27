from __future__ import annotations

from pathlib import Path

from app.utils import unzip_pack, zip_folder, ensure_clean_dir
from app.converter import (
    rewrite_pack_mcmeta,
    copy_pack_icon_if_present,
    copy_assets,
    rename_legacy_texture_folders,
    rename_legacy_item_files,
    rename_legacy_block_files,
    rename_legacy_special_item_textures,
    remove_incompatible_gui_files,
)


BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"
WORK_DIR = BASE_DIR / ".work"


def main() -> None:
    ensure_clean_dir(WORK_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    zip_files = list(INPUT_DIR.glob("*.zip"))
    if not zip_files:
        raise FileNotFoundError("No .zip file found in input/")

    source_zip = zip_files[0]
    extracted = WORK_DIR / "extracted"
    converted = WORK_DIR / "converted"

    unzip_pack(source_zip, extracted)
    ensure_clean_dir(converted)

    copy_assets(extracted, converted)
    copy_pack_icon_if_present(extracted, converted)
    rename_legacy_texture_folders(converted)
    rename_legacy_item_files(converted)
    rename_legacy_block_files(converted)
    rename_legacy_special_item_textures(converted)
    remove_incompatible_gui_files(converted)
    rewrite_pack_mcmeta(converted)

    out_zip = OUTPUT_DIR / f"{source_zip.stem}_converted.zip"
    zip_folder(converted, out_zip)

    print(f"Done: {out_zip}")


if __name__ == "__main__":
    main()