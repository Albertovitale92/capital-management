import pandas as pd
from models.exposure import Exposure


def load_exposures(path):

    df = pd.read_csv(path)

    exposures = []

    for _, row in df.iterrows():

        exposure = Exposure(
            exposure_id=row["exposure_id"],
            carrying_value=row["carrying_value"],
            pd=row["pd"],
            lgd=row["lgd"],
            risk_weight=row["risk_weight"]
        )

        exposures.append(exposure)

    return exposures