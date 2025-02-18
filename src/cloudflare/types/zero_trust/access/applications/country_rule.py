# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ....._models import BaseModel

__all__ = ["CountryRule", "Geo"]


class Geo(BaseModel):
    country_code: str
    """The country code that should be matched."""


class CountryRule(BaseModel):
    geo: Geo
