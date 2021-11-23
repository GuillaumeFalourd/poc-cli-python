# poc-cli-python

POC of a CLI project using Python 🐍

## Setup

At the repository root, run:

First:

```bash
python3 -m venv env
```

Then:

```bash
source env/bin/activate
```

Finally:

```bash
python3 -m pip install --editable .
```

## Usage

After the setup above, you'll be able to use the command by typing `os`:

```bash
➜ os
Usage: os [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  create
  describe
  list
```

Each command has a subcommand stack and template such as `os create`:

```bash
➜ os create
Usage: os create [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  stack
  template
  ```

The behaviour is the same with `os list` and `os describe`.

## Demo

