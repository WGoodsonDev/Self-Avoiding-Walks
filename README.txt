Warren Goodson
Brandon Adamson-Rakidzich

FINAL PROJECT: SELF-AVOIDING WALKS

CS 454 Theory of Computation 
Dr. Ravikumar
Sonoma State University
Spring 2019

Description of source files:

    startk4.py
        Contains our DFA implementation for k = 4, in both UDLR and 1234 versions.
        Prompts user for a walk length, outputs number of walks of that length that do not have cycles of length 4 or less.

    k6.py
        Contains our DFA implementation for k = 6 using 1234 reduction.
        Prompts user for a walk length, outputs number of walks of that length that do not have cycles of length 6 or less.

    dfaGen.py
        Contains our attempt at implementing the algorithm from [Pönitz, André and Peter Tittmann: Improved Upper Bounds for Self-Avoiding Walks in Zd, The Electronic Journal of Combinatorics, 2000]. 
        Prompts user for a maximum loop size k (k is made even if not already even).
        Outputs number of unique walks that can be extended to a loop in k or fewer total steps.
        Outputs all such strings either to the console or to file, depending on user choice.

Other files:

    firstk4_Transition_Table.ods
        Spreadsheet containing our original DFA transition function (UDLR) for k = 4.

    secondk4_Transition_Table.ods
        Spreadsheet containing our DFA transition function (1234) for k = 4.

    k6_Transition_Table.ods
        Spreadsheet containing our DFA transition function (1234) for k = 6.
    
    k14_walks.txt
        Sample output from dfaGen.py when k = 14

    k16_walks.txt
        Sample output from dfaGen.py when k = 16

    CS454_Final_Project_Report.pdf
        Our final report.