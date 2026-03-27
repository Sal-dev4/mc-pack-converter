from __future__ import annotations

from pathlib import Path
import json
import shutil

from app.mappings import LEGACY_ITEM_FILE_RENAMES, LEGACY_BLOCK_FILE_RENAMES


def rewrite_pack_mcmeta(root: Path) -> None:
    mcmeta_path = root / "pack.mcmeta"

    data = {
        "pack": {
            "description": "Converted from 1.8.9 by the automatic converter",
            "min_format": [69, 0],
            "max_format": [75, 0]
        }
    }

    mcmeta_path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )


def copy_pack_icon_if_present(source_root: Path, dest_root: Path) -> None:
    src = source_root / "pack.png"
    dst = dest_root / "pack.png"
    if src.exists():
        shutil.copy2(src, dst)


def copy_assets(source_root: Path, dest_root: Path) -> None:
    src_assets = source_root / "assets"
    dst_assets = dest_root / "assets"

    if src_assets.exists():
        shutil.copytree(src_assets, dst_assets, dirs_exist_ok=True)


def rename_legacy_texture_folders(dest_root: Path) -> None:
    minecraft_textures = dest_root / "assets" / "minecraft" / "textures"

    old_blocks = minecraft_textures / "blocks"
    new_block = minecraft_textures / "block"

    old_items = minecraft_textures / "items"
    new_item = minecraft_textures / "item"

    if old_blocks.exists():
        if new_block.exists():
            for file_path in old_blocks.rglob("*"):
                if file_path.is_file():
                    relative = file_path.relative_to(old_blocks)
                    target = new_block / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(file_path, target)
            shutil.rmtree(old_blocks)
        else:
            old_blocks.rename(new_block)

    if old_items.exists():
        if new_item.exists():
            for file_path in old_items.rglob("*"):
                if file_path.is_file():
                    relative = file_path.relative_to(old_items)
                    target = new_item / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(file_path, target)
            shutil.rmtree(old_items)
        else:
            old_items.rename(new_item)


def rename_legacy_item_files(dest_root: Path) -> None:
    item_dir = dest_root / "assets" / "minecraft" / "textures" / "item"
    if not item_dir.exists():
        return

    for old_name, new_name in LEGACY_ITEM_FILE_RENAMES.items():
        old_path = item_dir / old_name
        new_path = item_dir / new_name

        if old_path.exists():
            if new_path.exists():
                old_path.unlink()
            else:
                old_path.rename(new_path)


def rename_legacy_block_files(dest_root: Path) -> None:
    block_dir = dest_root / "assets" / "minecraft" / "textures" / "block"
    if not block_dir.exists():
        return

    for old_name, new_name in LEGACY_BLOCK_FILE_RENAMES.items():
        old_path = block_dir / old_name
        new_path = block_dir / new_name

        if old_path.exists():
            if new_path.exists():
                old_path.unlink()
            else:
                old_path.rename(new_path)


def rename_legacy_special_item_textures(dest_root: Path) -> None:
    item_dir = dest_root / "assets" / "minecraft" / "textures" / "item"
    if not item_dir.exists():
        return

    special_renames = {
        "bow_standby.png": "bow.png",
        "fishing_rod_uncast.png": "fishing_rod.png",
        "fishing_rod_cast.png": "fishing_rod_cast.png",
    }

    for old_name, new_name in special_renames.items():
        old_path = item_dir / old_name
        new_path = item_dir / new_name

        if old_path.exists():
            if new_path.exists():
                old_path.unlink()
            else:
                old_path.rename(new_path)


def remove_incompatible_gui_files(dest_root: Path) -> None:
    container_dir = dest_root / "assets" / "minecraft" / "textures" / "gui" / "container"
    if not container_dir.exists():
        return

    old_inventory = container_dir / "inventory.png"
    if old_inventory.exists():
        old_inventory.unlink()

    old_creative_inventory = container_dir / "creative_inventory"
    if old_creative_inventory.exists() and old_creative_inventory.is_dir():
        shutil.rmtree(old_creative_inventory)