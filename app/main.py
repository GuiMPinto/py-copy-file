def copy_file(command: str) -> None:
    arquivo_original = command.split()[1]
    arquivo_novo = command.split()[2]
    if arquivo_original == arquivo_novo:
        return

    with open(arquivo_original, "r"), open(arquivo_novo, "w"):
        arquivo_novo.write(arquivo_original.read())
