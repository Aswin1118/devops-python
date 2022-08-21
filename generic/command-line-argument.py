import os
import subprocess


def execute_shell():

    script_dir = os.path.dirname(__file__)

    script_abosulte_path = os.path.join("operating-system/files/script.sh")

    subprocess.call(['sh', script_abosulte_path])

execute_shell()
