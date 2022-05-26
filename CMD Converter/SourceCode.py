#Convert Old Bedrock 1.18 and lower /execute commands to New Bedrock 1.19+
#Made by L0VE MC aka Love#1000
#Published by Odin Network

def fix_t_format(command): #Formats ~'s
    command = command.replace("~ ~ ~", "~~~")
    command  = command.replace("~ ~~", "~~~")
    command  = command.replace("~~ ~", "~~~")
    return command

def translate(command): #Translates to 1.19 execute commands
    command = command.replace("execute @p","execute as @p")
    command = command.replace("execute @a","execute as @a")
    command = command.replace("execute @r","execute as @r")
    command = command.replace("execute @e","execute as @e")
    command = command.replace("execute @s","execute as @s")
    command = command.replace("~~~","at @s run")
    return command

def main(command): #Fixes the format then runs the translate function
    command = fix_t_format(command)
    command = translate(command)
    return(command)

with open('new_commands.txt', 'w') as file: #Opens the new command file
    with open('old_commands.txt', 'r') as f: #Opens the old command file
        exe_commands = 0 
        non_exe = 0    #Setting some vars for output and debugging
        line_count = 0
        error_lines = []
        for line in f: #Loops through the lines in the old command file
            line_count += 1
            if 'execute' in line: #Checks if the commands is a /execute command
                exe_commands += 1
                file.write(main(line)) #Writes the formatted line to the new commands file
                if "fill" in line: #Checks if the command is a /fill or /summon
                    error_lines += [f"{str(line_count)}"] #Lets the person know there could be an error
                if "summon" in line: #Checks if the command is a /fill or /summon
                    error_lines += [f"{str(line_count)}"] #Lets the person know there could be an error
            else:
                non_exe += 1
                file.write(line) #Writes the same command line because its not a /execute command

print("""
░██╗░░░░░░░██╗░█████╗░░█████╗░░██████╗██╗░░██╗██╗
░██║░░██╗░░██║██╔══██╗██╔══██╗██╔════╝██║░░██║██║
░╚██╗████╗██╔╝██║░░██║██║░░██║╚█████╗░███████║██║
░░████╔═████║░██║░░██║██║░░██║░╚═══██╗██╔══██║╚═╝
░░╚██╔╝░╚██╔╝░╚█████╔╝╚█████╔╝██████╔╝██║░░██║██╗
░░░╚═╝░░░╚═╝░░░╚════╝░░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝
""") #Whoosh!

close = input(f"Converted: {exe_commands}\nSkipped Lines: {non_exe}\nCheck lines {error_lines} for errors (/fills and /summons can bug out sometimes)") #Prints data to user