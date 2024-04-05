# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .unnamed_schema_ref_3b1a76a5e4a139b72ed7d93834773d39 import UnnamedSchemaRef3b1a76a5e4a139b72ed7d93834773d39
from .unnamed_schema_ref_eebdc868ce7f7ae92e23438caa84e7b5 import UnnamedSchemaRefEebdc868ce7f7ae92e23438caa84e7b5

__all__ = ["HealthCheck"]


class HealthCheck(BaseModel):
    direction: Optional[Literal["unidirectional", "bidirectional"]] = None
    """The direction of the flow of the healthcheck.

    Either unidirectional, where the probe comes to you via the tunnel and the
    result comes back to Cloudflare via the open Internet, or bidirectional where
    both the probe and result come and go via the tunnel. Note in the case of
    bidirecitonal healthchecks, the target field in health_check is ignored as the
    interface_address is used to send traffic into the tunnel.
    """

    enabled: Optional[bool] = None
    """Determines whether to run healthchecks for a tunnel."""

    rate: Optional[UnnamedSchemaRefEebdc868ce7f7ae92e23438caa84e7b5] = None
    """How frequent the health check is run. The default value is `mid`."""

    target: Optional[str] = None
    """The destination address in a request type health check.

    After the healthcheck is decapsulated at the customer end of the tunnel, the
    ICMP echo will be forwarded to this address. This field defaults to
    `customer_gre_endpoint address`. This field is ignored for bidirectional
    healthchecks as the interface_address (not assigned to the Cloudflare side of
    the tunnel) is used as the target.
    """

    type: Optional[UnnamedSchemaRef3b1a76a5e4a139b72ed7d93834773d39] = None
    """The type of healthcheck to run, reply or request. The default value is `reply`."""
