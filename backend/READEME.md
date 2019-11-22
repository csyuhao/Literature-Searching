# Introduction

This floder is the search engine implementation. 

## Structure

The file strcuture of `crawlerpy`, `storage.py` and `search.py`. 

`crawler.py` is used to download article records from [arxiv.org](https://www.arxiv.org). Every record contains `id`, `updated`, `published`, `title`, `summary`, `affiliation`, `doi`, `link`, `comment`, `journal_ref`, `primary_category`, `category` and `authors`. `authors` is a list of authors.
The example is following:
```
    {
        "id": "http://arxiv.org/abs/cond-mat/0102536v1",
        "updated": "2001-02-28T20:12:09Z",
        "published": "2001-02-28T20:12:09Z",
        "title": "Impact of Electron-Electron Cusp on Configuration Interaction Energies",
        "summary": "  The effect of the electron-electron cusp on the convergence of configuration\ninteraction (CI) wave functions is examined. By analogy with the\npseudopotential approach for electron-ion interactions, an effective\nelectron-electron interaction is developed which closely reproduces the\nscattering of the Coulomb interaction but is smooth and finite at zero\nelectron-electron separation. The exact many-electron wave function for this\nsmooth effective interaction has no cusp at zero electron-electron separation.\nWe perform CI and quantum Monte Carlo calculations for He and Be atoms, both\nwith the Coulomb electron-electron interaction and with the smooth effective\nelectron-electron interaction. We find that convergence of the CI expansion of\nthe wave function for the smooth electron-electron interaction is not\nsignificantly improved compared with that for the divergent Coulomb interaction\nfor energy differences on the order of 1 mHartree. This shows that, contrary to\npopular belief, description of the electron-electron cusp is not a limiting\nfactor, to within chemical accuracy, for CI calculations.\n",
        "affiliation": "NMRC, University College, Cork, Ireland",
        "doi": "10.1063/1.1383585",
        "link": null,
        "comment": "11 pages, 6 figures, 3 tables, LaTeX209, submitted to The Journal of\n  Chemical Physics",
        "journal_ref": "J. Chem. Phys. 115, 1626 (2001)",
        "primary_category": null,
        "category": null,
        "authors": [
            {
                "name": "David Prendergast",
                "affiliation": "Department of Physics"
            },
            {
                "name": "M. Nolan",
                "affiliation": "NMRC, University College, Cork, Ireland"
            },
            {
                "name": "Claudia Filippi",
                "affiliation": "Department of Physics"
            },
            {
                "name": "Stephen Fahy",
                "affiliation": "Department of Physics"
            },
            {
                "name": "J. C. Greer",
                "affiliation": "NMRC, University College, Cork, Ireland"
            }
        ]
    }
```

`storage.py` is used to store these records to Elasticsearch.

`search.py` is used to search records from elasticsearch.