# Inference-by-Approximation

This python code performs Inference by Approximation which consists of:- <br />
1. Prior Sampling<br />
2. Rejection Sampling<br />
3. Likelihood Weighting.<br />

The program is built for the following Bayesian Network<br /> 

        
          
                        ___________                   ____________
                        |Burglary|                   |Earthquake|
          
                                        ________
                                        |Alarm|
                  
                        _______________               _____________
                        |John Calling|               |Mary Calling|
<br />
Where dependcies are as follows:
<br />
Burglary--------->Alarm<br />
Earthquake------->Alarm<br />
Alarm----------->JohnCalling<br />
Alarm----------->MaryCalling<br />

#Input Abbreviation<br />

Burglary--B<br />
Earthquake--E<br />
Alarm----A<br />
JohnCalling---J<br />
MaryCalling---M<br />
<br />
#INPUT:<br />
Eg:<br />
    2 1<br />
    J T<br />
    M T<br />
    A<br />

Input 2 & 1 signifies the number of evidence and query variables respectively.<br />
J T<br />
M T<br />
These are the Evidence Variables with their truth values being either True or False given as T and F respectively.<br />
A <br />
This represents the query variable whose truth value is always true.<br />



#OUTPUT:<br />
    Output gives the probabiility values for the Query Variable(s).


    

