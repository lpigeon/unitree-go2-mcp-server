import os
import subprocess
from typing import Any

class WirelessController:
    """
    Publishes WirelessController messages using ros2 topic pub via subprocess.
    
    Message fields:
      - float32 lx : left stick x axis (-1 ~ 1) -> robot move left and right
      - float32 ly : left stick y axis (-1 ~ 1) -> robot move forward and backward
      - float32 rx : right stick x axis (-1 ~ 1) -> robot rotate left and right
      - float32 ry : right stick y axis (-1 ~ 1) -> robot rotate up and down
      - uint16 keys : button state
    """
    def __init__(self, topic: str = "/wirelesscontroller", msg_type: str = "unitree_go/msg/WirelessController", setup_sh_path: str = "your_path_to_setup.sh"):
        self.topic = topic
        self.msg_type = msg_type
        self.rate = 10 # Hz
        self.setup_sh_path = setup_sh_path
        
    def execute(self, command: str) -> tuple[bool, Any]:
        try:
            output = subprocess.check_output(command, shell=True, executable='/bin/bash').decode()
            return True, output
        except Exception as e:
            return False, str(e)

    def publish(self, lx: float, ly: float, rx: float, ry: float, keys: int, duration: float = 0) -> tuple[bool, Any]:
        if self.rate > 0 and duration > 0:
            t = int(self.rate * duration)
            rate_opt = f"-r {self.rate} --times {t}"
        else:
            rate_opt = "-1"
        command = (
            f"source {self.setup_sh_path} && "
            f"ros2 topic pub {self.topic} {self.msg_type} "
            f"'{{lx: {lx}, ly: {ly}, rx: {rx}, ry: {ry}, keys: {keys}}}' {rate_opt}"
        )
        return self.execute(command)

    def _customised_movements(self, keys: int, rate: int = None, times: int = 5) -> tuple[bool, Any]:
        rate = rate if rate is not None else self.rate
        rate_opt = f"-r {rate} --times {times}"
        command = (
            f"source {self.setup_sh_path} && "
            f"ros2 topic pub {self.topic} {self.msg_type} "
            f"'{{lx: 0.0, ly: 0.0, rx: 0.0, ry: 0.0, keys: {keys}}}' {rate_opt}"
        )
        return self.execute(command)
    
    def stand_up_from_a_fall(self):
        return self._customised_movements(keys=1056)
    
    def stretch(self):
        self.stand_up_from_a_fall()
        return self._customised_movements(keys=272)

    def shake_hands(self):
        self.stand_up_from_a_fall()
        return self._customised_movements(keys=528)
    
    def love(self):
        self.stand_up_from_a_fall() 
        return self._customised_movements(keys=2064)
    
    def pounce(self):
        self.stand_up_from_a_fall()
        return self._customised_movements(keys=1025)

    def jump_forward(self):
        self.stand_up_from_a_fall()
        return self._customised_movements(keys=257)
    
    def sit_down(self):
        self.stand_up_from_a_fall()
        return self._customised_movements(keys=513)

    def greet(self):
        self.stand_up_from_a_fall()
        return self._customised_movements(keys=258)
    
    def dance(self):
        self.stand_up_from_a_fall()
        return self._customised_movements(keys=514)
    
    def stop(self):
        return self._customised_movements(keys=0, times=3)
