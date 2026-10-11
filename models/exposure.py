import pandas as pd
import numpy as np
class Exposure:
    def __init__(self, exposure_id, exposure_type, carrying_value, pd, lgd, maturity, risk_weight, interest_rate, maturity_date, product_type):
        self.exposure_id = exposure_id
        self.exposure_type = exposure_type
        self.carrying_value = carrying_value
        self.pd = pd
        self.lgd = lgd
        self.maturity = maturity
        self.risk_weight = risk_weight
        self.interest_rate = interest_rate
        self.maturity_date = maturity_date
        self.product_type = product_type

    @property
    def ead(self):
        """
        Return EAD in terms of carrying value, with already the structure to make it more complex and
        product-based formula in the future
        """
        if self.product_type == "Credit Line":
            return self.drawn_amount + 0.5*self.undrawn_amount

        return self.carrying_value

    @property
    def get_credit_loss(self):
        """
        Calculate the expected credit loss for the exposure.
        ECL = EAD * PD * LGD
        """
        return self.ead * self.pd * self.lgd

    @property
    def get_credit_rwa_std(self):
        """
        Calculate the risk-weighted assets for the exposure.
        RWA = Carrying Value * Risk Weight
        """
        return self.ead * self.risk_weight

    @property
    def get_credit_rwa_std(self):
        """
        Calculate the credit risk-weighted assets for the exposure.
        RWA credit = EAD * Risk Weight
        """
        return self.ead * self.risk_weight

    @property
    def rwa_std(self):
        """
        Calculate the risk-weighted assets for the exposure.
        RWA = Credit RWA + Market RWA + CVA RWA
        """
        credit_rwa = self.get_credit_rwa_std()
        #market_rwa = self.get_market_rwa_std()
        #cva_rwa = self.get_cva_rwa_std()

        return credit_rwa #+ market_rwa + cva_rwa

    @property
    def capital_requirement_std(self):
        """
        Calculate the capital as 8% or RWA
        """
        return 0.08 * self.rwa_std() #+ market_rwa + cva_rwa

    