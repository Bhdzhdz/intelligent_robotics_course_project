<!-- Project characterization: This section must contain the following subsections, and it
should be around 5 to 10 pages long:
    a. Task description
    b. Environment description, add images or figures with the measurements and specific characteristics of your environment. Whatever objects, obstacles, etc., you will use must be described.
    c. Robot description
        i. Sensors: Describe which sensors will be used and add the experiments performed for each sensor, explain these experiments and the results found.
        ii. Actuators: Describe which actuators will be used and add the experiments performed for each of them, explain these experiments and the results found. -->



# Project characterization

## Task description

The robot will need to navigate through the environment, avoid obstacles, decide which area of the environment is yet to be explored and then move to it. Using a Kinect, the robot will be able to detect the presence of obstacles and walls, saving the information to create a map of the environment. The robot will stop the exploration when it as no way to move towards the unexplored area, this could be because the robot has mapped the whole environment or because there is no way to move path wide enough to reach the unexplored area.

## Environment description

The environment that the robot must map consists of a 3x3 meter space with box-like obstacles. 

* Wall: A wall is a rectangular area of the environment that is not traversable, it defines the boundaries of 3x3 meter space. To create a wall we will use the plywood sheet available in the lab or the cardboard boxes we can gather. The approximate dimensions of the walls should be 3mx1mx1cm.

* Obstacle: An obstacle is a rectangular area of the environment that is not traversable, To create an obstacle we will use the cardboard boxes we can gather. All three dimensions of the obstacles should be between 20 cm and 40 cm.

![Environment](images/enviroment.png){.center}

## Robot description



`\pagebreak`{=latex}