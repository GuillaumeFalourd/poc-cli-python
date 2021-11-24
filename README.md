# poc-cli-python

POC of a CLI project using Python and [Click 8.0.x](https://click.palletsprojects.com/en/8.0.x/api/) 🐍

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

### AutoComplete

Run the following command according to the shell you're working with:

**Fish:**

```shell
eval (./auto_complete_fish.sh )
```

**Bash:**

```shell
. ./auto_complete_bash.sh
```

**Zsh:**

```shell
. ./auto_complete_zsh.sh
```

Then, the autocomplete should be activated using `<TAB> <TAB>`

![autocomplete_decorator](https://user-images.githubusercontent.com/22433243/143119442-69ca57cc-9612-4fb2-9ba0-1ae25ed364ba.gif)

## Usage

After the setup above, you'll be able to use the command by typing `os`:

```bash
➜ os
Usage: os [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  apply
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

The behaviour is the same with `os list`, `os describe` and `os apply`.

## Demo

![os_create_stack](https://user-images.githubusercontent.com/22433243/143079082-9550bb66-b580-403f-8ee4-0c8af1186926.gif)

![os_describe_stack](https://user-images.githubusercontent.com/22433243/143079102-7317a7c5-8bad-407c-9711-9896c9bed4e3.gif)

![os_apply_plugin](https://user-images.githubusercontent.com/22433243/143255418-ad915a3d-2b89-4eba-95d6-47df2f60d34e.gif)
