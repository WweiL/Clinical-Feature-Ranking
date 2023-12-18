## How to visualize the tables
1. go to folder `/glioblastomaEHRsData`
2. open R console by typing `R`
3. in the console, type 
```
install.packages(c("usethis", "devtools", "roxygen2"))
library(devtools)
devtools::load_all()
```
4. call one of `descriptiveStatisticsUtrecht2019dataset()`, `descriptiveStatisticsMunich2019dataset()`, `descriptiveStatisticsTainan2020dataset()`
5. New webpage should open up, if not, try running the commands in data-raw/DATASET.R in the console