import os

from xlsx_data_stream import ColumnDescription, get_xlsx_file_stream

if not os.path.exists("samples"):
    os.makedirs("samples")


chunks = get_xlsx_file_stream(
    [
        ColumnDescription(field="a"),
        ColumnDescription(field="b", number_format="0"),
        ColumnDescription(field="c", number_format="0.00"),
    ],
    [{"a": "text", "b": 1.2345, "c": 1.2345} for _ in range(1000)],
)

with open("samples/sample.xlsx", "wb") as fh:
    for chunk in chunks:
        fh.write(chunk)
