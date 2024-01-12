# Load and descriptions of open, de-identified electronic health records (EHRs) of patients with glioblastoma

## Execution
1. go to folder `/glioblastomaEHRsData`
2. open R console by typing `R`
3. in the console, type 
```
list.of.packages <- c("pacman")
new.packages <- list.of.packages[!(list.of.packages %in%
installed.packages()[,"Package"])]
if(length(new.packages)) install.packages(new.packages)

library("pacman")
pacman::p_load("usethis", "devtools", "roxygen2", "devtools")
devtools::load_all()
```
4. call one of `descriptiveStatisticsUtrecht2019dataset()`, `descriptiveStatisticsMunich2019dataset()`, `descriptiveStatisticsTainan2020dataset()`
5. New webpage should open up, if not, try running the commands in data-raw/DATASET.R in the console

## Article
More information about this study can be found in the following peer-reviewed article:

> Gabriel Cerono, Ombretta Melaiu, and Davide Chicco, ["Clinical feature ranking based on ensemble machine learning reveals top survival factors for glioblastoma multiforme"](https://urldefense.com/v3/__https://doi.org/10.1007/s41666-023-00138-1__;!!DZ3fjg!7sUFgO4nj8ss_co08kEiIJ8bPEAUSimDg6B-al0-BHEwR6zmG0L7rB5DKIH2eNoZMrFpxUs9FH7nEkMPdWYHV__x$ ), Journal of Healthcare Informatics Research, 2023

## Contact
For questions on this repository, please contact Wei Liu at weil8(AT)illinois.ed
For questions or enquires, please contact [Davide Chicco](https://urldefense.com/v3/__https://www.davidechicco.it__;!!DZ3fjg!7sUFgO4nj8ss_co08kEiIJ8bPEAUSimDg6B-al0-BHEwR6zmG0L7rB5DKIH2eNoZMrFpxUs9FH7nEkMPdfKlCz_T$ ) at davidechicco(AT)davidechicco.it
