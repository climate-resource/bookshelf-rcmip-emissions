# RCMIP Emissions

The RCMIP emissions dataset is a dataset of emissions of greenhouse gases and air pollutants
for use in climate models.
This repository contains the code to generate the RCMIP emissions book for the [bookshelf](https://github.com/climate-resource/bookshelf).

## Getting started

Install the local virtual environment:

```bash
   make virtual-environment
```

The configuration that describes the book is in `src/rcmip-emissions.yaml`
while the source code to process the book is in `src/rcmip-emissions.py`.


The book can be generated using `make run`,
which produces some outputs which are stored in `dist/`.
This includes the generated CSV files and the rendered notebook
that was used to generate the book.

These build artifacts can then be published to the bookshelf using `make publish`
(not currently working).
Generally this is done automatically by the CI/CD pipeline on a new release.
