# %%
from pathlib import Path

def load_env():
    import tomllib
    with open("../env.toml", "rb") as f:
        env_data = tomllib.load(f)
    return env_data["game_links"]
env_data = load_env()

in1 = env_data["in1"]
in2 = env_data["in2"]
out = env_data["out"]

in_folders = [
    *Path(in1).glob("*"),
    *Path(in2).glob("*"),
]
print(f"all games: {in_folders.__len__()}")

out_names = {
    link.name[2:] 
    for link in Path(out).glob("./*.lnk")
}
print(f"existing links: {out_names.__len__()}")

new_links = [    
    {"name": new_link_name, "path": path}
    for folder in in_folders
    for path in folder.glob("./Launch *.lnk")
    if (new_link_name := path.name.removeprefix("Launch ")) not in out_names
]
print(f"new links: {new_links}")

# %%
import os
import shutil

def copy_links():
    os.makedirs(Path(out), exist_ok=True)
    return [
        shutil.copy2(link["path"], Path(out) / f"gg{link["name"]}")
        for link in new_links
    ]
copy_links()
