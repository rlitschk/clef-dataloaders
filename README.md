# CLEF dataloader
## Setup
- Download and unzip [The CLEF Test Suite for the CLEF 2000-2003 Campaigns – Evaluation Package](https://catalogue.elra.info/en-us/repository/browse/ELRA-E0008/).
- Set environment variable `CLEF_HOME` to point to the location of the unzipped dataset.
- *(Optional)* Download and unzip Swahili (SW) and Somali (SO) CLEF queries [here](https://ciir.cs.umass.edu/ictir19_simulate_low_resource).
- *(Optional)* Set `CLEF_LOWRES_DIR` in `clef_paths.py` to where you unzipped the dataset.

Dataloaders expect the following structure after downloading and unzipping CLEF:
```bash
clef/
├── clef-low-resource
│         └── long_paper
├── DocumentData
│         ├── dutch
│         ├── english
│         ├── finnish
│         ├── french
│         ├── german
│         ├── italian
│         └── russian
├── RelAssess
│         ├── 2001
│         ├── 2002
│         └── 2003
└── Topics
    ├── 2001
    ├── 2002
    └── 2003
```

## References

```bibtex
@inproceedings{Bonab2019swahiliclef,
    author = {Bonab, Hamed and Allan, James and Sitaraman, Ramesh},
    title = {Simulating CLIR Translation Resource Scarcity Using High-Resource Languages},
    year = {2019},
    url = {https://doi.org/10.1145/3341981.3344236},
    booktitle = {Proceedings of ICTIR},
    pages = {129–136},
}
```
```bibtex
@inproceedings{braschler2003clef,
    title={{CLEF 2003--Overview of results},
    author={Braschler, Martin},
    booktitle={Workshop of the Cross-Language Evaluation Forum for European Languages},
    pages={44--63},
    year={2003},
    organization={Springer}
}
```
