json-yml-pipe

json-yml-pipe is a small python script that helps you provide YML versions of
JSON files. It achieves this by creating a named pipe in the same folder as
the JSON file with a ".yml" extension, and writing the YML version to the pipe
when something reads from it.

This repository comes with a shell script to automatically setup multiple
pipes at once. You pass it a list of JSON files and it runs one copy of the
script for each file automatically. The shell script assumes that the python
script is in your PATH.

I built this tool to make it easier to write Ansible playbooks in JSON,
because I have a strong dislike for markup languages that are dependent upon
whitespace for delimiting blocks. I'm sure you'll find other uses for it
though!

This program is released into the public domain without any warranty.
