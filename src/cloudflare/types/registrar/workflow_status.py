# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WorkflowStatus", "Links", "Error"]


class Links(BaseModel):
    self: str
    """URL to this status resource."""

    resource: Optional[str] = None
    """URL to the domain resource."""


class Error(BaseModel):
    """Error details when a workflow reaches the `failed` state.

    The specific
    error codes and messages depend on the workflow type (registration,
    update, etc.) and the underlying registry response. These workflow
    error codes are separate from immediate HTTP error `errors[].code`
    values returned by non-2xx responses. Surface
    `error.message` to the user for context.
    """

    code: str
    """Machine-readable error code identifying the failure reason."""

    message: str
    """Human-readable explanation of the failure.

    May include registry-specific details.
    """


class WorkflowStatus(BaseModel):
    """Status of an async registration workflow."""

    completed: bool
    """Whether the workflow has reached a terminal state.

    `true` when `state` is `succeeded` or `failed`. `false` for `pending`,
    `in_progress`, `action_required`, and `blocked`.
    """

    created_at: datetime

    links: Links

    state: Literal["pending", "in_progress", "action_required", "blocked", "succeeded", "failed"]
    """Workflow lifecycle state.

    - `pending`: Workflow has been created but not yet started processing.
    - `in_progress`: Actively processing. Continue polling `links.self`. The
      workflow has an internal deadline and will not remain in this state
      indefinitely.
    - `action_required`: Paused — requires action by the user (not the system). See
      `context.action` for what is needed. An automated polling loop must break on
      this state; it will not resolve on its own without user intervention.
    - `blocked`: The workflow cannot make progress due to a third party such as the
      domain extension's registry or a losing registrar. No user action will help.
      Continue polling — the block may resolve when the third party responds.
    - `succeeded`: Terminal. The operation completed successfully. `completed` will
      be `true`. For registrations, `context.registration` contains the resulting
      registration resource.
    - `failed`: Terminal. The operation failed. `completed` will be `true`. See
      `error.code` and `error.message` for the reason. Do not auto-retry without
      user review.
    """

    updated_at: datetime

    context: Optional[Dict[str, object]] = None
    """Workflow-specific data for this workflow.

    The workflow subject is identified by `context.domain_name` for domain-centric
    workflows.
    """

    error: Optional[Error] = None
    """Error details when a workflow reaches the `failed` state.

    The specific error codes and messages depend on the workflow type (registration,
    update, etc.) and the underlying registry response. These workflow error codes
    are separate from immediate HTTP error `errors[].code` values returned by
    non-2xx responses. Surface `error.message` to the user for context.
    """
