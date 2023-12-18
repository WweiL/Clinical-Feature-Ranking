## code to prepare `glioblastomaEHRsData` dataset goes here

Munich2019dataset = readr::read_csv("data-raw/Munich2019dataset.csv")
usethis::use_data(Munich2019dataset, overwrite=TRUE)

Tainan2020dataset = readr::read_csv("data-raw/Tainan2020dataset.csv")
usethis::use_data(Tainan2020dataset, overwrite=TRUE)

Utrecht2019dataset = readr::read_csv("data-raw/Utrecht2019dataset.csv")
usethis::use_data(Utrecht2019dataset, overwrite=TRUE)

# usethis::use_data(glioblastomaEHRsData, overwrite = TRUE)


