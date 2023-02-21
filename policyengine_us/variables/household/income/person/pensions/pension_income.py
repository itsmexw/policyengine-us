from policyengine_us.model_api import *


class pension_income(Variable):
    value_type = float
    entity = Person
    label = "pension income"
    unit = USD
    documentation = "Income from all pensions."
    definition_period = YEAR

    adds = [
        "tax_exempt_pension_income",
        "taxable_pension_income",
    ]
