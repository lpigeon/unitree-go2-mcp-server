from mcp.server.fastmcp import FastMCP
from utils.websocket_manager import WebSocketManager
from utils.ros2_manager import Ros2Manager
from msgs import WirelessController

# UNITREE ROS2  
UNITREE_ROS2_SETUP_SH_PATH = "/home/lpigeon/unitree_ros2/setup.sh"

# ROSBRIDGE (Optional)
use_rosbridge = False
LOCAL_IP = "192.168.50.90"
ROSBRIDGE_IP = "192.168.50.90"
ROSBRIDGE_PORT = 9090

mcp = FastMCP("go2-mcp-server")
ws_manager = WebSocketManager(ROSBRIDGE_IP, ROSBRIDGE_PORT, LOCAL_IP)
ros2_manager = Ros2Manager(UNITREE_ROS2_SETUP_SH_PATH)
wirelesscontroller = WirelessController(topic="/wirelesscontroller", msg_type="unitree_go/msg/WirelessController", setup_sh_path=UNITREE_ROS2_SETUP_SH_PATH)

@mcp.tool()
def get_topics():
    if use_rosbridge:
        topic_info = ws_manager.get_topics()
        ws_manager.close()
        
        if topic_info:
            topics, types = zip(*topic_info)
            return {
                "topics": list(topics),
                "types": list(types)
            }
        else:
            return "No topics found"
    else:
        topics = ros2_manager.get_topics()
        return {
            "topics": topics
        }
        
def convert_velocity_to_wirelesscontroller(velocity: float):
    if velocity > 3.7:
        velocity = 3.7
    elif velocity < -3.7:
        velocity = -3.7
    # -3.7 ~ 3.7 to -1.0 ~ 1.0
    return velocity / 3.7

@mcp.tool()
def pub_wirelesscontroller(linear_x: float, linear_y: float, yaw: float, pitch: float, keys: int, duration: float = 0):
    lx = convert_velocity_to_wirelesscontroller(linear_y)
    ly = convert_velocity_to_wirelesscontroller(linear_x)
    rx = convert_velocity_to_wirelesscontroller(-yaw)
    ry = convert_velocity_to_wirelesscontroller(pitch)
    
    result, msg = wirelesscontroller.publish(lx, ly, rx, ry, keys, duration)
    wirelesscontroller.stop()
    return result

@mcp.tool()
def stand_up_from_a_fall():
    _, msg = wirelesscontroller.stand_up_from_a_fall()
    return msg

@mcp.tool()
def stretch():
    _, msg = wirelesscontroller.stretch()
    wirelesscontroller.stop()
    return msg

@mcp.tool()
def shake_hands():
    _, msg = wirelesscontroller.shake_hands()
    wirelesscontroller.stop()
    return msg

@mcp.tool()
def love():
    _, msg = wirelesscontroller.love()
    wirelesscontroller.stop()
    return msg
    
@mcp.tool()
def pounce():
    _, msg = wirelesscontroller.pounce()
    wirelesscontroller.stop()
    return msg

@mcp.tool()
def jump_forward():
    _, msg = wirelesscontroller.jump_forward()
    wirelesscontroller.stop()
    return msg

@mcp.tool()
def sit_down():
    _, msg = wirelesscontroller.sit_down()
    wirelesscontroller.stop()
    return msg

@mcp.tool()
def greet():
    _, msg = wirelesscontroller.greet()
    wirelesscontroller.stop()
    return msg

@mcp.tool()
def dance():
    _, msg = wirelesscontroller.dance()
    wirelesscontroller.stop()
    return msg

@mcp.tool()
def stop():
    _, msg = wirelesscontroller.stop()
    return msg

if __name__ == "__main__":
    mcp.run(transport="stdio")
