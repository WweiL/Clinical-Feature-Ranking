library("table1")

descriptiveStatisticsTainan2020dataset <- function() {
    table1::table1(~factor(sex_1male_0female) + age + dose + PFS + factor(surgery) + volume + overall_survival_years + factor(chemotherapy_group) + factor(chemotherapy_yes1_no0) + diagnostic_year| death_status, data=Tainan2020dataset)
}

