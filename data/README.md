# data/

Everything in this folder except this README is git-ignored. Real data never leaves the machine.

Layout:

- `raw/`: inputs exactly as received (intake export, campaign CSVs). Never edited.
- `labels/`: hand labels for the eval set (Stage 2).
- `snapshots/`: frozen fetched pages (Stage 3).
- `daedalus.sqlite`: the local database (Stage 1 onward).

Published examples use synthetic or anonymised rows only.
