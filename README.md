# Unitree Go2 MCP Server
![ROS 2](https://img.shields.io/badge/ROS_2-Foxy|Humble-blue)
![Static Badge](https://img.shields.io/badge/License-Apache2.0-green)

<center><img src="https://github.com/lpigeon/unitree-go2-mcp-server/blob/main/img/thumbnail.png" width="800"/></center>

The **Unitree Go2 MCP Server** is a server built on the Model Context Protocol (MCP) that enables users to control the Unitree Go2 robot using natural language commands interpreted by a Large Language Model (LLM). These commands are translated into ROS2 instructions, allowing the robot to perform corresponding actions.

<a href="https://glama.ai/mcp/servers/@lpigeon/unitree-go2-mcp-server">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/@lpigeon/unitree-go2-mcp-server/badge" alt="Unitree Go2 Server MCP server" />
</a>

## Requirements

- **Unitree Go2 robot**
- **Ubuntu 20.04 or 22.04**
- **ROS2 environment** : [Humble](https://docs.ros.org/en/humble/Installation.html)(recommended) or [Foxy](https://docs.ros.org/en/foxy/Installation.html)

## MCP Functions

You can find the list of functions in the [MCPFUNCTIONS.md](MCPFUNCTIONS.md).

## Installation

### 1. Setup `unitree_ros2` environment

https://github.com/unitreerobotics/unitree_ros2

- **You need to complete the setup up to `Step 2: Connect and test` in the repository linked above.**

### 2. Clone this repository

```bash
git clone https://github.com/lpigeon/unitree-go2-mcp-server.git
cd unitree-go2-mcp-server
```

### 3. `uv` Installation
- To install `uv`, you can use the following command:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
or
```bash
pip install uv
```

- Create virtual environment and activate it (Optional)
```bash
uv venv
source .venv/bin/activate
```

### 4. MCP Server Configuration
Set MCP setting to mcp.json.

**Please keep in mind that the configuration must be done on the PC connected to the Go2.**

```bash
{
    "mcpServers": {
        "unitree-go2-mcp-server": {
            "command": "uv",
            "args": [
              "--directory",
              "/ABSOLUTE/PATH/TO/PARENT/FOLDER/unitree-go2-mcp-server",
              "run",
              "server.py"
            ]
        }
    }
}
```

If you use Claude Desktop, you can find mcp.json using the following command:

- MacOS
```bash
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

- Linux(Ubuntu)
  
You can install Claude Desktop to use [claude-desktop-debian](https://github.com/aaddrick/claude-desktop-debian).

```bash
code ~/.config/Claude/claude_desktop_config.json
```

- Windows
```bash
code $env:AppData\Claude\claude_desktop_config.json
```

## How To Use
### 1. Set `UNITREE_ROS2_SETUP_SH_PATH`.
- Open `server.py` and change your `UNITREE_ROS2_SETUP_SH_PATH` (eg. `/home/lpigeon/unitree_ros2/setup.sh`)

#### If you use `rosbridge`, you need Set IP and Port to connect rosbridge (Optional).
- Open `server.py` and change your `LOCAL_IP`, `ROSBRIDGE_IP` and `ROSBRIDGE_PORT`. (`ROSBRIDGE_PORT`'s default value is `9090`)

### 2. Check the Go2 robot is connected to the network.
Type the following command in the terminal.
```bash
ros2 topic list
```
You should see the following topic:
```bash
/wirelesscontroller
```
**If you don't see the topic, check the connection between the Go2 robot and the network.**

### 3. Run any AI system that has imported `unitree-go2-mcp-server`.

### 4. Type "Make the Go2 robot move forward at a velocity of 0.5 m/s for 3 seconds.".

<center><img src="https://github.com/lpigeon/unitree-go2-mcp-server/blob/main/img/how_to_use_1.png" width="500"/></center>

### 5. Check the Go2 robot's movement.

<center><img src="https://github.com/lpigeon/unitree-go2-mcp-server/blob/main/img/how_to_use_2.gif" width="500"/></center>

### 6. Type what you want to do and Enjoy!

## Contextual Understanding
When you type a command like "It looks like the Go2 is getting tired," the LLM interprets this contextually — understanding that the robot might need a break or some form of stretching!

<center><img src="https://github.com/lpigeon/unitree-go2-mcp-server/blob/main/img/contextual_understanding.gif" width="800"/></center>

## Simple Task
This task is a comprehensive demo task showcasing the Unitree Go2 robot's obstacle avoidance, direction changing, and user interaction capabilities.

<center><img src="https://github.com/lpigeon/unitree-go2-mcp-server/blob/main/img/task_test.gif" width="800"/></center>

## Contributing
Contributions are welcome!  
Whether you're fixing a typo, adding a new function, or suggesting improvements, your help is appreciated.  
Please follow the [contributing guidelines](CONTRIBUTING.md) for more details on how to contribute to this project.
