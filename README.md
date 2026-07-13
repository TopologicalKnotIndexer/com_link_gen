# com-link-gen-10

Generate composite-link descriptions from the bundled prime-link catalogue.

## Installation

```bash
pip install com-link-gen
```

## Quick start

`from com_link_gen_10 import com_link_gen` then `com_link_gen(10, 3)`.

PD codes are lists of four-entry crossings. Each arc label must occur exactly twice. Functions validate their inputs and do not mutate caller-owned PD-code lists unless explicitly documented.

## Development

Use Python 3.10 or newer for Python packages. Build distributions with `poetry build`. Run the package's tests or examples before publishing. C++ projects require a modern standards-compliant compiler.

## License

MIT. See `LICENSE`.
