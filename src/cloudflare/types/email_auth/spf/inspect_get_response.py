# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["InspectGetResponse", "Error"]


class Error(BaseModel):
    """An error encountered during SPF inspection"""

    code: str
    """Error code. Known values:

    - `lookup_failed` — DNS TXT lookup failed
    - `spf_not_found` — no SPF record found
    - `invalid_spf` — record does not start with `v=spf1`
    - `invalid_domain` — PSL validation failed
    - `loop_detected` — include/redirect cycle detected
    - `invalid_mechanism` — unrecognised or malformed mechanism
    - `resource_limit_exceeded` — internal resource protection limits exceeded
      (recursion depth or query budget)
    - `max_lookups` — RFC 7208 10-lookup limit exceeded
    """

    domain: str
    """Domain where the error occurred"""

    message: str
    """Human-readable error message"""

    details: Optional[str] = None
    """Additional error-specific details (optional).

    - For `invalid_domain` errors: the invalid domain string
    - For `invalid_mechanism` errors: the invalid mechanism text (e.g.,
      "invalidmech123")
    - For `loop_detected` errors: the domain that caused the loop
    - For other error types: not present
    """


class InspectGetResponse(BaseModel):
    """Recursive SPF inspection tree"""

    components: List[object]
    """Parsed SPF components (mechanisms)"""

    domain: str
    """Domain being inspected"""

    record: str
    """Raw SPF record content"""

    total_lookups: int
    """Total number of DNS lookups performed across all includes"""

    errors: Optional[List[Error]] = None
    """
    All errors encountered during inspection, collected from the entire tree. This
    includes errors from nested includes at any depth, providing a quick overview of
    all issues without needing to traverse the nested structure. Each error includes
    a `domain` field to identify where it occurred. Empty array if no errors
    (omitted from JSON when empty).
    """
