# Chapter 2 — Components, Ports, PCells & Mini-PDK

This chapter develops a reusable silicon-photonics component library using GDSFactory.

## Reusable Components

### pdk_straight

Usage:

```python
pdk_straight(length=20, width=0.5)
```

Parameters:

- `length`: waveguide length in µm
- `width`: waveguide width in µm

Ports:

- `o1`: input
- `o2`: output

### taper_nima

Usage:

```python
taper_nima(
    width1=0.45,
    width2=1.0,
    length1=10,
    length2=20,
    taper_length=15,
)
```

Parameters:

- `width1`: input waveguide width
- `width2`: output waveguide width
- `length1`: input straight-waveguide length
- `length2`: output straight-waveguide length
- `taper_length`: taper transition length

Ports:

- `A_in`: input-side port
- `A_out`: output-side port

### custom_coupler

Usage:

```python
custom_coupler(
    length=20,
    gap=0.2,
)
```

Parameters:

- `length`: directional-coupler interaction length
- `gap`: gap between the two waveguides

Ports:

- `o1`
- `o2`
- `o3`
- `o4`

## Mini-PDK

The project mini-PDK contains:

- `pdk/layers.py` — layer definitions
- `pdk/cross_sections.py` — waveguide cross-section definitions
- `pdk/components.py` — PDK-aware component generators

Technology flow:

```text
Layer definition
      ↓
Cross-section
      ↓
PCell
      ↓
GDSFactory Component
      ↓
GDS / OASIS
```

Example:

```text
WG = (1, 0)
      ↓
strip_xs(width=0.5)
      ↓
pdk_straight(length=20, width=0.5)
      ↓
waveguide component
```

## Automated Tests

Tests are located in:

```text
tests/test_components.py
```

Run them with:

```bash
python -m pytest tests/test_components.py -q
```

Current tests check:

- expected port count
- expected port names
- invalid dimensions
- deterministic cell naming
- correct waveguide layer
- taper interface
- directional-coupler interface

## Component Gallery

The Chapter 2 component gallery contains examples of:

- straight waveguide
- Euler bend
- taper
- MMI
- directional coupler
- routed waveguide section

The gallery can be inspected in KLayout.

## Layout Export

The project supports:

- GDSII (`.gds`)
- OASIS (`.oas`)

Both formats can be opened and inspected in KLayout.

## Chapter 2 Main Concepts

This chapter covered:

- optical port semantics
- component references
- translation, rotation and mirroring
- cross-sections
- tapers
- MMIs and splitters
- directional couplers
- parameter sweeps
- reusable `@gf.cell` PCells
- input-parameter validation
- deterministic cell naming
- component modules
- mini-PDK structure
- automated testing with pytest
- GDSII and OASIS export
