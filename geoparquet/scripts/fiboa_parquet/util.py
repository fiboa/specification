import click

from yaml import safe_load as yaml_load
from .const import LOG_STATUS_COLOR

def log(text: str, status="info"):
  click.echo(click.style(text, fg=LOG_STATUS_COLOR[status]))

def load_fiboa_schema():
  with open('./core/schema/schema.yml', 'r') as f:
    return yaml_load(f)