# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DurableObjectBinding"]


class DurableObjectBinding(BaseModel):
    class_name: str
    """The exported class name of the Durable Object"""

    name: str
    """A JavaScript variable name for the binding."""

    type: Literal["durable_object_namespace"]
    """The class of resource that the binding provides."""

    environment: Optional[str] = None
    """The environment of the script_name to bind to"""

    namespace_id: Optional[str] = None
    """Namespace identifier tag."""

    script_name: Optional[str] = None
    """
    The script where the Durable Object is defined, if it is external to this Worker
    """
