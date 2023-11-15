library("table1")

descriptiveStatisticsUtrecht2019dataset <- function() {
    table1::table1(~age + factor(adjuvant_treatment) + factor(biopsy_debulking) + factor(KPS) + factor(SVZ_status) + survival_days_from_surgery | death_status, data=Utrecht2019dataset)
}
