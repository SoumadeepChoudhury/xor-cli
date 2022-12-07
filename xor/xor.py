from getpass import getpass
import os
import subprocess
import sys
import platform
import COLORS
import datetime


def help():
    commands = [["search FORMULA|CASK", "info", "install FORMULA|CASK", "update",
                 "upgrade FORMULA|CASK", "uninstall FORMULA|CASK", "list"], ["config", "doctor"], ["man"]]
    print("Example Usages:")
    for i in commands[0]:
        print("\t", i)
    print("\nTroubleshooting:")
    for i in commands[1]:
        print("\t", i)
    print("\nFurther help:")
    for i in commands[2]:
        print("\t", i)


def info():
    pass


def search():
    pass


def install():
    pass


def update():
    pass


def upgrade():
    pass


def doctor():
    pass


def uninstall():
    pass


def list():
    pass


def main():
    process = {"Darwin": "clear", "Windows": "cls",
               "help": help, "doctor": doctor, "install": install, "uninstall": uninstall, "list": list, "search": search, "info": info, "update": update, "upgrade": upgrade}
    s_prs = subprocess.Popen(process[platform.system()])
    s_prs.wait()
    print(COLORS.RED)
    print("""
XXXXXXX       XXXXXXX     OOOOOOOOO     RRRRRRRRRRRRRRRRR   
X:::::X       X:::::X   OO:::::::::OO   R::::::::::::::::R  
X:::::X       X:::::X OO:::::::::::::OO R::::::RRRRRR:::::R 
X::::::X     X::::::XO:::::::OOO:::::::ORR:::::R     R:::::R
XXX:::::X   X:::::XXXO::::::O   O::::::O  R::::R     R:::::R
   X:::::X X:::::X   O:::::O     O:::::O  R::::R     R:::::R
    X:::::X:::::X    O:::::O     O:::::O  R::::RRRRRR:::::R 
     X:::::::::X     O:::::O     O:::::O  R:::::::::::::RR  
     X:::::::::X     O:::::O     O:::::O  R::::RRRRRR:::::R 
    X:::::X:::::X    O:::::O     O:::::O  R::::R     R:::::R
   X:::::X X:::::X   O:::::O     O:::::O  R::::R     R:::::R
XXX:::::X   X:::::XXXO::::::O   O::::::O  R::::R     R:::::R
X::::::X     X::::::XO:::::::OOO:::::::ORR:::::R     R:::::R
X:::::X       X:::::X OO:::::::::::::OO R::::::R     R:::::R
X:::::X       X:::::X   OO:::::::::OO   R::::::R     R:::::R
XXXXXXX       XXXXXXX     OOOOOOOOO     RRRRRRRR     RRRRRRR
""")
    print(COLORS.RESET)
    try:
        import pickle
        cur_dir = str(os.path.realpath(os.path.dirname(__file__)))
        #userName = input(f"{COLORS.BLUE}[?]{COLORS.RESET} Enter user name: ")
        #password = getpass(prompt=f"{COLORS.BLUE}[?]{COLORS.RESET} Password: ")
        #detail = {'username': userName, 'password': password}
        if os.path.isfile(cur_dir+'/.xorcnf'):
            with open(f'{cur_dir}/.xorcnf', 'rb') as file:
                try:
                    det = pickle.load(file)
                except:
                    det = {}
                file.close()
            # Date

            def d_time(n1, n2):
                def datediff(d1, d2):
                    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
                    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
                    delta = d2 - d1
                    if int(delta.days) > 0:
                        return True
                    else:
                        return False
                diff = str(datetime.timedelta(hours=int(n2.split(":")[0]), minutes=int(n2.split(":")[1]), seconds=int(n2.split(":")[2].split(".")[0]) + int(n2.split(".")[1].split()[
                           0])/1000000) - datetime.timedelta(hours=int(n1.split(":")[0]), minutes=int(n1.split(":")[1]), seconds=int(n1.split(":")[2].split(".")[0]) + int(n1.split(".")[1].split()[0])/1000000))

                if diff[0] == '-':
                    return False
                diff = diff.split(":")
                diff = int(diff[0])*3_600_000_000+int(diff[1])*60_000_000 + \
                    int(diff[2].split(".")[0])*1_000_000 + \
                    int(diff[2].split(".")[1])

                if datediff(n1.split()[1], n2.split()[1]):
                    diff += 86_400_000_000
                if diff > 86_400_000_000:
                    return True
                else:
                    return False

            dateTimeNow = ' '.join(str(datetime.datetime.now()).split()[::-1])
            if not d_time(det["Last Logged In"], dateTimeNow):
                if [*det.keys()] == ["username", "password", "Last Logged In"]:
                    if len(sys.argv) == 1:
                        process["help"]()
                    if sys.argv[1] not in list(process.keys()):
                        print(
                            f"{COLORS.RED}Error:{COLORS.RESET} Unknown Command: {sys.argv[1]}")
                    else:
                        process[sys.argv[1]]()
                else:
                    choice = input(
                        "User not found...Do you wanna create new account ? [y/n]: ").lower()
                    if choice in ('yes', 'y'):
                        try:
                            subprocess.call("rm .xorcnf; xor", shell=True)
                        except Exception as e:
                            print(e)
            else:
                userName = input(
                    f"{COLORS.BLUE}[?]{COLORS.RESET} Enter user name: ")
                password = getpass(
                    prompt=f"{COLORS.BLUE}[?]{COLORS.RESET} Password: ")
                dateTimeNow = ' '.join(
                    str(datetime.datetime.now()).split()[::-1])
                detail = {'username': userName, 'password': password,
                          'Last Logged In': dateTimeNow}
                with open(f'{cur_dir}/.xorcnf', 'wb') as file:
                    pickle.dump(detail, file)
                    file.close()
        else:
            userName = input(
                f"{COLORS.BLUE}[?]{COLORS.RESET} Enter user name: ")
            password = getpass(
                prompt=f"{COLORS.BLUE}[?]{COLORS.RESET} Password: ")
            dateTimeNow = ' '.join(str(datetime.datetime.now()).split()[::-1])
            detail = {'username': userName, 'password': password,
                      'Last Logged In': dateTimeNow}
            with open(f'{cur_dir}/.xorcnf', 'wb') as file:
                pickle.dump(detail, file)
                file.close()
            print("Created the XOR account...")
        if len(sys.argv) == 1:
            process["help"]()
        if sys.argv[1] not in list(process.keys()):
            print(
                f"{COLORS.RED}Error:{COLORS.RESET} Unknown Command: {sys.argv[1]}")
        else:
            process[sys.argv[1]]()
    except:
        pass


if __name__ == "__main__":
    main()
