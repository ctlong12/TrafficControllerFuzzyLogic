# Intelligent Traffic Controller Using Fuzzy Logic

The purpose of this project is to address the design and implementation of an intelligent traffic light system based on fuzzy logic technology. Using Python, a fuzzy logic system has been developed to determine the wait time of a typical traffic junction.

<a target="_blank"><img width="950" height="400" src="https://raw.githubusercontent.com/ctlong12/TrafficControllerFuzzyLogic/master/images/traffic-lights.png" align = "center" border="0" alt="High Level Overview"></a>

## Prerequisites

In order to develop an intelligent traffic light system using fuzzy logic, it is crucial to understand how normal traffic junctions operate. For this we can consider a simple four way intersection and observe its state diagram.  This four way intersection is made of two streets Main and Side. Assuming there are no turning lanes, the intersection can be boiled down to four different states. The flow of the traffic diagram is a loop and the timing of each signal is constant.<a target="_blank"><img align="right" width="525" height="475" src="https://raw.githubusercontent.com/ctlong12/TrafficControllerFuzzyLogic/master/images/state-diagram.png" border="0" alt="State Diagram"></a> This traffic system can be represented with four states. Each of theses states ensure there is no possible combination in which the two streets both have green lights. The system also ensures that there is a state between the switching of green lights that gives time for remaining cars to make it through. When starting at state “0 0”, as long as the timer is counting or there are no cars waiting on the other street, the state will remain on “0 0”. If the timer is not counting and cars are waiting to move through the intersection, the state will change to yellow for five seconds. When the short timer stops counting the system will finally give permission to the adjacent street allowing cars to move through. A similar process is carried out with the states “1 1” and “1 0” which eventually loop back to the original starting state. Although this is a very simple example of a traffic light system, the foundations are in place for developing more complicated traffic systems using fuzzy logic controllers. 

## The Fuzzy Logic Controller

At its core, fuzzy logic is an approach to computing based on "degrees of truth" rather than the usual "true or false" boolean logic on which modern computers are based on. For example, if trying to describe how honest someone is, we might try and be more specific than simple stating he/she is honest or dishonest. One might specify that someone is a little honest, very honest, or not honest at all. 

<a target="_blank"><img src="https://raw.githubusercontent.com/ctlong12/TrafficControllerFuzzyLogic/master/images/state-diagram.png" border="0" alt="Fuzzy Logic"></a>

Fuzzy logic is derived from this idea and can be applied in many different computational situations. This fuzzy logic traffic system isn’t like that of a typical traffic system. The model observes the number of cars currently waiting as well as the number of cars coming into the intersection. Rules are developed to generically describe the status of a single street of the intersection. Anywhere from 0 - 10 cars can be described as minimal traffic, while 50 or more cars can be described as standstill traffic. The same logic is applied to cars that are coming into the intersection giving an overall sense of busy the street is and as well as how busy the street may become. 

<a target="_blank"><img src="http://i65.tinypic.com/2z4zkwh.png" border="0" alt="System Design"></a>

## The Implementation

The implementation of this intelligent traffic system with fuzzy logic focuses on determining the wait time for a given side of the street. When given the number of cars waiting at the intersection along with the number of oncoming cars, the program will perform the fuzzification and defuzzification process in order to suggest the approximate wait time. During the fuzzification process each of the values are passed into their own functions. These functions are the fuzzification process which determines the fuzzy set for each of the sensors. 

<a target="_blank"><img src="http://i64.tinypic.com/207vkgo.png" border="0" alt="Fuzzy System"></a>

The fuzzy sets returned from these functions are then used to infer the linguistic value corresponding to how busy the particular intersection might be. After an inference as to what the state of the intersection may be, that inference is passed into the defuzzification process which outputs the the suggested wait time for the cars on the corresponding street.

## Conclusion

Smarter, faster, and more dynamic traffic systems are becoming necessary in cities with rapid population growth. These intelligent traffic light systems have proven to have positive effects in society and have challenged computer scientists around the world to try and create better systems for traffic management. Further development into the current state of this fuzzy logic controller would yield better results, for it only has the capabilities of determining the status of a single street. The future of intelligent traffic management systems is bright and it is only a matter of time before systems such as these are implemented in many cities around the world. 
