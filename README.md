# hexeditlyylli
A text user interface-based [hex editor](https://en.wikipedia.org/wiki/Hex_editor) written in Python. Support big files!

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FHaydenBobMutthew%2Fhexeditlyylli%2F&count_bg=%233961FF&title_bg=%23555555&icon=github.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://github.com/HaydenBobMutthew/hexeditlyylli) [![GitHub license](https://img.shields.io/github/license/HaydenBobMutthew/hexeditlyylli?logo=github)](https://github.com/HaydenBobMutthew/hexeditlyylli/blob/main/LICENSE) [![GitHub all releases](https://img.shields.io/github/downloads/HaydenBobMutthew/hexeditlyylli/total?logo=github)](https://github.com/HaydenBobMutthew/hexeditlyylli/releases) [![GitHub latest release](https://img.shields.io/github/downloads/HaydenBobMutthew/hexeditlyylli/v0.9.1/total?label=downloads%40v0.9.1&logo=github)](https://github.com/HaydenBobMutthew/hexeditlyylli/releases)

## Documentation

### Requirments
- Python 3.9 or up
- [Colorama](https://pypi.org/project/colorama/)

### How to launch the program
Run `python __main__.py -f <filename> -l <number of lines> -b <bytes per line>` to view and edit hex data of a file.
`-l` and `-b` can be omitted and defaults to 16.

![How it looks after a successful launch](/images/view.png)

### Option command arguments
After printing a page, it is prompted to input option command.

*data* can be a string (enclosed with `'` or `"`) or a hexadecimal string.
*endian* can only be `big` or `little`.
*start* and *end* are inputted as a hexadecimal number.

#### File editing commands
- `write <start> <data>`
  - Overwrite *data* starting from position *start* in bytes.
  ![Write Data](/images/write.png)
- `append <data>`
  - Append *data* at the end of file.
- `insert <start> <data>`
  - Insert *data* starting from one byte before position *start*.
- `remove <start> <end>`
  - Remove data from position *start* to *end*.
- `trunc <size>` or `truncate <size>`
  - Truncate the file to at most *size* bytes.
- `inspect write <endian> <pos> <dtype> <data>`
  - Overwrite *data* of data type *dtype* starting from position *pos* with *endian* endianness.
- `inspect append <endian> <pos> <dtype> <data>`
  - Append *data* of data type *dtype* at the end of file with *endian* endianness.
- `inspect insert <endian> <pos> <dtype> <data>`
  - Insert *data* of data type *dtype* starting from one byte before position *start* with *endian* endianness.

#### Data inspection commands
- `inspect view <endian> <pos>`
  - Inspect data from position *pos* in bytes with *endian* endianness.
  ![Inspect Data](/images/inspect_view.png)
  
#### Navigation commands
- `goto <pos>`
  - Go to the page that position *pos* is located.
- `prev [pages]`
  - Go back `pages` page(s). If `pages` is not specified, `pages` defaults to 1. Go to the beginning of file if going back the pages specified will exceed the first page.
- `next [pages]`
  - Go next `pages` page(s). If `pages` is not specified, `pages` defaults to 1.
- No option input
  - Go to the next page. Terminates the program if the current page is the last page.

#### Miscellaneous commands
- `help`
  - Get help of option commands. (Work in progress feature)
- `fileinfo`
  - Get the file info. (Work in progress feature, only file size is printed)