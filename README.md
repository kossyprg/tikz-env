# Tikz-env

This repository provides a Docker-based environment for creating and compiling TikZ diagrams using LaTeX.

## Getting Started

### 1. Build the Docker image

```sh
docker build -t tikz-env .
```

### 2. Run the container

For Windows PowerShell users
```sh
docker run -it --rm -v ${PWD}:/work -w /work tikz-env bash
```

This mounts your current directory into the container so you can edit and compile `.tex` files seamlessly.

### 3. Compile and export png file

Once inside the container, you can compile your `main.tex` file.

```sh
$ make build
```

After `main.pdf` is exported in `out` directory, you can export png file.

```sh
$ make png
```

If you want to compile a TeX file other than `main.tex`, specify the filename using the `FNAME` variable:

```sh
$ make build FNAME=foo
$ make png FNAME=foo
```

## Requirements

- Docker must be installed on your system.

## License
MIT
