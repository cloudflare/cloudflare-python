# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from ....._models import BaseModel
from ...radar_email_series import RadarEmailSeries

__all__ = ["TimeseriesGroupDKIMResponse"]


class TimeseriesGroupDKIMResponse(BaseModel):
    meta: object

    serie_0: RadarEmailSeries
