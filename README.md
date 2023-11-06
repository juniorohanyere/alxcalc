# alxcalc.

`alxcalc` is a tool that enables `ALX learners` to predict/calculate their expected avarage score for a particular month, project, or task, based on the learners' computation/input.

## Installation.

```bash
git clone https://github.com/juniorohanyere/alxcalc.git
```
```bash
cd alxcalc
```
```bash
make
```

## Usage.

**Getting Started:**

Like a tree, a user can choose to input values based on project score, task score, or checker status (whether a check is green or not) while taking note of the deadline space where necessary.
A project score input should be either an integer or floating point value terminated with the percentage `%` sign.
A task score input should aslo be either an integer or floating point value, terminated with the percentage `%` sign as well.
To calculate scores based on checker status, the user has to specify a deadline. The deadline value is an integer value between `0` (inclusive) and `2` (inclusive). `0` denotes *before end of first deadline*, `1` denotes *before end of second deadline*, and `2` denotes *after end of second deadline*.
A check value (checker status) should be an integer value of either `0` or `1`, **like a binary switch,** yeah, funny. `0` denotes a `green check`, `1` denotes a `red check`.
Mandatory or optional task is managed or preset by the program, so a user don't have to provide this input.

In all, the format for each label/field in the input file is **<label>==<value>**, no spaces between. Empty lines are also vital. A user is only expected to input values where appropriate, otherwise, the program stands a chance of producing inaccurate results.


```bash
alxcalc   # brief introduction + developer's name + version number
```
```bash
alxcalc -h    # display help message (man page)
```
```bash
alxcalc -v    # display version number
```

**Global Operations:**

*Specify -r, -f or combination of both at the end of the line to perform global operations.*

```bash
alxcalc -r    # reset values in input file to empty
```
```bash
alxcalc -f    # warn for detected empty values, empty is different from a zero value
```
```bash
alxcalc -m <int> -p <str> -t <int> -rf
```

**Month:**

```bash
alxcalc -M <int>  # open editor for the given month
```
```bash
alxcalc -m <int>  # display result for the given month
```
```bash
alxcalc -fm <int> # don't skip empty values, treat as warning (--)
                    # without the -f flag, empty value is treated as zero
```
```bash
alxcalc -rfm <int> # reset and don't skip empty values
```

**Project:**

```bash
alxcalc -M <int> -p <str>
```
```bash
alxcalc -m <int> -rfp <str>
```

**Task:**

```bash
alxcalc -m <int> -fp <str> -rt <int>
```
```bash
alxcalc -M <int> -p <str> -t <int> -f
```
```bash
alxcalc -M <int> -p <str> -ft <int> -f
```

**And Much More...**

## Notice.

> alxcalc is a work in progress, hence, all intructions seen here is only the tip of the iceberg of what the program is capable of
