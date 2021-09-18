# Contract using latex

Generate contract using latex, with all temporary files inside /tmp and using 
[acroread](https://www.systutorials.com/docs/linux/man/1-acroread/)
to recompile, and there is a 
[makefile](https://man7.org/linux/man-pages/man1/make.1.html)
to facilitate.

[demo](tmp/main.pdf)

# Usage

```
make
```
To develop and preject be recompiled automatically

```
make once
```
To compile only once

# Dependencies 

* latexmk ([texlive-core](https://archlinux.org/packages/extra/any/texlive-core/))
* xstring ([texlive-latexextra](https://archlinux.org/packages/extra/any/texlive-latexextra/))
* [acroread](https://aur.archlinux.org/packages/acroread/)
