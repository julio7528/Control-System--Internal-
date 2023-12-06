import os
import subprocess
try:
    import requests
    from colorama import Fore, Style, init as init_colorama
except ModuleNotFoundError:
    subprocess.run("python.exe -m pip install --upgrade pip", shell=True)
    subprocess.run("pip install requests", shell=True)
    subprocess.run("pip install colorama", shell=True)
    print(f"Please Close Applications and Run the program again.")
    # Stop the program
    exit()

class VirtualEnvironment:
    """
    📌 Name: VirtualEnvironment
    🚀 Functionality: Class to manage virtual environments.

    📥 Input Values:
        - projectPath (str): Path to the project directory.
        - virtualEnvironment (str): Name of the virtual environment.

    📤 Output Values:
        None

    📤 Returns:
        None

    🏭 Description of Process:
        - createVirtualEnvironment:
            [Steps:]
            1. Change the current directory to the projectPath.
            2. Run the command "python -m venv [virtualEnvironment]" using subprocess.
            3. Print a message indicating the command to use for the virtual environment.
            4. Exit the program.

        - deleteVirtualEnvironment:
            [Steps:]
            1. Construct the venv_path using projectPath and virtualEnvironment.
            2. If venv_path exists, run the command "cmd /c rmdir /s /q [venv_path]" using subprocess.
            3. If venv_path does not exist, print an error message.

        - listVirtualEnvironment:
            [Steps:]
            1. Change the current directory to the projectPath.
            2. Get a list of directories in the current path that are directories.
            3. Print the list of directories.

        - activateVirtualEnvironment:
            [Steps:]
            1. Construct the activateScript path using projectPath and virtualEnvironment.
            2. Print a command to activate the virtual environment.
            3. Prompt the user to press any key to continue.

        - creatingRequirements:
            [Steps:]
            1. Change the current directory to the projectPath.
            2. If "requirements.txt" exists, remove it.
            3. Run the command "pip freeze > requirements.txt" using subprocess.
            4. Print a message indicating the command to use for the virtual environment.

        - creatingGitignore:
            [Steps:]
            1. Fetch the Python.gitignore file from the GitHub repository.
            2. Save the content in a local file named ".gitignore".
            3. Print a message indicating the command to use for the virtual environment.
        
        - creatingDevelopmentStructure:
            [Steps:]
            1. Prompt the user to enter the project name.
            2. Create the project structure.
            3. Print a message indicating the command to use for the virtual environment.

    🚨 Exception Description:
        - In deleteVirtualEnvironment:
            - If venv_path does not exist, print an error message.

    🚨 Exception Return:
        None
    """

    def __init__(self, projectPath, virtualEnvironment):
        self.projectPath = projectPath
        self.virtualEnvironment = virtualEnvironment

    def createVirtualEnvironment(self):
        os.chdir(self.projectPath)
        if not os.path.exists(self.virtualEnvironment):
            subprocess.run(["python", "-m", "venv", self.virtualEnvironment])
            print(f"{Fore.GREEN}Created: {self.virtualEnvironment}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}Restart the applications to keep update the environment.{Style.RESET_ALL}")
            exit()
        else:
            print(f"{Fore.RED}Error: {self.virtualEnvironment} already exists.{Style.RESET_ALL}")

    def deleteVirtualEnvironment(self):
        venv_path = os.path.join(self.projectPath, self.virtualEnvironment)
        if os.path.exists(venv_path):
            subprocess.run(["cmd", "/c", "rmdir", "/s", "/q", venv_path], shell=True)
        else:
            print(f"Error: {venv_path} does not exist.")

    def listVirtualEnvironment(self):
        os.chdir(self.projectPath)
        directories = [name for name in os.listdir() if os.path.isdir(name)]
        print(directories)
        
    def activateVirtualEnvironment(self):
        activateScript = os.path.join(self.projectPath, self.virtualEnvironment, "Scripts", "activate")
        print(f"{Fore.CYAN}To activate the Virtual environment - use this command:{Style.RESET_ALL}")
        subprocess.run("pip install requests", shell=True)
        subprocess.run("pip install colorama", shell=True)
        print(f'***COPY***')
        print(f'{Fore.RED}cmd /k "call "{activateScript}"{Style.RESET_ALL}')
        print(f'***COPY***')
        input("Press any key to continue...")
    
    def creatingRequirements(self):
        os.chdir(self.projectPath)
        if os.path.exists("requirements.txt"):
            os.remove("requirements.txt")
        subprocess.run("pip freeze > requirements.txt", shell=True)
        print(f"{Fore.RED}Use this command only if the virtual environment is enabled.{Style.RESET_ALL}")
    
    def creatingGitignore(self):
        url = "https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore"
        response = requests.get(url)
        with open(".gitignore", "w") as f:
            f.write(response.text)
        print(f"{Fore.RED}Use this command only if the virtual environment is enabled.{Style.RESET_ALL}")
        
    def creatingDevelopmentStructure(self):
        vProjectName = input(f"{Fore.GREEN}{Style.BRIGHT}Project Name: {Style.RESET_ALL}")
        vStructure = [
            vProjectName,
            vProjectName + "/__init__.py",
            vProjectName + "/main_module.py",
            vProjectName + "/submodules",
            vProjectName + "/submodules/__init__.py",
            vProjectName + "/submodules/module1.py",
            vProjectName + "/submodules/module2.py",
            "tests",
            "tests/__init__.py",
            "tests/test_main_module.py",
            "tests/test_submodules",
            "tests/test_submodules/__init__.py",
            "tests/test_submodules/test_module1.py",
            "tests/test_submodules/test_module2.py",
            "docs",
            "data",
            "data/raw",
            "data/processed",
            "logs",
            "notebooks",
            "scripts",
            "setup.py",
            "README.md",
        ]
        for item in vStructure:
            if not os.path.exists(item):
                if "." in item:
                    with open(item, "w") as f:
                        pass
                else:
                    os.mkdir(item)
                    print(f"{Fore.GREEN}{Style.BRIGHT}Created: {Style.RESET_ALL}{Fore.GREEN}{item}{Style.RESET_ALL}")
            else:
                print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}Already Exists: {Style.RESET_ALL}{Fore.YELLOW}{item}{Style.RESET_ALL}")
        pass
        

