# Project Daedalus

Evidence-first buyer qualification for an industrial supplier, built as an applied AI-engineering project.

An earlier automated outreach pipeline for a sheet-metal manufacturer used an LLM to score prospects and write personalised emails. The scores were confident and often wrong, and the emails read as generic. Daedalus rebuilds the process on one principle: **evidence first, then judgement, then measurement.** Every claim carries a source and a date, every decision is checked against a labelled eval set, and a person approves anything that goes out.

## Status

Stage 0 of 7: Python foundations. See [docs/adr](docs/adr) for decisions made so far.

## Layout

```
backend/            Python package, tests and config
  src/daedalus/
    core/           domain models and pure logic (strict typing)
    adapters/       LLM providers, search, fetching, storage
    pipeline/       orchestration of the steps
    cli/            command-line interface
    evals/          eval harness, metrics, reports
data/               local only, git-ignored
docs/
  adr/              architecture decision records
  labelling/        labelling rules for the eval set
  blog/             write-ups per stage
```

## Getting started

Requires [uv](https://docs.astral.sh/uv/).

```bash
cd backend
uv sync                      # installs Python 3.13 and all dependencies
uv run pytest                # tests
uv run ruff check .          # lint
uv run pyright               # type check
uv run pre-commit install    # commit hooks
```

## Licence

MIT
