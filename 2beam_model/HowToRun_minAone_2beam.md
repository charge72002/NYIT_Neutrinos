# Running minAone optimization code

Sherry Wong

Last updated 28 Jun 2022

## Usage

`equations.txt` → python_scripts directory

1. Setup python dependencies (sympy)
`conda create --name anaconda_env anaconda
 conda activate anaconda-env`
2. Collect all your data files based on `specs.txt`
3. `python original_minaone.py` → Makefile
4. `make` → neutrinos_cpp executable
5. `./neutrinos.cpp`
6. `submit.sbatch` → .dat files (a LOT for 8-beam; ~256MB)

Troubleshooting a Segfault:

- Are all the data files correctly labeled in `specs.txt`? Are they all in the directory?
- Are all data files the right/same length? (Use `wc`)
- Special characters like ^M don't matter, but can be viewed with `vim -b FILENAME`