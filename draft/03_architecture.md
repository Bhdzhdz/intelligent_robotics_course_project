<!-- Robot Architecture: This section must contain the following subsections, and it should be
around 2 to 5 pages long:
a. Architecture: Diagram or image where the architecture is shown, and the explanation of such architecture.
b. Behaviors: List of all behaviors to be used and their explanation -->

# Architecture

![Robot Architecture](images/architecture.png){.center}

## Modules description

### Collide

Receives a collision message from the Roomba bumper sensor, and sends a message to the Robot to stop moving.

### Feel force

Receives a force message from the Roomba's infrared sensors and the Kinect's depth sensor, using this info the Roomba will detect what direction will get it away from the walls.

### Avoid

Determine if a wall is too close. Uses the map and environment information.

### Wall/obstacle detection

Using the cloud point generate planes to represent walls and obstacles.

### Map update

Add new detected wall and obstacles to the 3D map.

### Virtual position correction

Using odometry techniques and landmarks gathered from the camera, correct the virtual position to better represent the real position of the robot.

### Find path to unexplored

Find the closest unexplored reachable position. 

### Direct towards unexplored

Calculate the necessary moves to the reach the next position to explore.

### Calculate safe direction

Using the info from the "Direct towards unexplored" and "Avoid" modules determine the value the motors need to have.

`\pagebreak`{=latex}
