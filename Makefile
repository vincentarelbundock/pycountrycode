.PHONY: readme test help install

help:  ## Display this help screen
	@echo -e "\033[1mAvailable commands:\033[0m\n"
	@grep -E '^[a-z.A-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}' | sort

test: install ## run pytest suite
	uv run --all-extras pytest

readme: ## render Quarto readme
	uv run quarto render README.qmd

lint: ## run the lint checkers
	uv run --all-extras ruff check countrycode
	uv run --all-extras ruff check tests
	uv run --all-extras ruff format countrycode
	uv run --all-extras ruff format tests

install: ## install in poetry venv
	uv pip install .

coverage:
	pytest --cov=marginaleffects --cov-report=term-missing --cov-report=html tests/

build:
	uv build

publish: build
	uv publish
