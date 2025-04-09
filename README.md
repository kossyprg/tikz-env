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

### 3. Compile and export png/gif file

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

You can generate a GIF file by running `pdf2gif.py`.  
Make sure you have a PDF file in which each page corresponds to a frame of the animation.  
For an example, see [animation.tex](animation.tex).

```sh
$ make build FNAME=animation
$ python pdf2gif.py --input ./out/animation.pdf --output animation.gif --dpi 300
```

## Requirements

- Docker must be installed on your system.

## License
MIT
