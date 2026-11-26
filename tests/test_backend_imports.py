"""Tests verifying compiled extension imports and selective build utilities in skybornbackend."""

from __future__ import annotations

import importlib

import numpy as np


def test_version_present():
    import skybornbackend

    assert skybornbackend.__version__ == "0.1.0"


def test_all_compiled_backend_extensions_importable():
    extension_modules = [
        "skybornbackend.gridfill._gridfill",
        "skybornbackend.interp.regrid",
        "skybornbackend.interp.fortran.grid2triple",
        "skybornbackend.interp.fortran.int2p_kernels",
        "skybornbackend.interp.fortran.isentropic_kernels",
        "skybornbackend.interp.fortran.rcm2points",
        "skybornbackend.interp.fortran.rcm2rgrid",
        "skybornbackend.interp.fortran.triple2grid",
        "skybornbackend.interp.fortran.vinth2p_kernels",
        "skybornbackend.calc.GPI.tropical_cyclone_potential_intensity",
        "skybornbackend.calc.cape.cape_core",
        "skybornbackend.calc.causality._causality_core",
        "skybornbackend.calc.dcape.dcape_core",
        "skybornbackend.calc.filter._lanczos_core",
        "skybornbackend.calc.geostrophic.geostrophicwind",
        "skybornbackend.calc.growth_rate.growth_rate_kernels",
        "skybornbackend.calc.mann_kendall.mann_kendall_core",
        "skybornbackend.calc.srh.srh_core",
        "skybornbackend.calc.troposphere.tropopause_height",
    ]
    for mod_name in extension_modules:
        mod = importlib.import_module(mod_name)
        assert mod is not None


def test_mann_kendall_kernel_smoke():
    from skybornbackend.calc.mann_kendall.mann_kendall_core import mk_score_var_batch

    series = np.asfortranarray(np.arange(1, 11, dtype=np.float64)[:, None])
    s_vals, var_vals = mk_score_var_batch(series, 0)
    assert float(s_vals[0]) == 45.0
    assert float(var_vals[0]) > 0.0
