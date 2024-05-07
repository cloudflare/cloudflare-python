# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

__all__ = ["SteeringPolicy"]

SteeringPolicy = Literal[
    "off", "geo", "random", "dynamic_latency", "proximity", "least_outstanding_requests", "least_connections", '""'
]
