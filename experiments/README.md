# Contents:

- [Infrared1](#infrared1)
- [Infrared2](#infrared2)
- [Motors1](#motors1)

# Infrared1

## Roomba infrared sensors test

### Goal

Test the integrated infrared sensors of the Roomba, and see if they are
working properly.

### Setup

We will place the Roomba at different distances from the wall, and for
each sensor compare the distance measured by the sensor with the real
distance.

This experiment will be divided into `infrared1.1`, \``infrared1.2`,
`infrared1.3`, `infrared1.4`.

![The experiment will be performed with each
sensor](images/roomba_infrared_1.png)

The distances that we will measure are: 5 cm, 15 cm, 30 cm, 50 cm, 75 cm
and 100 cm.

For each sensor and for each distance, we will take three measurements,
and use its mean to calculate the error.

<table>
<thead>
  <tr>
    <th>Real distance</th>
    <th>Measurement</th>
    <th>Error</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="3">S1_A</td>
    <td>S1_a1</td>
    <td rowspan="3">S1_E_a</td>
  </tr>
  <tr>
    <td>S1_a2</td>
  </tr>
  <tr>
    <td>S1_a3</td>
  </tr>
  <tr>
    <td rowspan="3">S2_A</td>
    <td>S2_a1</td>
    <td rowspan="3">S2_E_a</td>
  </tr>
  <tr>
    <td>S2_a2</td>
  </tr>
  <tr>
    <td>S2_a3</td>
  </tr>
  <tr>
    <td>...</td>
    <td>...</td>
    <td>...</td>
  </tr>
</tbody>
</table>

### Expected Results

We expect that error to be similar among all sensors, that it increases
with the distance, and it to be around 10%.

# Infrared2

## Kinect infrared sensors test

### Goal

Test the integrated infrared sensors of the Kinect, and see if they are
working properly.

### Setup

We will place the Roomba at different distances from the wall, and for
each sensor compare the distance measured by the sensor with the real
distance.

The distances that we will measure are: 5 cm, 15 cm, 30 cm, 50 cm, 75 cm
and 100 cm.

For each sensor and for each distance, we will take three measurements,
and use its mean to calculate the error.

<table>
<thead>
  <tr>
    <th>Real distance</th>
    <th>Measurement</th>
    <th>Error</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="3">K_A</td>
    <td>K_a1</td>
    <td rowspan="3">K_E_a</td>
  </tr>
  <tr>
    <td>K_a2</td>
  </tr>
  <tr>
    <td>K_a3</td>
  </tr>
</tbody>
</table>

### Expected Results

We expect that error increases with the distance, and it to be around
15%.

# Motors1

## Forward wheel motors test

### Goal

Test the motors of the Roomba, and see if they are working properly for moving tasks.
This is necessary to command and track movement.

### Setup

We will make the Roomba move forward different distances, and for each
distance we will make three measurements of the distance traveled by the
Roomba. We will check that the Roomba is moving towards the expected
position.

The Roomba will move forward for the following distances: 60 cm, 80 cm,
100 cm.

We will repeat the experiment three times for each distance. We will
take the mean of the three measurements to calculate the error.

![The Roomba to should move forward without
deviation](images/roomba_motors_1.png)

### Expected Results

We are expecting that the Roomba to move forward without deviation for
each distance. The error should be around 5%.


# Motors2

## Rotate wheel motors test

### Goal

Test the motors of the Roomba, and see if they are working properly for rotating tasks.
This is necessary to command and track movement.

### Setup

