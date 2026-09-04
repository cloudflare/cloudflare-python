# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RegistrationStatusGetResponse", "Links", "Error"]


class Links(BaseModel):
    self: str
    """URL to this status resource."""

    resource: Optional[str] = None
    """URL to the domain resource."""


class Error(BaseModel):
    """Provides error details when a workflow reaches the `failed` state.

    The workflow type (registration, update, etc.) and underlying registry response determine the specific codes and messages. Workflow error codes differ from immediate HTTP error `errors[].code` values in non-2xx responses. Surface `error.message` to the user for context.
    """

    code: str
    """Machine-readable error code identifying the failure reason."""

    message: str
    """Human-readable explanation of the failure.

    May include registry-specific details.
    """


class RegistrationStatusGetResponse(BaseModel):
    """Status of an async registration workflow."""

    completed: bool
    """Indicates whether the workflow reached a terminal state.

    A `succeeded` or `failed` state returns `true`; `pending`, `in_progress`,
    `action_required`, and `blocked` return `false`.
    """

    created_at: datetime

    links: Links

    state: Literal["pending", "in_progress", "action_required", "blocked", "succeeded", "failed"]
    """Describes the workflow lifecycle state.

    - `pending`: The workflow awaits processing.
    - `in_progress`: Processing started. Continue polling `links.self`. An internal
      deadline limits the duration of this state.
    - `action_required`: The workflow pauses for user action. See `context.action`
      for details. Stop automated polling until the user completes the required
      action.
    - `blocked`: A third party, such as the domain extension's registry or a losing
      registrar, prevents progress. Continue polling because the block may resolve
      when the third party responds.
    - `succeeded`: Terminal state. The operation completed successfully. `completed`
      equals `true`. For registrations, `context.registration` contains the
      resulting registration resource.
    - `failed`: Terminal state. The operation failed. `completed` equals `true`. See
      `error.code` and `error.message` for the reason. Require user review before
      retrying.
    """

    updated_at: datetime

    context: Optional[Dict[str, object]] = None
    """Provides workflow-specific data.

    For domain-centric workflows, `context.domain_name` identifies the workflow
    subject.
    """

    error: Optional[Error] = None
    """Provides error details when a workflow reaches the `failed` state.

    The workflow type (registration, update, etc.) and underlying registry response
    determine the specific codes and messages. Workflow error codes differ from
    immediate HTTP error `errors[].code` values in non-2xx responses. Surface
    `error.message` to the user for context.
    """
