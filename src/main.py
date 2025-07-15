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

import os
import collections

import click
from markdown_it import MarkdownIt
from mdit_plain.renderer import RendererPlain

parser = MarkdownIt(renderer_cls=RendererPlain)


def file_stats(source: str, destination: str = "") -> None:
    """
    Get stats for a single `.md` file.
    """

    word_count: int = 0
    line_count: int = 0
    command_word: str = ""
    character_count: int = 0

    with open(source) as file:
        lines: list[str] = []

        for line in file:
            lines.append(parser.render(line))

        for line in lines:
            print(line)
            word_count = word_count + len(line.split())
            line_count = line_count + 1
            character_count = character_count + len(line)

    if destination == "":
        destination = "./output.md"

    with open(destination, "w") as output:
        output.write(
            f"Word count: {word_count}\nLine count: {line_count}\nCharacter count: {character_count}"
        )


def directory_stats(source: str, destination: str = "") -> None:
    """
    Generates stats for an entire directory of `.md` files.
    """

    total_files: int = 0
    average_word_count: int = 0
    sub_directory_count: int = 0

    word_count: int = 0
    line_count: int = 0
    character_count: int = 0
    average_word_count: int = 0

    for root, sub_paths, files in os.walk(source):
        for file in files:
            if file.endswith(".md"):
                with open(f"{root}/{file}") as buffer:
                    lines: list[str] = []

                    for line in buffer:
                        lines.append(parser.render(line))

                    for line in lines:
                        word_count = word_count + len(line.split())
                        line_count = line_count + 1
                        character_count = character_count + len(line)

                total_files = total_files + 1

    if destination == "":
        destination = "output.md"

    average_word_count = word_count / total_files

    with open(destination, "w") as output:
        output.write(
            f"Word count: {word_count}\n"
            f"Line count: {line_count}\n"
            f"Character count: {character_count}\n"
            f"Total files: {total_files}\n"
            f"Average word count: {average_word_count}"
        )


def aggregator(source: str, destination: str = "") -> None:
    """
    Pastes all content from different files into a single file.
    """

    if destination == "":
        destination = "output.md"

    with open(destination, "w") as output:
        output.write("Aggregated file, check content below:\n\n")

    for root, sub_paths, files in os.walk(source):
        for file in files:
            if file.endswith(".md"):
                with open(f"{root}/{file}") as buffer:
                    with open(destination, "a") as output:
                        for lines in buffer:
                            output.write(lines)
                        output.write("\n")
