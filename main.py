from src.draw import open_new_window
from src.view_examples import verify
import os
import zipfile

from src.config.config import params


def get_missing():
    total = [{
        "letter": l,
        "numbers": [i for i in range(1, params['QUANTITY']+1) if not os.path.exists(os.path.join("OUTPUT", params['IMAGE_PATH'], l, f"{l}{i}.{params['IMAGE_FORMAT']}"))]
    } for l in params['LETTERS']]
    total = [t for t in total if len(t["numbers"]) > 0]
    missing = []
    for t in total:
        for n in t["numbers"]:
            tuple = (n, t["letter"])
            missing.append(tuple)
    return missing

missing = get_missing()

stop = False
while (True):
    while len(missing) > 0 and not stop:
        m = missing.pop(0)
        print(f"Draw the letter {m[1]}")
        stop = open_new_window(m[0], m[1])
    if stop:
        break
    verify()
    missing = get_missing()
    if len(missing) == 0:
        break

if len(missing) == 0:
    out_path = os.path.join("OUTPUT",params['IMAGE_PATH'])
    zip_path = f"{out_path}.zip"
    if os.path.exists(zip_path):
        os.remove(zip_path)
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, dirs, files in os.walk(out_path):
            for file in files:
                zipf.write(os.path.join(root, file))