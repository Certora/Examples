+--------------------------------------------------------------------------------------------------+
|         param         |         type        |       values      |           description          |
+-----------------------+---------------------+-------------------+--------------------------------+
|        row_sep        |         str         |                   |  Row separation strategy using |
|                       |                     |                   |        `----` as pattern       |
+-----------------------+---------------------+-------------------+--------------------------------+
|                       |                     |       always      |        Separate each row       |
+-----------------------+---------------------+-------------------+--------------------------------+
|                       |                     |     topbottom     |  Separate the top (header) and |
|                       |                     |                   | bottom (last row) of the table |
+-----------------------+---------------------+-------------------+--------------------------------+
|                       |                     |      markdown     | Separate only header from body |
+-----------------------+---------------------+-------------------+--------------------------------+
|                       |                     |        None       |    No row separators will be   |
|                       |                     |                   |            inserted            |
+-----------------------+---------------------+-------------------+--------------------------------+
|     padding_width     |         int         |                   |  Allocate padding to all table |
|                       |                     |                   |              cells             |
+-----------------------+---------------------+-------------------+--------------------------------+
|     padding_weight    |         str         |                   |     Strategy for allocating    |
|                       |                     |                   |   padding within table cells   |
+-----------------------+---------------------+-------------------+--------------------------------+
|                       |                     |        left       |  Aligns the cell's contents to |
|                       |                     |                   |       the end of the cell      |
+-----------------------+---------------------+-------------------+--------------------------------+
|                       |                     |       right       |  Aligns the cell's contents to |
|                       |                     |                   |    the beginning of the cell   |
+-----------------------+---------------------+-------------------+--------------------------------+
|                       |                     |     centerleft    |  Centers cell's contents with  |
|                       |                     |                   | extra padding allocated to the |
|                       |                     |                   |      beginning of the cell     |
+-----------------------+---------------------+-------------------+--------------------------------+
|                       |                     |    centerright    |  Centers cell's contents with  |
|                       |                     |                   | extra padding allocated to the |
|                       |                     |                   |         end of the cell        |
+-----------------------+---------------------+-------------------+--------------------------------+
|      padding_char     |         str         |                   |  Single character used to fill |
|                       |                     |                   |   padding with. Default is a   |
|                       |                     |                   |        blank space ` `.        |
+-----------------------+---------------------+-------------------+--------------------------------+
|      newline_char     |         str         |                   | Character appended to each row |
|                       |                     |                   | to force a newline. Default is |
|                       |                     |                   |              `\\n`             |
+-----------------------+---------------------+-------------------+--------------------------------+
|     float_rounding    |         int         |                   | Integer denoting the precision |
|                       |                     |                   | of cells of `floats` after the |
|                       |                     |                   |    decimal point. Default is   |
|                       |                     |                   |             `None`.            |
+-----------------------+---------------------+-------------------+--------------------------------+
|     emoji_spacing     |         str         |                   |  Strategy for rendering emojis |
|                       |                     |                   |    in tables. Currently only   |
|                       |                     |                   |     `mono` is supported for    |
|                       |                     |                   |  monospaced fonts. Default is  |
|                       |                     |                   |  `None` which disables special |
|                       |                     |                   |       handling of emojis.      |
+-----------------------+---------------------+-------------------+--------------------------------+
|       multiline       |    dict<Any,int>    |                   |     Renders the table with     |
|                       |                     |                   | predefined widths by passing a |
|                       |                     |                   |  `dict` with `keys` being the  |
|                       |                     |                   |  column names (e.g. equivalent |
|                       |                     |                   |  to those in the passed `data` |
|                       |                     |                   |  variable) and `values` -- the |
|                       |                     |                   |  `width` of each column as an  |
|                       |                     |                   |  integer. Note that the width  |
|                       |                     |                   |  of a column cannot be smaller |
|                       |                     |                   |   than the longest contiguous  |
|                       |                     |                   |   string present in the data.  |
+-----------------------+---------------------+-------------------+--------------------------------+
|   multiline_strategy  |         str         |                   |  Strategy applied to rendering |
|                       |                     |                   |   contents in multiple lines.  |
|                       |                     |                   |   Possible values are `rows`,  |
|                       |                     |                   | `header` or `rows_and_header`. |
|                       |                     |                   |  The default value is `rows`.  |
+-----------------------+---------------------+-------------------+--------------------------------+
|                       |                     |        rows       |  Splits only rows overfilling  |
|                       |                     |                   | by the predefined column width |
|                       |                     |                   | as provided in the `multiline` |
|                       |                     |                   |            variable            |
+-----------------------+---------------------+-------------------+--------------------------------+
|                       |                     |       header      |     Splits only the header     |
|                       |                     |                   |  overfilling by the predefined |
|                       |                     |                   |   column width as provided in  |
|                       |                     |                   |    the `multiline` variable    |
+-----------------------+---------------------+-------------------+--------------------------------+
|                       |                     |  rows_and_header  |     Splits rows and header     |
|                       |                     |                   |  overfilling by the predefined |
|                       |                     |                   |   column width as provided in  |
|                       |                     |                   |    the `multiline` variable    |
+-----------------------+---------------------+-------------------+--------------------------------+
|  multiline_delimiter  |         str         |                   | Character that will be used to |
|                       |                     |                   |  split a cell's contents into  |
|                       |                     |                   |   multiple rows. The default   |
|                       |                     |                   |   value is a blank space ` `.  |
+-----------------------+---------------------+-------------------+--------------------------------+
|         quote         |         bool        |                   |  Wraps the generated markdown  |
|                       |                     |                   |      table in block quotes     |
|                       |                     |                   |     ```table```. Default is    |
|                       |                     |                   |             `True`.            |
+--------------------------------------------------------------------------------------------------+

