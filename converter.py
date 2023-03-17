# Convert Old Bedrock 1.18 and lower /execute commands to New Bedrock 1.19
# Made by L0VE MC aka Love#1000
# Published by Odin Network

import os

# TODO - Curtidor
# add support for detect [Done]
# add support for execute pos other than triple tilde [Done]
# fix the problem with fill summon etc [Done]

## CONSTS ###
SOURCE_DIRECTORY_PATH = "./old"
OUT_DIRECTORY_PATH = "./new"


def convert_selector(command):
    return command.replace("execute @p", "execute as @p") \
        .replace("execute @a", "execute as @a") \
        .replace("execute @r", "execute as @r") \
        .replace("execute @e", "execute as @e") \
        .replace("execute @s", "execute as @s").split()


# formats the position (x, y, z) for consistent spacing
def formate_command(command: str) -> list[str]:
    command_data = convert_selector(command)

    index = 0
    while index < len(command_data):
        if '~' in command_data[index] and '~' in command_data[index + 1]:
            command_data[index] += command_data[index + 1]
            del command_data[index + 1]
        elif '~' in command_data[index] and '~' in command_data[index - 1]:
            command_data[index - 1] += command_data[index]
            del command_data[index]
        index += 1
    return command_data


# adds the run key word
def add_run(command_data: list[str], index: int, offset: int) -> None:
    index += 1
    while index < len(command_data):
        if command_data[index].lstrip('-').isdigit() or '~' in command_data[index]:
            index += 1
        else:
            break
    if not command_data[index] == 'detect': command_data[index + offset] = 'run ' + command_data[index + offset]


def convert(command: str) -> str:
    if not command.startswith('execute'): return command.rstrip('\n')
    command_data = formate_command(command)
    for index, token in enumerate(command_data):
        if token == 'execute' or token == 'run execute':
            if command_data[index + 3] == '~~~':
                command_data[index + 3] = command_data[index + 3].replace('~~~', 'at @s run')
            else:
                command_data[index + 3] = 'positioned ' + command_data[index + 3]
                add_run(command_data, index + 3, 0)
        elif token == 'detect':
            command_data[index] = 'if block'
            if command_data[index - 1] == 'at @s run': command_data[index - 1] = 'at @s'
            add_run(command_data, index, 2)
    return " ".join(command_data)


def convert_file(source_path: str, out_path: str) -> None:
    with open(source_path, "r") as source_file:
        with open(out_path, "w") as out_file:
            for command in source_file:
                converted_command = convert(command)
                if converted_command:
                    out_file.write(converted_command + "\n")


def main():
    for file_name in os.listdir(SOURCE_DIRECTORY_PATH):
        if not file_name.endswith("mcfunction"): continue
        source = os.path.join(SOURCE_DIRECTORY_PATH, file_name)
        out = os.path.join(OUT_DIRECTORY_PATH, file_name)
        convert_file(source, out)


if __name__ == "__main__":
    main()
