# Makefile to help automate key steps

.DEFAULT_GOAL := help

# A helper script to get short descriptions of each target in the Makefile
define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([\$$\(\)a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-30s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

export BOOKSHELF_NOTEBOOK_DIRECTORY = src


.PHONY: help
help:  ## print short description of each target
	@python3 -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

.PHONY: checks
checks:  ## run all the linting checks of the codebase
	@echo "=== pre-commit ==="; uvx pre-commit run --all-files || echo "--- pre-commit failed ---" >&2; \
		echo "======"

.PHONY: ruff-fixes
ruff-fixes:  ## fix the code using ruff
    # format before and after checking so that the formatted stuff is checked and
    # the fixed stuff is formatted
	uvx ruff@0.6.9 format
	uvx ruff@0.6.9 check --fix
	uvx ruff@0.6.9 format

#.PHONY: test
#test:  ## run the tests
#	uv run pytest src tests -r a -v --doctest-modules --cov=src

.PHONY: changelog-draft
changelog-draft:  ## compile a draft of the next changelog
	uvx towncrier build --draft --version $(shell uv run python scripts/get-version.py)

.PHONY: virtual-environment
virtual-environment:  ## update virtual environment, create a new one if it doesn't already exist
	uv sync
	uvx pre-commit install

run:  ## Generate the book
	uv run bookshelf run rcmip-emissions -o dist


publish:  ## publish a new release of the project
	uv run bookshelf publish rcmip-emissions
