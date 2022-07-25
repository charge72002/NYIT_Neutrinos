# Running minAone optimization code

Sherry Wong

Last updated 25 Jul 2022

## Usage

`equations.txt` → python_scripts directory

1. Setup python dependencies (sympy)
`conda create --name anaconda_env anaconda
 conda activate anaconda-env`
2. Collect all your data files based on `specs.txt`
3. `python original_minaone.py` → Makefile
4. `make` → neutrinos_cpp executable
5. `./neutrinos.cpp` OR `submit.sbatch` → .dat files (a LOT for 8-beam; ~256MB), ipopt.out

### Troubleshooting a Segfault:

- Are all the data files correctly labeled in `specs.txt`? Are they all in the directory?
- Are all data files the right/same length? (Use `wc`)
- Special characters can be viewed with `vim -b FILENAME`
    - trailing whitespace “ “ matters
    - linebreak-likes “^M“ might matter
- If minAone.py runs, equations.txt is OK
- If neutrinos_cpp runs, specs.txt is OK

## Troubleshooting other issues/dependencies

```bash
==> WARNING: A newer version of conda exists. <==
  current version: 4.6.12
  latest version: 4.13.0

Please update conda by running

    $ conda update -n base -c defaults conda
```

## Jupyter notebook tunnel:

On remote, run`jupyter notebook --no-browser --port=NNNN`

Prerequisite: `module add anaconda`

On local, run `ssh -t -t USERNAME[@hpc-logon.nyit.edu](mailto:aahmet03@hpc-logon.nyit.edu) -L NNNN:localhost:NNNN ssh node002 -L NNNN:localhost:NNNN`

you ran `ssh -t -t [swong25@10.10.32.70](mailto:swong25@10.10.32.70) -L 6969:localhost:6969 ssh node002 -L 8892:localhost:6969`

## GitHub on the cluster

prequisites:

- SSH key (haven’t figured out how that works yet)
- OR Personal Access Token
    
    `git clone <URL>`
    
    `git add FILES; git commit -m "MESSAGE"`
    
    `git push origin master`