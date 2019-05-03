# Intelligent Traffic Controller Using Fuzzy Logic

The purpose of this project is to address the design and implementation of an intelligent traffic light system based on fuzzy logic technology. Using Python, a fuzzy logic system has been developed to determine the wait time of a typical traffic junction. The problem is highly graphical in nature and simulates traffic conditions of an intersection with the intention to increase or mitigate wait times when needed based off certain conditions.

<a target="_blank"><img src="http://i65.tinypic.com/2ibj22a.png" border="0" alt="traffic System"></a>

## Prerequisites

In order to develop an intelligent traffic light system using fuzzy logic, it is crucial to understand how normal traffic junctions operate. For this we can consider a simple four way intersection and observe its state diagram.  This four way intersection is made of two streets Main and Side. Assuming there are no turning lanes, the intersection can be boiled down to four different states. The flow of the traffic diagram is a loop and the timing of each signal is constant.
<a target="_blank"><img align = "right" src="http://i63.tinypic.com/idy8ic.png" border="0" alt="State Diagram"></a>
This traffic system can be represented with four states. Each of theses states ensure there is no possible combination in which the two streets both have green lights. The system also ensures that there is a state between the switching of green lights that gives time for remaining cars to make it through. When starting at state “0 0”, as long as the timer is counting or there are no cars waiting on the other street, the state will remain on “0 0”. If the timer is not counting and cars are waiting to move through the intersection, the state will change to yellow for five seconds. When the short timer stops counting the system will finally give permission to the adjacent street allowing cars to move through. A similar process is carried out with the states “1 1” and “1 0” which eventually loop back to the original starting state. Although this is a very simple example of a traffic light system, the foundations are in place for developing more complicated traffic systems using fuzzy logic controllers. 

