See "HowToRun_minAone_2beam" for a full(er) guide on how to run this code.

PREREQUISITES:
- Anaconda environment setup (sympy package)

The 'go' execuetable is a bash script that compiles and runs the code. 
Use that as a model for the compile-run procedure.
The final ./neutrinos_cpp execution will take a long time. Confirm that it runs, then run ./submit.sbatch.

Code inputs (see specs.txt):
- equations.txt
- specs.txt
- B*.txt
- P*.txt
   
Compile outputs:
- Makefile
- *.cpp, *.hpp, *.o files
- neutrinos.opt

make outputs:
- ipopt.out
   
Code outputs:
- *.dat files

