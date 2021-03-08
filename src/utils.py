import pathlib
from PIL import Image # pip install pillow

def dir_to_thumbnails(source_dir, size=(150, 150)):
    path = pathlib.Path(source_dir).resolve()
    if not path.exists():
        return
    output_dir = path / "thumbs"
    output_dir.mkdir(exist_ok=True, parents=True)
    for fpath in path.glob("*"):
        if not fpath.is_file():
            continue
        fname = fpath.stem # fpath.name -> myfile.jpg
        ext = fpath.suffix # .jpg
        # if ext not in ['.jpg', '.git', '.png']:
        #     continue
        try:
            im = Image.open(fpath)
        except Exception as e:
            print(e)
            continue
        if ext != ".jpg":
            im = im.convert("RGB") # png -> RGBA -> jpg - RGB
            ext = '.jpg'
        im.thumbnail(size)
        output_path = output_dir / f"{fname}-thumb{ext}"
        im.save(output_path, 'JPEG')
    return str(output_dir)