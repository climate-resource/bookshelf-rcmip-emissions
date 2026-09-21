# %% [markdown]
# # RCMIP Emissions
#
# Emissions of greenhouse gases and air pollutants from RCMIP,
# for use in climate models.
#
# The recipe in `bookshelf.yaml` names the version, the licence, the discovery metadata
# and the inputs.
#
# This file contains the code that processes the data into a form used by the bookshelf.

# %%
import bookshelf
import scmdata

# %%
build = bookshelf.setup()

# %% [markdown]
# # Fetch
#
# `build.use` resolves a resource named in the recipe,
# and registers them as an input of this build.

# %%
raw = build.use("raw")
rcmip_emissions = scmdata.ScmRun(str(raw.path), lowercase_cols=True)
rcmip_emissions

# %% [markdown]
# # Process
#
# The complete protocol goes out as it arrives.
# A second resource carries only the variables MAGICC is driven by.

# %%
rcmip_emissions.get_unique_meta("variable")

# %%
magicc_emissions = rcmip_emissions.filter(
    variable=[
        "Emissions|BC",
        "Emissions|CH4",
        "Emissions|CO",
        "Emissions|CO2",
        "Emissions|CO2|MAGICC AFOLU",
        "Emissions|CO2|MAGICC Fossil and Industrial",
        "Emissions|F-Gases|*",
        "Emissions|Montreal Gases|*",
        "Emissions|N2O",
        "Emissions|NH3",
        "Emissions|NOx",
        "Emissions|OC",
        "Emissions|Sulfur",
        "Emissions|VOC",
    ]
)

# %%
magicc_emissions.meta[["variable", "unit"]].drop_duplicates()

# %% [markdown]
# # Publish
#
# A timeseries is stored wide, one column per year,
# which is the shape `ScmRun.timeseries` already returns.

# %%
build.book.write(
    "complete",
    rcmip_emissions.timeseries().reset_index(),
    type="timeseries",
    used=[raw],
)
build.book.write(
    "magicc",
    magicc_emissions.timeseries().reset_index(),
    type="timeseries",
    used=[raw],
)
build.book.publish()
