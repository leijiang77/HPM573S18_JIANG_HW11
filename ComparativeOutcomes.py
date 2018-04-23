import ParameterClasses as P
import MarkovModel as MarkovCls
import SupportMarkovModel as SupportMarkov

# simulate no therapy
# create a cohort
cohort_none = MarkovCls.Cohort(id=0, therapy=P.Therapies.NONE)
# simulate cohort
simOutputs_none = cohort_none.simulate()

# simulate anticoagulation therapy
cohort_anticoag = MarkovCls.Cohort(id=1, therapy=P.Therapies.ANTICOAG)
simOutputs_anticoag = cohort_anticoag.simulate()

SupportMarkov.draw_survival_curves_and_histograms(simOutputs_none, simOutputs_anticoag)

SupportMarkov.print_outcomes(simOutputs_none, "No therapy")
SupportMarkov.print_outcomes(simOutputs_anticoag, "Anticoagulation theraoy")

SupportMarkov.print_comparative_outcomes(simOutputs_none, simOutputs_anticoag)

SupportMarkov.report_CEA_CBA(simOutputs_none, simOutputs_anticoag)

