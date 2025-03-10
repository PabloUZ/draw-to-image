from draw import open_new_window
import os
import zipfile

def get_missing():
    total = [{
        "letter": l,
        "numbers": [i for i in range(1, 21) if not os.path.exists(f"vowels/{l}/{l}{i}.png")]
    } for l in "AEIOUaeiou"]
    total = [t for t in total if len(t["numbers"]) > 0]
    missing = []
    for t in total:
        for n in t["numbers"]:
            tuple = (n, t["letter"])
            missing.append(tuple)
    return missing

missing = get_missing()

stop = False
while len(missing) > 0 and not stop:
    m = missing.pop(0)
    stop = open_new_window(m[0], m[1])

if len(missing) == 0:
    with zipfile.ZipFile('vowels.zip', 'w') as zipf:
        for root, dirs, files in os.walk('vowels'):
            for file in files:
                zipf.write(os.path.join(root, file))