# skyborn-backend (`skybornbackend`)

Prebuilt Fortran, C, and Cython numerical computation kernels powering the [**Skyborn**](https://github.com/skyborn-org/Skyborn) atmospheric and climate science ecosystem.

Part of the [**Skyborn** (`skyborn-org`)](https://github.com/skyborn-org) organization.

## Included Compiled Modules

- `skybornbackend.gridfill`: Poisson spherical/rectangular gap-filling (`_gridfill`).
- `skybornbackend.interp`: Vertical hybrid/pressure/isentropic interpolation, horizontal bilinear/conserving regridding, and curvilinear-to-rectilinear kernels.
- `skybornbackend.calc`:
  - `GPI`: Potential intensity kernels (`tropical_cyclone_potential_intensity`)
  - `cape` & `dcape`: Convective and downdraft CAPE kernels
  - `causality`: Batch Liang–Kleeman information flow & AR(1) kernels
  - `filter`: Lanczos filtering Fortran kernels
  - `geostrophic`: Geostrophic wind solver (`geostrophicwind`)
  - `growth_rate`: Eady baroclinic & barotropic growth rate kernels
  - `mann_kendall`: Vectorized multidimensional Mann–Kendall & Theil–Sen kernels
  - `srh`: Storm-relative helicity kernels
  - `troposphere`: WMO tropopause height kernels

## Installation

Most users should install the high-level library instead, which pulls this package automatically:

```bash
pip install skyborn
```

## Developer Incremental Build Tips

```bash
# First inplace build compiles all 12 Meson modules:
python setup.py build_ext --inplace

# Subsequent edits reuse Ninja caches; optionally target a single module:
SKYBORN_BUILD_ONLY=calc.mann_kendall python setup.py build_ext --inplace
```

## License

BSD 3-Clause License. See [LICENSE](LICENSE).
