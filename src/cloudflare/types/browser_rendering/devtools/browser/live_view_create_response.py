# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["LiveViewCreateResponse", "Options", "OptionsGuardrails"]


class OptionsGuardrails(BaseModel):
    """Connection guardrails applied to this link"""

    mode: Literal["readonly"]


class Options(BaseModel):
    mode: Literal["devtools", "tab", "full"]
    """UI mode for the live view"""

    guardrails: Optional[OptionsGuardrails] = None
    """Connection guardrails applied to this link"""


class LiveViewCreateResponse(BaseModel):
    id: str
    """Target ID"""

    devtools_frontend_url: str = FieldInfo(alias="devtoolsFrontendUrl")
    """URL to open the live view in a browser"""

    options: Options

    web_socket_debugger_url: str = FieldInfo(alias="webSocketDebuggerUrl")
    """WebSocket URL for CDP connection"""
