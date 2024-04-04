# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from ...._models import BaseModel
from ...unnamed_schema_ref_c5858f1f916a921846e0b6159af470a7 import UnnamedSchemaRefC5858f1f916a921846e0b6159af470a7

__all__ = ["RouteStatsResponse", "Stats"]


class Stats(BaseModel):
    distinct_origins: int

    distinct_origins_ipv4: int

    distinct_origins_ipv6: int

    distinct_prefixes: int

    distinct_prefixes_ipv4: int

    distinct_prefixes_ipv6: int

    routes_invalid: int

    routes_invalid_ipv4: int

    routes_invalid_ipv6: int

    routes_total: int

    routes_total_ipv4: int

    routes_total_ipv6: int

    routes_unknown: int

    routes_unknown_ipv4: int

    routes_unknown_ipv6: int

    routes_valid: int

    routes_valid_ipv4: int

    routes_valid_ipv6: int


class RouteStatsResponse(BaseModel):
    meta: UnnamedSchemaRefC5858f1f916a921846e0b6159af470a7

    stats: Stats
