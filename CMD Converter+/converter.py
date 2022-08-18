# Convert Old Bedrock 1.18 and lower /execute commands to New Bedrock 1.19
# Made by L0VE MC aka Love#1000
# Published by Odin Network

import os
from typing import Iterator

# TODO - Curtidor
# add support for detect [Half Done]
# add support for execute pos other than triple tilde [Not Done]
# fix the problem with fill summon etc [Done]

### CONSTS ###
SOURCE_DIRECTORY_PATH = os.path.join("../CMD Converter+", 'old')
OUT_DIRECTORY_PATH = os.path.join("../CMD Converter+", 'new')


def convert_selector(command: str) -> list[str]:
	command = command.replace("execute @p", "execute as @p")
	command = command.replace("execute @a", "execute as @a")
	command = command.replace("execute @r", "execute as @r")
	command = command.replace("execute @e", "execute as @e")
	command = command.replace("execute @s", "execute as @s")
	return command.split()


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

# adds the run key word when
def add_run(command_data: list[str], index: int, offset: int) -> None:
	index += 1
	while index < len(command_data):
		if command_data[index].lstrip('-').isdigit() or '~' in command_data[index]:
			index += 1
		else: break
	if not command_data[index] == 'detect': command_data[index + offset] = 'run ' + command_data[index + offset]


def convert(command: str) -> Iterator[str]:
	if not command.startswith('execute'): yield command.rstrip('\n')
	command_data = formate_command(command)
	for index, token in enumerate(command_data):
		if token == 'execute' or token == 'run execute':
			if command_data[index+3] == '~~~':
				command_data[index+3] = command_data[index+3].replace('~~~', 'at @s run')
			else:
				command_data[index+3] = 'positioned ' + command_data[index+3]
				add_run(command_data, index+3, 0)
		elif token == 'detect':
			command_data[index] = 'if block'
			if command_data[index - 1] == 'at @s run': command_data[index-1] = 'at @s'
			add_run(command_data, index, 2)
	print(command_data)
	yield " ".join(command_data)


def main():
	for file_name in os.listdir(SOURCE_DIRECTORY_PATH):
		if not file_name.endswith("mcfunction"): continue
		with open(os.path.join(SOURCE_DIRECTORY_PATH, file_name), "r") as source_file:
			with open(os.path.join(OUT_DIRECTORY_PATH, file_name), "w") as out_file:
				for command in source_file:
					out_file.write(next(convert(command)))
					out_file.write('\n')


if __name__ == "__main__":
	main()
