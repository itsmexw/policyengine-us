from openfisca_us.model_api import *


class il_base_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "IL base income"
    unit = USD
    definition_period = YEAR
    reference = ""

    def formula(tax_unit, period, parameters):
        return (
            tax_unit("federal_agi", period)
            + tax_unit("il_base_income_additions", period)
            - tax_unit("il_base_income_subtractions", period)
        )
