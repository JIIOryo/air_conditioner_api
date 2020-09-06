import subprocess

def run_air_conditioner(
    irrppy_path: str,
    command_file_path: str,
    gpio: int,
    command: str,
):
    cmd = f'python3 {irrppy_path} -p -g{gpio} -f {command_file_path} {command}'
    subprocess.Popen(cmd.split())
    return
