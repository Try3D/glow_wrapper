# Glow_wrapper
A python library which is a wrapper for glow, the markdown render for the CLI

## Setup
- Ensure that you have the following installed
    - python
    - go
    - git
- Clone the repository to your hard drive

    $ `git clone https://github.com/Try3D/glow_wrapper`
- Change into the clone'd directory

    $ `cd glow_wrapper`
- Install the glow binary

    $ `python setup.py`
This will build the go binary and place it in `glow/glow`

## Example usage

```python
from glow_wrapper import GlowWrapper

glow_wrapper = GlowWrapper()

rendered_output = glow_wrapper.render_markdown('example.md')
print(rendered_output)
```

