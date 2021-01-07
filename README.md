# hexeditlyylli
A text user interface-based [hex editor](https://en.wikipedia.org/wiki/Hex_editor).

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FHaydenBobMutthew%2Fhexeditlyylli%2F&count_bg=%233961FF&title_bg=%23555555&icon=github.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://github.com/HaydenBobMutthew/hexeditlyylli)

## Documentation

### Requirments
- Python 3.9 or up

### How to launch the program
Run `__main__.py -f <filename> -l <number of lines> -b <bytes per line>` to view and edit hex data of a file.
`-l` and `-b` can be omitted and defaults to 16.

![How it look safter a successful launch](/images/view.png)

### Option command arguments

#### File editing commands
After printing a page, it is prompted to input option command.

*data* can be a string (enclosed with `'` or `"`) or a hexadecimal string.

- `write <start> <data>`
  - Write *data* starting from position *start* in bytes.
  ![Write Data](/images/write.png)
- `append <data>`
  - Append *data* at the end of file.
- `trunc <size>` or `truncate <size>`
  - Truncate the file to at most *size* bytes.
- `inspect view <endian> <pos>`
  - Inspect and edit data from position *pos* in bytes with *endian* endianness. *endian* can only be `big` or `little`.
  ![Inspect Data](/images/inspect_view.png)
- `inspect edit <endian> <pos> <dtype> <data>`
  - Write *data* of data type *dtype* starting from position *pos* with *endian* endianness.
- `goto <pos>`
  - Go to the page that position *pos* located.
- `prev`
  - Back to the previous page.
- `next` or with no command input
  - Go to the next page.
- `help`
  - Get help of option commands.
