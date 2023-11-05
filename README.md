# alxcalc.

`alxcalc` is a tool that enables `ALX learners` to predict/calculate their expected avarage score for a particular month, project, or task, based on the learners' computation/input.

## Installation.

```bash
git clone https://github.com/juniorohanyere/alxcalc.git
```

## Usage.

**Getting Started:**

```bash
./alxcalc   # brief introduction + developer's name + version number
```
```bash
./alxcalc -h    # display help message (man page)
```
```bash
./alxcalc -v    # display version number
```

**Global Operations:**

*Specify -r, -f or combination of both at the end of the line to perform global operations.*

```bash
./alxcalc -r    # reset values in input file to empty
```
```bash
./alxcalc -f    # warn for detected empty values, empty is different from a zero value
```
```bash
./alxcalc -m <int> -p <str> -t <int> -rf
```

**Month:**

```bash
./alxcalc -M <int>  # open editor for the given month
```
```bash
./alxcalc -m <int>  # display result for the given month
```
```bash
./alxcalc -fm <int> # don't skip empty values, treat as warning (--)
                    # without the -f flag, empty value is treated as zero
```
```bash
./alxcalc -rfm <int> # reset and don't skip empty values
```

**Project:**

```bash
./alxcalc -M <int> -p <str>
```
```bash
./alxcalc -m <int> -rfp <str>
```

**Task:**

```bash
./alxcalc -m <int> -fp <str> -rt <int>
```
```bash
./alxcalc -M <int> -p <str> -t <int> -f
```
```bash
./alxcalc -M <int> -p <str> -ft <int> -f
```

**And Much More...**

## Notice.

> alxcalc is a work in progress, hence, any intructions given here is only the tip of the iceberg of what the program is capable of
