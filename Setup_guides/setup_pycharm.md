# How to setup pycharm for the SoundZone Server project

## Open project

Press - "Open"

![](photos/welcome.png)

Select and open - "soundzone_server" project

![](photos/server_project.png)

## Set project root

1. Press - "File"
2. Press - "Settings"

![](photos/open_settings.png)

3. Press - "Project: soundzone_server"
4. Press - "Project: Stucture"
5. Press - "Add Content Root"

![](photos/add_content_root.png)

6. Select and add - "shared_modules"

![](photos/add_shared_modules.png)

7. Select - "shared_modules"
8. Select - ".idea"
9. Press - "Exclude"
10. Press - "Apply"
11. Press - Ok

![](photos/exclude_idea.png)

## Setup Intepreter

You can either use a local interpretor or a remote interpreter (A Pi that executes the code).

### Local

1. Press - "File"
2. Press - "Settings"
3. Press - "Project: "
4. Press - "Project Interpreter"
5. Select - "Python 3.X"
6. Press - "Apply"
7. Press - "Ok"

![](photos/local_interpreter.png)

### Remote

1. Press - "File"
2. Press - "Settings"
3. Press - "Project: "
4. Press - "Project Interpreter"
5. Press on the gear, that is on the right of the Python interpreter
6. Press - "add"
7. Press - "SSH Interpreter"
8. Press - "New server configuration"
    1. Host: either ip or hostname of Pi
    2. Username: Your Username on the pi
    3. Port: 22
9. Press - "Next"


![](photos/ssh_interpreter.png)

10. Add password or add keypair (I would allways use key pair)
11. Select interpreter by clicking on the folder
    1. /home/{UserName}/.virtualenvs/SZP/bin/python3
12. Set "Sync folders"
    1. Local Path should be fine
    2. Set remote path to "/home/{UserName}/szp"
13. Press - "okay"
14. Press - "Finnish"
15. Press - "Apply"
16. Press - "Ok"

![](photos/sync_folders.png)

## Setup Deployment

1. Press - "File"
2. Press - "Settings"
3. Press - "Build, Execution, Deployment"
4. Press - "Deployment"
5. Select the host as default
6. Press - "Mappings"
    1. Add local path: "\Wireless_sound_zones\Server\soundzone_server" to remote: /home/ncpd/szp, and Web path: "/"
    2. Add local path: "\Wireless_sound_zones\shared_modules" to  remote: /home/ncpd/szp/modules, and Web path: "/"
7. Press - "Apply"
8. Press - "Excluded Paths"
    1. Add local path - "/Wireless_sound_zones/Server/soundzone_server/.idea"
    2. Add local path - "/Wireless_sound_zones/Server/soundzone_server/venv"
9. Press - "Apply"

![](photos/deployment_mappings.png)