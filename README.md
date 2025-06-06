# xlsx_data_stream

A lightweight Python library for efficiently generating Excel files from large
datasets or async data streams. Designed for:

- low memory usage (streams data row-by-row);
- sync and async support;
- dynamic formatting (per-column number formats, additional sheets, e.t.c).

Refer to the `tests/` and `get_xlsx_file_stream`/`get_xlsx_file_stream_async`
docstrings for usage examples and details about the API. Proper documentation
currently lacks, so you might need to read the code.

## Installation

Using pip:

```bash
pip install xlsx_data_stream
```

Using poetry:

```bash
poetry add xlsx_data_stream
```

## Usage

### Synchronous interface

```py
from xlsx_data_stream import ColumnDescription, get_xlsx_file_stream


chunks = get_xlsx_file_stream(
    [
        ColumnDescription(field="a"),
        ColumnDescription(field="b", number_format="0"),
        ColumnDescription(field="c", number_format="0.00"),
    ],
    [
        {"a": "text", "b": 1.2345, "c": 1.2345}
        for _ in range(1000)
    ],
)

with open("output.xlsx", "wb") as fh:
    for chunk in chunks:
        fh.write(chunk)
```

### Asynchronous interface

```py
import asyncio

from xlsx_data_stream import ColumnDescription, get_xlsx_file_stream_async


async def data():
    for _ in range(1000):
        yield {"a": "text", "b": 1.2345, "c": 1.2345}


async def main():
    chunks = get_xlsx_file_stream_async(
        [
            ColumnDescription(field="a"),
            ColumnDescription(field="b", number_format="0"),
            ColumnDescription(field="c", number_format="0.00"),
        ],
        data(),
    )

    with open("output.xlsx", "wb") as fh:
        async for chunk in chunks:
            fh.write(chunk)


asyncio.run(main())
```

### `convert_cell_value_to_excel_string`

```py
from datetime import datetime, timezone

from xlsx_data_stream import convert_cell_value_to_excel_string

assert convert_cell_value_to_excel_string(10, timezone.utc) == '10'

assert convert_cell_value_to_excel_string(None, timezone.utc) == ''

assert convert_cell_value_to_excel_string(
    datetime(2020, 1, 1, 10, tzinfo=timezone.utc),
    timezone.utc,
) == '43831.416666666664'
```

## Mentions

- This project is heavely based on [Polyconseil/xlsx_streaming](https://github.com/Polyconseil/xlsx_streaming).

## License

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fmichaelkryukov%2Fxlsx-data-stream.svg?type=large&issueType=license)](https://app.fossa.com/projects/git%2Bgithub.com%2Fmichaelkryukov%2Fxlsx-data-stream?ref=badge_large&issueType=license)
