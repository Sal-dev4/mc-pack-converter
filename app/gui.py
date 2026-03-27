from __future__ import annotations

import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import os
import sys

from app.utils import unzip_pack, zip_folder, ensure_clean_dir
from app.converter import (
    rewrite_pack_mcmeta,
    copy_pack_icon_if_present,
    copy_assets,
    rename_legacy_texture_folders,
    rename_legacy_item_files,
    rename_legacy_special_item_textures,
    remove_incompatible_gui_files,
)


if getattr(sys, "frozen", False):
    BASE_DIR = Path(sys.executable).resolve().parent.parent
else:
    BASE_DIR = Path(__file__).resolve().parent.parent

OUTPUT_DIR = BASE_DIR / "output"
WORK_DIR = BASE_DIR / ".work"


def convert_pack(source_zip: Path) -> Path:
    ensure_clean_dir(WORK_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    extracted = WORK_DIR / "extracted"
    converted = WORK_DIR / "converted"

    unzip_pack(source_zip, extracted)
    ensure_clean_dir(converted)

    copy_assets(extracted, converted)
    copy_pack_icon_if_present(extracted, converted)
    rename_legacy_texture_folders(converted)
    rename_legacy_item_files(converted)
    rename_legacy_special_item_textures(converted)
    remove_incompatible_gui_files(converted)
    rewrite_pack_mcmeta(converted)

    out_zip = OUTPUT_DIR / f"{source_zip.stem}_converted.zip"
    zip_folder(converted, out_zip)
    return out_zip


class PackConverterApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Minecraft Pack Converter")
        self.root.geometry("520x260")
        self.root.resizable(False, False)

        self.selected_file: Path | None = None

        self.title_label = tk.Label(
            root,
            text="1.8.9 Resource Pack Converter",
            font=("Segoe UI", 14, "bold")
        )
        self.title_label.pack(pady=(20, 10))

        self.path_label = tk.Label(
            root,
            text="No zip selected",
            wraplength=470,
            justify="center"
        )
        self.path_label.pack(pady=10)

        self.select_button = tk.Button(
            root,
            text="Choose Pack Zip",
            width=22,
            command=self.choose_file
        )
        self.select_button.pack(pady=5)

        self.convert_button = tk.Button(
            root,
            text="Convert",
            width=22,
            command=self.run_conversion
        )
        self.convert_button.pack(pady=5)

        self.output_button = tk.Button(
            root,
            text="Open Output Folder",
            width=22,
            command=self.open_output_folder
        )
        self.output_button.pack(pady=5)

    def choose_file(self) -> None:
        file_path = filedialog.askopenfilename(
            title="Select a resource pack zip",
            filetypes=[("ZIP files", "*.zip")]
        )

        if not file_path:
            return

        self.selected_file = Path(file_path)
        self.path_label.config(text=str(self.selected_file))

    def run_conversion(self) -> None:
        if self.selected_file is None:
            messagebox.showerror("Error", "Please choose a pack zip first.")
            return

        try:
            output_zip = convert_pack(self.selected_file)
            messagebox.showinfo(
                "Done",
                f"Converted pack created:\n{output_zip}"
            )
        except Exception as exc:
            messagebox.showerror("Conversion failed", str(exc))

    def open_output_folder(self) -> None:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        os.startfile(OUTPUT_DIR)

def main() -> None:
    root = tk.Tk()
    app = PackConverterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()