
import os

def fix_t_format(command):
    command = command.replace("~ ~ ~", "~~~")
    command  = command.replace("~ ~~", "~~~")
    command  = command.replace("~~ ~", "~~~")
    return command

def translate(command):
    command = command.replace("execute @p","execute as @p")
    command = command.replace("execute @a","execute as @a")
    command = command.replace("execute @r","execute as @r")
    command = command.replace("execute @e","execute as @e")
    command = command.replace("execute @s","execute as @s")
    command = command.replace("~~~","at @s run")
    return command

def main(command):
    command = fix_t_format(command)
    command = translate(command)
    return(command)

def show(total_converted, total_not, err_lines, file, line_count):
        print(f"----------------\n{file} was converted.\nExecute Commands: {total_converted}\nSkipped Lines: {total_not}\nTotal Lines: {line_count}\n")
        if err_lines != []:
            print(f"Check lines {err_lines} for errors (/fills, /particles and /summons can bug out sometimes)\n")

path_of_the_directory= '.\old'

for filename in os.listdir(path_of_the_directory):
    f = os.path.join(path_of_the_directory,filename)
    if os.path.isfile(f):
        filename=f.replace(".\old\\","")
        f = f.replace(".\old\\","")
        if ".mcfunction" in f:
            with open(f'.\\new\\{f}', 'w') as file:
                with open(f'.\old\\{f}', 'r') as f:
                        exe_commands = 0 
                        non_exe = 0
                        line_count = 0
                        error_lines = []
                        for line in f:
                            line_count += 1
                            if 'execute' in line:
                                exe_commands += 1
                                file.write(main(line))
                                if "fill" in line:
                                    error_lines += [f"{str(line_count)}"]
                                if "summon" in line:
                                    error_lines += [f"{str(line_count)}"]
                                if "particle" in line:
                                    error_lines += [f"{str(line_count)}"]
                            else:
                                non_exe += 1
                                file.write(line)
                show(exe_commands,non_exe,error_lines,filename,line_count)
        else:
            print(f"\n{f} was skipped because it is not a .mcfunction\n")

close = input("----------------\nType anything to close...")