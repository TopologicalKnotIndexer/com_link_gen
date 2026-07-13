# com-link-gen-10

Enumerate textual representations of composite links built from prime knots and links with at most ten crossings.

## Installation

```bash
pip install com-link-gen-10
```

## Usage example

```python
from com_link_gen_10 import com_link_gen

representations = com_link_gen(total_crs=5, max_component_cnt=2)
print(len(representations))  # 33
print(representations[0])
```

## Algorithm

Prime names are sorted by crossing number, knot/link class, alternating class, table index, and mirror flag. A depth-first multiset enumeration permits repeated prime factors and keeps every non-empty solution whose crossing sum is within the bound. For each solution, component counts are loaded from its PD codes. The group-combination algorithm then enumerates connected edge sets with exactly `factor_count - 1` joins, producing one deterministic link-representation document per valid tree.

## Input conventions

A PD code is represented as a list of four-entry crossings. Arc labels normally occur exactly twice. Public functions validate inputs and return new values rather than mutating caller-owned data unless their API explicitly says otherwise.

## External software

No external software is required. This package is implemented entirely in Python and reads data installed with the prime-link catalogue.

## Development

Run examples and package checks before release. Python packages require Python 3.10 or newer. Build PyPI artifacts with:

```bash
poetry check
poetry build
```

## License

MIT. See `LICENSE`.
