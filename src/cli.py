# Obsidian-Stats: A CLI Tool
# Copyright (C) 2025 Vishal Srivatsava AV
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https:#www.gnu.org/licenses/>.

import click

from main import file_stats, directory_stats


@click.group()
def cli():
    pass


@click.command(name="file-stat")
# @click.argument("source")
# @click.argument("destination")
@click.option("--source", help="Input file to generate stats of.", metavar="<path>")
@click.option("--destination", default="", help="Output file path", metavar="<path>")
def c_file_stat(source, destination):
    file_stats(source, destination)


@click.command(name="folder-stat")
# @click.argument("source")
# @click.argument("destination")
@click.option("--source", help="Input directory to iterate.", metavar="<path>")
@click.option(
    "--destination",
    default="",
    help="Generated stat file path",
    metavar="<path>",
)
def c_directory_stat(source, destination):
    directory_stats(source, destination)


cli.add_command(c_file_stat)
cli.add_command(c_directory_stat)

if __name__ == "__main__":
    cli()