if __name__ == "__main__":
    init_colorama()
    os.system("cls")
    projectPath = os.getcwd()
    virtualEnvironment = "venv"

    vKeepMenu = True
    while vKeepMenu:
        print(f"{Fore.RED}{Style.BRIGHT}Virtual Environment {Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Project Path: {Style.RESET_ALL}{Fore.MAGENTA}{projectPath}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}Virtual Environment Name: {Style.RESET_ALL}{Fore.MAGENTA}{virtualEnvironment}{Style.RESET_ALL}")
        print("")
        print(f"{Fore.YELLOW}{Style.BRIGHT}1. Create Virtual Environment {Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{Style.BRIGHT}2. Activate Virtual Environment {Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{Style.BRIGHT}3. Delete Virtual Environment {Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{Style.BRIGHT}4. List Virtual Environment {Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{Style.BRIGHT}5. Create Requirements File {Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{Style.BRIGHT}6. Create .Gitignore File {Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{Style.BRIGHT}7. Create Development Structure {Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{Style.BRIGHT}8. Exit {Style.RESET_ALL}")
        print("")
        option = input(f"{Fore.GREEN}{Style.BRIGHT}Select Option: {Style.RESET_ALL}")
        if option == "1":
            print(f"{Fore.YELLOW}{Style.BRIGHT}Creating Virtual Environment {Style.RESET_ALL}")
            virtualEnvironment = VirtualEnvironment(projectPath, virtualEnvironment)
            vKeepMenu = False
            virtualEnvironment.createVirtualEnvironment()
            exit()
        elif option == "2":
            print(f"{Fore.YELLOW}{Style.BRIGHT}Activating Virtual Environment {Style.RESET_ALL}")
            virtualEnvironment = VirtualEnvironment(projectPath, virtualEnvironment)
            virtualEnvironment.activateVirtualEnvironment()
        elif option == "3":
            print(f"{Fore.YELLOW}{Style.BRIGHT}Deleting Virtual Environment {Style.RESET_ALL}")
            virtualEnvironment = VirtualEnvironment(projectPath, virtualEnvironment)
            virtualEnvironment.deleteVirtualEnvironment()
        elif option == "4":
            print(f"{Fore.YELLOW}{Style.BRIGHT}Listing Virtual Environment {Style.RESET_ALL}")
            virtualEnvironment = VirtualEnvironment(projectPath, virtualEnvironment)
            virtualEnvironment.listVirtualEnvironment()
        elif option == "5":
            print(f"{Fore.YELLOW}{Style.BRIGHT}Creating Requirements File {Style.RESET_ALL}")
            virtualEnvironment = VirtualEnvironment(projectPath, virtualEnvironment)
            virtualEnvironment.creatingRequirements()
        elif option == "6":
            print(f"{Fore.YELLOW}{Style.BRIGHT}Creating .Gitignore File {Style.RESET_ALL}")
            virtualEnvironment = VirtualEnvironment(projectPath, virtualEnvironment)
            virtualEnvironment.creatingGitignore()
        elif option == "7":
            print(f"{Fore.YELLOW}{Style.BRIGHT}Creating Development Structure {Style.RESET_ALL}")
            virtualEnvironment = VirtualEnvironment(projectPath, virtualEnvironment)
            virtualEnvironment.creatingDevelopmentStructure()
        elif option == "8":
            print(f"{Fore.YELLOW}{Style.BRIGHT}Exiting {Style.RESET_ALL}")
            vKeepMenu = False
            exit()
        else:
            print(f"{Fore.RED}{Style.BRIGHT}Invalid Option {Style.RESET_ALL}")
            vKeepMenu = False
            exit()
        print("")
    pass