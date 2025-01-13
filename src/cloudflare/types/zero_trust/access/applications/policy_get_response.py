# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..application_policy import ApplicationPolicy

__all__ = ["PolicyGetResponse"]


class PolicyGetResponse(ApplicationPolicy):
    precedence: Optional[int] = None
    """The order of execution for this policy.

    Must be unique for each policy within an app.
    """
