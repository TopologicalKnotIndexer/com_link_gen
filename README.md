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

Prime names are sorted by crossing number, knot/link class, alternating class, table index, and mirror flag. A depth-first multiset enumeration permits repeated prime factors and keeps every non-empty solution whose crossing sum is within the bound. Therefore one-factor prime documents are included alongside composite documents. For each solution, component counts are loaded from its PD codes. The group-combination algorithm then enumerates connected edge sets with exactly `factor_count - 1` joins, producing one deterministic link-representation document per valid tree.

The historical parameter name `max_component_cnt` limits the number of **prime factors**, not the number of link components inside those factors. Both bounds must be positive integers, and the crossing bound is currently restricted to 2 through 10.

## Input conventions

A PD code is represented as a list of four-entry crossings. Arc labels normally occur exactly twice. Public functions validate inputs and return new values rather than mutating caller-owned data unless their API explicitly says otherwise.

## External software

No external software is required. This package is implemented entirely in Python and reads data installed with the prime-link catalogue.

## Development

Python 3.10 or newer is required. Run tests with the declared catalogue, component, and combination dependencies available:

```bash
python -m unittest discover -s tests -v
```

No PyPI publication is performed as part of repository maintenance.

## License

MIT. See `LICENSE`.

## Citation

If you use this repository in academic work, please cite it as:

```bibtex
@software{topologicalknotindexer_com_link_gen,
  author = {{GGN\_2015}},
  title = {{com\_link\_gen}},
  year = {2026},
  url = {https://github.com/TopologicalKnotIndexer/com_link_gen}
}
```
