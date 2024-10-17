# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ...._models import BaseModel

__all__ = ["FallthroughCreateResponse"]


class FallthroughCreateResponse(BaseModel):
    expression: str
    """WAF Expression for fallthrough"""

    title: str
    """Title for the expression"""
