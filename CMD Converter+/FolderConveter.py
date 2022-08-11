#Convert Old Bedrock 1.18 and lower /execute commands to New Bedrock 1.19+
#Made by L0VE MC aka Love#1000
#Published by Odin Network

import os

# TODO - Curtidor
# add suport for detect [Not Done]
# add suport for execute pos other than triple tilde [Not Done]
# fix the problem with fill summon etc [Done]

###CONSTS###
DIRECTORY_PATH = 'CMD Converter+/old'


def fix_t_format(command: str) -> str:
    command = command.replace("~ ~ ~", "~~~")
    command = command.replace("~ ~~", "~~~")
    command = command.replace("~~ ~", "~~~")
    return command


def translate(command: str) -> str:
	command = fix_t_format(command)
	command = command.replace("execute @p", "execute as @p")
	command = command.replace("execute @a", "execute as @a")
	command = command.replace("execute @r", "execute as @r")
	command = command.replace("execute @e", "execute as @e")
	command = command.replace("execute @s", "execute as @s")
	command_data = command.split()
	for index, token in enumerate(command_data):
		if token == '~~~' and command_data[index-1] == 'execute':
			command = command.replace("~~~", "at @s run")
	return command


def show(total_converted: int, total_not: int, file: str, line_count: int) -> None:
    print(f"{'-'.rjust(20,'-')} \n{file} was converted.")
    print( f"Execute Commands: {total_converted}\nSkipped Lines:{total_not}\nTotal Lines: {line_count}\n" )


for file_name in os.listdir(DIRECTORY_PATH):
    if file_name.endswith('mcfunction'):
        with open(os.path.join('CMD Converter+/new', file_name),
                  'w') as out_file:
            with open(os.path.join('CMD Converter+/old', file_name),
                      'r') as reader:
                exe_commands = 0
                non_exe = 0
                for line_count, command in enumerate(reader):
                    if 'execute' in command:
                        exe_commands += 1
                        out_file.write(translate(command))
                    else:
                        non_exe += 1
                        out_file.write(command)
            show(exe_commands, non_exe, file_name, line_count)

close = input("----------------\nType anything to close...")
