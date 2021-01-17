# openSIF Reliability Calculator
openSIF is a program designed to;
- Calculate Safety Instrumented Function (SIF) subsystem reliability based upon ISA-TR84.00.02-2015 Table C.2.
simplified equations.
- Identify subsystem Hardware Fault Tolerance (HFT).
- Calculate SIF total Probability of Failure on Demand average (PFDavg) based upon ISA-TR84.00.02-2015 Equation 8.1 and Risk Reduction Factor
(RRF) for most common voting configurations. 
- Identify SIF Safety Integrity Level (SIL).
- Record and retain date/time stamped versions of results and inputted data within a text file and associated folder.

## Notes and limitations
- Voted subsystems are limited to having the same devices i.e. same failure rate data, proof test interval, etc.
- Calculations are for Low Demand mode functions only.
- Calculations are simplified to exclude Diagnostic Interval (DI) due to negligible contribution to subsystem PFDavg.

## Use
- openSIF is designed for use on Windows. 
- Download and run openSIF.exe. 
- Install the application to a folder location different from that of the downloaded installation file. 
Take note of the folder location as this is where you will run the application from and where calculations will be saved.
- Navigate to the folder location and run the application file openSIF.exe.
- Follow the command prompt instructions.

## Use notes
- Source code is included for verification purposes within the file openSIF.py.
- openSIF is released to the public domain, which means you can modify it, redistribute it or use it however you like.
