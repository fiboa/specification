import click

from .util import log
from .validate import validate
from .create import create

@click.command()
@click.argument("command")
@click.argument("file")
def main(command, file):
  if command == "validate":
    validate(file)
  elif command == "create":
    create(file)
  else:
    log("Command not supported", "error")
    exit(1)


if __name__ == "__main__":
  main()
