# cli-obsidian-tools

I've recently gone berserk and extremely obsessed with Obsidian, and I love data.

This cli-tool creates `.md` files of statistics from your vault and I've planned to make it more useful by adding stuff that helps me.

For now it does basic file stats such as:
- word, line, and character count per file
- the above but for an entire directory
- aggregates content from various files into a single one

More would be added as I get time.

I didn't create this as an Obsidian Plugin cause I was too lazy to learn JS / TS.

# Setup
Run the following commands:
```shell
$ py -m venv env
$ pip install -r requirements
```

# Usage

> [!NOTE]
Run the programme in a virtual environment, global package has yet to be released / done.

So far only two commands are present:
```shell
$ cli.py aggregator --help
$ cli.py file-stat --help
$ cli.py folder-stat --help
```

Documentation will be done for this soon. Until then, enjoy figuring it out.

# Licensing
Please adhere to GPLv3 license utilised here.