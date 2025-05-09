import os
import subprocess
from typing import Any

class Ros2Manager:
    def __init__(self, setup_sh_path: str):
        self.setup_sh_path = setup_sh_path
        
    def get_topics(self) -> list[str]:
        command = f"source {self.setup_sh_path} && ros2 topic list"
        output = subprocess.check_output(command, shell=True, executable='/bin/bash').decode()
        return output.split('\n')
