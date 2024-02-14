# File generated from our OpenAPI spec by Stainless.

from . import types
from ._version import __version__, __title__
from ._client import (
    Timeout,
    Transport,
    RequestOptions,
    Client,
    AsyncClient,
    Stream,
    AsyncStream,
    Cloudflare,
    AsyncCloudflare,
)
from ._exceptions import (
    CloudflareError,
    APIError,
    APIStatusError,
    APITimeoutError,
    APIConnectionError,
    APIResponseValidationError,
    BadRequestError,
    AuthenticationError,
    PermissionDeniedError,
    NotFoundError,
    ConflictError,
    UnprocessableEntityError,
    RateLimitError,
    InternalServerError,
)
from ._types import NoneType, Transport, ProxiesTypes
from ._utils import file_from_path
from ._models import BaseModel
from ._utils._logs import setup_logging as _setup_logging
from ._response import APIResponse as APIResponse, AsyncAPIResponse as AsyncAPIResponse

__all__ = [
    "types",
    "__version__",
    "__title__",
    "NoneType",
    "Transport",
    "ProxiesTypes",
    "CloudflareError",
    "APIError",
    "APIStatusError",
    "APITimeoutError",
    "APIConnectionError",
    "APIResponseValidationError",
    "BadRequestError",
    "AuthenticationError",
    "PermissionDeniedError",
    "NotFoundError",
    "ConflictError",
    "UnprocessableEntityError",
    "RateLimitError",
    "InternalServerError",
    "Timeout",
    "RequestOptions",
    "Client",
    "AsyncClient",
    "Stream",
    "AsyncStream",
    "Cloudflare",
    "AsyncCloudflare",
    "file_from_path",
    "BaseModel",
]

_setup_logging()

# Update the __module__ attribute for exported symbols so that
# error messages point to this module instead of the module
# it was originally defined in, e.g.
# cloudflare._exceptions.NotFoundError -> cloudflare.NotFoundError
__locals = locals()
for __name in __all__:
    if not __name.startswith("__"):
        try:
            setattr(__locals[__name], "__module__", "cloudflare")
        except (TypeError, AttributeError):
            # Some of our exported symbols are builtins which we can't set attributes for.
            pass
