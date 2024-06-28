from pathlib import Path
import mkdocs_gen_files

root = Path(__file__).parent.parent
src = root / "sendou"


for path in sorted(src.rglob("*.py")):
    module_path = path.relative_to(src).with_suffix("")
    if "__init__" in module_path.name:
        continue
    file_name_path = str(module_path).replace("/", ".")
    with mkdocs_gen_files.open(f"References/{str(module_path)}.md", "w") as fd:
        identifier = f"sendou.{file_name_path}"
        print("::: " + identifier, file=fd)
