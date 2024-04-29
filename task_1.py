import logging
import pathlib
from typing import List, Union
import shutil


def copy_dir_content(src_dir: Union[str, pathlib.Path], dest_dir: Union[str, pathlib.Path] = "dist") -> None:
    src_dir = pathlib.Path(src_dir)
    dest_dir = pathlib.Path(dest_dir)
    if not src_dir.exists():
        logging.error(f"Source directory {src_dir} does not exist. Exiting...")
        return
    if not dest_dir.exists():
        logging.info(f"Destination directory {dest_dir} does not exist. Creating...")
        try:
            dest_dir.mkdir()
        except PermissionError:
            logging.error(f"Permission denied to create directory {dest_dir}. Exiting...")
            return

    extensions: List[str] = []

    for item in src_dir.iterdir():
        if item.is_dir():
            copy_dir_content(item, dest_dir)
        if item.is_file():
            ext = item.suffix[1:]
            if ext and len(ext) <= 5:
                ext_dir = dest_dir / ext
                if ext not in extensions:
                    extensions.append(ext)
                    try:
                        if not ext_dir.exists():
                            ext_dir.mkdir()
                    except PermissionError:
                        logging.error(f"Permission denied to create directory {ext_dir}. Skipping...")
                        continue
            else:
                ext_dir = dest_dir / "other"
                if not ext_dir.exists():
                    try:
                        ext_dir.mkdir()
                    except PermissionError:
                        logging.error(f"Permission denied to create directory {ext_dir}. Skipping...")
                        continue
            try:
                logging.info(f"Copying file {item} to {ext_dir} directory. Extension: {ext}")
                shutil.copy2(item, ext_dir)
            except PermissionError:
                logging.error(f"Permission denied to copy file {item}. Skipping...")
                continue


if __name__ == "__main__":
    path = "/home/serhii/work"
    copy_dir_content(path)
