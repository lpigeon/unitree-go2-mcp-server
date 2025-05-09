# MCP Functions

This is a list of functions that can be used in the GO2 MCP Server.

## get_topics
- **Purpose**: Retrieves the list of available topics from the robot's ROS2 system.
- **Returns**: 
  - `{ "topics": List[str] }` (if using ROS2 directly)
  - `{ "topics": List[str], "types": List[str] }` (if using rosbridge)
  - Returns `"No topics found"` if no topics are available.

## pub_wirelesscontroller
- **Purpose**: Publishes a custom wirelesscontroller command to control the robot's movement and actions.
- **Parameters**:
  - `linear_x` (float): Linear velocity in the x direction (m/s)
  - `linear_y` (float): Linear velocity in the y direction (m/s)
  - `yaw` (float): Yaw rotation velocity (rad/s)
  - `pitch` (float): Pitch rotation velocity (rad/s)
  - `keys` (int): Button state value
  - `duration` (float, optional): Duration to send the command (seconds, default: 0)
- **Returns**: Result of the publish command (success status and message)

## stand_up_from_a_fall
- **Purpose**: Makes the robot stand up if it has fallen.
- **Returns**: Result message of the action

## stretch
- **Purpose**: Makes the robot perform a stretching motion.
- **Returns**: Result message of the action

## shake_hands
- **Purpose**: Makes the robot perform a handshake gesture.
- **Returns**: Result message of the action

## love
- **Purpose**: Makes the robot perform a 'love' gesture.
- **Returns**: Result message of the action

## pounce
- **Purpose**: Makes the robot perform a pouncing motion.
- **Returns**: Result message of the action

## jump_forward
- **Purpose**: Makes the robot jump forward.
- **Returns**: Result message of the action

## sit_down
- **Purpose**: Makes the robot sit down.
- **Returns**: Result message of the action

## greet
- **Purpose**: Makes the robot perform a greeting gesture.
- **Returns**: Result message of the action

## dance
- **Purpose**: Makes the robot perform a dance motion.
- **Returns**: Result message of the action

## stop
- **Purpose**: Stops all current robot actions.
- **Returns**: Result message of the action