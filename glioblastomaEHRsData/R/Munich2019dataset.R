library("table1")

descriptiveStatisticsMunich2019dataset <- function() {
    table1::table1(~factor(sex) + age + factor(cHsp70_level_high1_low0) + PFS + MGMT_methylation_methylated1_unmethylated0 + factor(progress_yes1_no0) + overall_survival_months | death_status, data=Munich2019dataset)
}

