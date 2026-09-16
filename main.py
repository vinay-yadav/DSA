import os


def createNewFile(filename, funcName):
    funcName = funcName.replace("def ", "").replace("List", "list")
    if not funcName.rstrip().endswith(":"):
        funcName = funcName.rstrip() + ":"

    methodName = funcName.split("(")[0].strip()

    templatePath = os.path.join(os.path.dirname(__file__), "template.txt")
    with open(templatePath, "r", encoding="utf-8") as templateFile:
        template = templateFile.read()

    fileContent = template.replace("{funcName}", funcName).replace(
        "{methodName}", methodName
    )

    filename = filename if "\\" in filename else f"LeetCodeDaily/{filename}"
    filepath = f"{filename}.py"

    os.makedirs(os.path.dirname(filepath) or ".", exist_ok=True)

    if os.path.exists(filepath):
        overwrite = input(f"{filepath} already exists. Overwrite? (y/n): ")
        if overwrite.lower() != "y":
            print("Aborted.")
            return

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(fileContent)

    print(f"Created {filepath}")


if __name__ == "__main__":
    filename = input("Filename: ")
    funcname = input("Funcname: ")
    createNewFile(filename, funcname)
