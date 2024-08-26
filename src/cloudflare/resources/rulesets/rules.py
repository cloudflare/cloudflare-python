# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from typing_extensions import Literal

from ...types.rulesets.logging_param import LoggingParam

from ...types.rulesets.rule_create_response import RuleCreateResponse

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from ..._base_client import make_request_options

from typing import Type

from ...types.rulesets.rule_delete_response import RuleDeleteResponse

from ...types.rulesets.rule_edit_response import RuleEditResponse

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

from ...types.rulesets import rule_create_params, rule_edit_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.rulesets import rule_create_params
from ...types.rulesets import rule_edit_params
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from ...types.rulesets import Logging
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["RulesResource", "AsyncRulesResource"]

class RulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self)

    @overload
    def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["block"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.BlockRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["challenge"] | NotGiven = NOT_GIVEN,
    action_parameters: object | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["compress_response"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.CompressResponseRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["execute"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.ExecuteRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["js_challenge"] | NotGiven = NOT_GIVEN,
    action_parameters: object | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["log"] | NotGiven = NOT_GIVEN,
    action_parameters: object | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["managed_challenge"] | NotGiven = NOT_GIVEN,
    action_parameters: object | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["redirect"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.RedirectRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["rewrite"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.RewriteRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["route"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.RouteRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["score"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.ScoreRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["serve_error"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.ServeErrorRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["set_config"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.SetConfigRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["skip"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.SkipRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["set_cache_settings"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.SetCacheSettingsRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["log_custom_field"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.LogCustomFieldRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["ddos_dynamic"] | NotGiven = NOT_GIVEN,
    action_parameters: object | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["force_connection_close"] | NotGiven = NOT_GIVEN,
    action_parameters: object | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["block"] | Literal["challenge"] | Literal["compress_response"] | Literal["execute"] | Literal["js_challenge"] | Literal["log"] | Literal["managed_challenge"] | Literal["redirect"] | Literal["rewrite"] | Literal["route"] | Literal["score"] | Literal["serve_error"] | Literal["set_config"] | Literal["skip"] | Literal["set_cache_settings"] | Literal["log_custom_field"] | Literal["ddos_dynamic"] | Literal["force_connection_close"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.BlockRuleActionParameters | object | rule_create_params.CompressResponseRuleActionParameters | rule_create_params.ExecuteRuleActionParameters | rule_create_params.RedirectRuleActionParameters | rule_create_params.RewriteRuleActionParameters | rule_create_params.RouteRuleActionParameters | rule_create_params.ScoreRuleActionParameters | rule_create_params.ServeErrorRuleActionParameters | rule_create_params.SetConfigRuleActionParameters | rule_create_params.SkipRuleActionParameters | rule_create_params.SetCacheSettingsRuleActionParameters | rule_create_params.LogCustomFieldRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        if not ruleset_id:
          raise ValueError(
            f'Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}'
          )
        if account_id and zone_id:
          raise ValueError('You cannot provide both account_id and zone_id');

        if account_id:
          account_or_zone = "accounts"
          account_or_zone_id = account_id
        else:
          if not zone_id:
            raise ValueError('You must provide either account_id or zone_id');

          account_or_zone = "zones"
          account_or_zone_id = zone_id
        return self._post(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules",
            body=maybe_transform({
                "id": id,
                "action": action,
                "action_parameters": action_parameters,
                "description": description,
                "enabled": enabled,
                "expression": expression,
                "logging": logging,
                "ref": ref,
            }, rule_create_params.RuleCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[RuleCreateResponse]._unwrapper),
            cast_to=cast(Type[RuleCreateResponse], ResultWrapper[RuleCreateResponse]),
        )

    def delete(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleDeleteResponse:
        """
        Deletes an existing rule from an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ruleset_id:
          raise ValueError(
            f'Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}'
          )
        if not rule_id:
          raise ValueError(
            f'Expected a non-empty value for `rule_id` but received {rule_id!r}'
          )
        if account_id and zone_id:
          raise ValueError('You cannot provide both account_id and zone_id');

        if account_id:
          account_or_zone = "accounts"
          account_or_zone_id = account_id
        else:
          if not zone_id:
            raise ValueError('You must provide either account_id or zone_id');

          account_or_zone = "zones"
          account_or_zone_id = zone_id
        return self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules/{rule_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[RuleDeleteResponse]._unwrapper),
            cast_to=cast(Type[RuleDeleteResponse], ResultWrapper[RuleDeleteResponse]),
        )

    @overload
    def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["block"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.BlockRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["challenge"] | NotGiven = NOT_GIVEN,
    action_parameters: object | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["compress_response"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.CompressResponseRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["execute"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.ExecuteRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["js_challenge"] | NotGiven = NOT_GIVEN,
    action_parameters: object | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["log"] | NotGiven = NOT_GIVEN,
    action_parameters: object | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["managed_challenge"] | NotGiven = NOT_GIVEN,
    action_parameters: object | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["redirect"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.RedirectRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["rewrite"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.RewriteRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["route"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.RouteRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["score"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.ScoreRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["serve_error"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.ServeErrorRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["set_config"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.SetConfigRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["skip"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.SkipRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["set_cache_settings"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.SetCacheSettingsRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["log_custom_field"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.LogCustomFieldRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["ddos_dynamic"] | NotGiven = NOT_GIVEN,
    action_parameters: object | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["force_connection_close"] | NotGiven = NOT_GIVEN,
    action_parameters: object | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @required_args(["ruleset_id"])
    def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["block"] | Literal["challenge"] | Literal["compress_response"] | Literal["execute"] | Literal["js_challenge"] | Literal["log"] | Literal["managed_challenge"] | Literal["redirect"] | Literal["rewrite"] | Literal["route"] | Literal["score"] | Literal["serve_error"] | Literal["set_config"] | Literal["skip"] | Literal["set_cache_settings"] | Literal["log_custom_field"] | Literal["ddos_dynamic"] | Literal["force_connection_close"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.BlockRuleActionParameters | object | rule_edit_params.CompressResponseRuleActionParameters | rule_edit_params.ExecuteRuleActionParameters | rule_edit_params.RedirectRuleActionParameters | rule_edit_params.RewriteRuleActionParameters | rule_edit_params.RouteRuleActionParameters | rule_edit_params.ScoreRuleActionParameters | rule_edit_params.ServeErrorRuleActionParameters | rule_edit_params.SetConfigRuleActionParameters | rule_edit_params.SkipRuleActionParameters | rule_edit_params.SetCacheSettingsRuleActionParameters | rule_edit_params.LogCustomFieldRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        if not ruleset_id:
          raise ValueError(
            f'Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}'
          )
        if not rule_id:
          raise ValueError(
            f'Expected a non-empty value for `rule_id` but received {rule_id!r}'
          )
        if account_id and zone_id:
          raise ValueError('You cannot provide both account_id and zone_id');

        if account_id:
          account_or_zone = "accounts"
          account_or_zone_id = account_id
        else:
          if not zone_id:
            raise ValueError('You must provide either account_id or zone_id');

          account_or_zone = "zones"
          account_or_zone_id = zone_id
        return self._patch(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules/{rule_id}",
            body=maybe_transform({
                "id": id,
                "action": action,
                "action_parameters": action_parameters,
                "description": description,
                "enabled": enabled,
                "expression": expression,
                "logging": logging,
                "ref": ref,
            }, rule_edit_params.RuleEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[RuleEditResponse]._unwrapper),
            cast_to=cast(Type[RuleEditResponse], ResultWrapper[RuleEditResponse]),
        )

class AsyncRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self)

    @overload
    async def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["block"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.BlockRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["challenge"] | NotGiven = NOT_GIVEN,
    action_parameters: object | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["compress_response"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.CompressResponseRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["execute"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.ExecuteRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["js_challenge"] | NotGiven = NOT_GIVEN,
    action_parameters: object | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["log"] | NotGiven = NOT_GIVEN,
    action_parameters: object | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["managed_challenge"] | NotGiven = NOT_GIVEN,
    action_parameters: object | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["redirect"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.RedirectRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["rewrite"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.RewriteRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["route"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.RouteRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["score"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.ScoreRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["serve_error"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.ServeErrorRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["set_config"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.SetConfigRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["skip"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.SkipRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["set_cache_settings"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.SetCacheSettingsRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["log_custom_field"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.LogCustomFieldRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["ddos_dynamic"] | NotGiven = NOT_GIVEN,
    action_parameters: object | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["force_connection_close"] | NotGiven = NOT_GIVEN,
    action_parameters: object | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        """Adds a new rule to an account or zone ruleset.

        The rule will be added to the end
        of the existing list of rules in the ruleset by default.

        Args:
          ruleset_id: The unique ID of the ruleset.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    async def create(self,
    ruleset_id: str,
    *,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["block"] | Literal["challenge"] | Literal["compress_response"] | Literal["execute"] | Literal["js_challenge"] | Literal["log"] | Literal["managed_challenge"] | Literal["redirect"] | Literal["rewrite"] | Literal["route"] | Literal["score"] | Literal["serve_error"] | Literal["set_config"] | Literal["skip"] | Literal["set_cache_settings"] | Literal["log_custom_field"] | Literal["ddos_dynamic"] | Literal["force_connection_close"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_create_params.BlockRuleActionParameters | object | rule_create_params.CompressResponseRuleActionParameters | rule_create_params.ExecuteRuleActionParameters | rule_create_params.RedirectRuleActionParameters | rule_create_params.RewriteRuleActionParameters | rule_create_params.RouteRuleActionParameters | rule_create_params.ScoreRuleActionParameters | rule_create_params.ServeErrorRuleActionParameters | rule_create_params.SetConfigRuleActionParameters | rule_create_params.SkipRuleActionParameters | rule_create_params.SetCacheSettingsRuleActionParameters | rule_create_params.LogCustomFieldRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleCreateResponse:
        if not ruleset_id:
          raise ValueError(
            f'Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}'
          )
        if account_id and zone_id:
          raise ValueError('You cannot provide both account_id and zone_id');

        if account_id:
          account_or_zone = "accounts"
          account_or_zone_id = account_id
        else:
          if not zone_id:
            raise ValueError('You must provide either account_id or zone_id');

          account_or_zone = "zones"
          account_or_zone_id = zone_id
        return await self._post(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules",
            body=await async_maybe_transform({
                "id": id,
                "action": action,
                "action_parameters": action_parameters,
                "description": description,
                "enabled": enabled,
                "expression": expression,
                "logging": logging,
                "ref": ref,
            }, rule_create_params.RuleCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[RuleCreateResponse]._unwrapper),
            cast_to=cast(Type[RuleCreateResponse], ResultWrapper[RuleCreateResponse]),
        )

    async def delete(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleDeleteResponse:
        """
        Deletes an existing rule from an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ruleset_id:
          raise ValueError(
            f'Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}'
          )
        if not rule_id:
          raise ValueError(
            f'Expected a non-empty value for `rule_id` but received {rule_id!r}'
          )
        if account_id and zone_id:
          raise ValueError('You cannot provide both account_id and zone_id');

        if account_id:
          account_or_zone = "accounts"
          account_or_zone_id = account_id
        else:
          if not zone_id:
            raise ValueError('You must provide either account_id or zone_id');

          account_or_zone = "zones"
          account_or_zone_id = zone_id
        return await self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules/{rule_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[RuleDeleteResponse]._unwrapper),
            cast_to=cast(Type[RuleDeleteResponse], ResultWrapper[RuleDeleteResponse]),
        )

    @overload
    async def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["block"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.BlockRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["challenge"] | NotGiven = NOT_GIVEN,
    action_parameters: object | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["compress_response"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.CompressResponseRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["execute"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.ExecuteRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["js_challenge"] | NotGiven = NOT_GIVEN,
    action_parameters: object | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["log"] | NotGiven = NOT_GIVEN,
    action_parameters: object | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["managed_challenge"] | NotGiven = NOT_GIVEN,
    action_parameters: object | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["redirect"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.RedirectRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["rewrite"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.RewriteRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["route"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.RouteRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["score"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.ScoreRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["serve_error"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.ServeErrorRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["set_config"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.SetConfigRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["skip"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.SkipRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["set_cache_settings"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.SetCacheSettingsRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["log_custom_field"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.LogCustomFieldRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["ddos_dynamic"] | NotGiven = NOT_GIVEN,
    action_parameters: object | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @overload
    async def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["force_connection_close"] | NotGiven = NOT_GIVEN,
    action_parameters: object | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        """
        Updates an existing rule in an account or zone ruleset.

        Args:
          ruleset_id: The unique ID of the ruleset.

          rule_id: The unique ID of the rule.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          id: The unique ID of the rule.

          action: The action to perform when the rule matches.

          action_parameters: The parameters configuring the rule's action.

          description: An informative description of the rule.

          enabled: Whether the rule should be executed.

          expression: The expression defining which traffic will match the rule.

          logging: An object configuring the rule's logging behavior.

          ref: The reference of the rule (the rule ID by default).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...
    @required_args(["ruleset_id"])
    async def edit(self,
    rule_id: str,
    *,
    ruleset_id: str,
    account_id: str | NotGiven = NOT_GIVEN,
    zone_id: str | NotGiven = NOT_GIVEN,
    id: str | NotGiven = NOT_GIVEN,
    action: Literal["block"] | Literal["challenge"] | Literal["compress_response"] | Literal["execute"] | Literal["js_challenge"] | Literal["log"] | Literal["managed_challenge"] | Literal["redirect"] | Literal["rewrite"] | Literal["route"] | Literal["score"] | Literal["serve_error"] | Literal["set_config"] | Literal["skip"] | Literal["set_cache_settings"] | Literal["log_custom_field"] | Literal["ddos_dynamic"] | Literal["force_connection_close"] | NotGiven = NOT_GIVEN,
    action_parameters: rule_edit_params.BlockRuleActionParameters | object | rule_edit_params.CompressResponseRuleActionParameters | rule_edit_params.ExecuteRuleActionParameters | rule_edit_params.RedirectRuleActionParameters | rule_edit_params.RewriteRuleActionParameters | rule_edit_params.RouteRuleActionParameters | rule_edit_params.ScoreRuleActionParameters | rule_edit_params.ServeErrorRuleActionParameters | rule_edit_params.SetConfigRuleActionParameters | rule_edit_params.SkipRuleActionParameters | rule_edit_params.SetCacheSettingsRuleActionParameters | rule_edit_params.LogCustomFieldRuleActionParameters | NotGiven = NOT_GIVEN,
    description: str | NotGiven = NOT_GIVEN,
    enabled: bool | NotGiven = NOT_GIVEN,
    expression: str | NotGiven = NOT_GIVEN,
    logging: LoggingParam | NotGiven = NOT_GIVEN,
    ref: str | NotGiven = NOT_GIVEN,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> RuleEditResponse:
        if not ruleset_id:
          raise ValueError(
            f'Expected a non-empty value for `ruleset_id` but received {ruleset_id!r}'
          )
        if not rule_id:
          raise ValueError(
            f'Expected a non-empty value for `rule_id` but received {rule_id!r}'
          )
        if account_id and zone_id:
          raise ValueError('You cannot provide both account_id and zone_id');

        if account_id:
          account_or_zone = "accounts"
          account_or_zone_id = account_id
        else:
          if not zone_id:
            raise ValueError('You must provide either account_id or zone_id');

          account_or_zone = "zones"
          account_or_zone_id = zone_id
        return await self._patch(
            f"/{account_or_zone}/{account_or_zone_id}/rulesets/{ruleset_id}/rules/{rule_id}",
            body=await async_maybe_transform({
                "id": id,
                "action": action,
                "action_parameters": action_parameters,
                "description": description,
                "enabled": enabled,
                "expression": expression,
                "logging": logging,
                "ref": ref,
            }, rule_edit_params.RuleEditParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[RuleEditResponse]._unwrapper),
            cast_to=cast(Type[RuleEditResponse], ResultWrapper[RuleEditResponse]),
        )

class RulesResourceWithRawResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.create = to_raw_response_wrapper(
            rules.create,
        )
        self.delete = to_raw_response_wrapper(
            rules.delete,
        )
        self.edit = to_raw_response_wrapper(
            rules.edit,
        )

class AsyncRulesResourceWithRawResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.create = async_to_raw_response_wrapper(
            rules.create,
        )
        self.delete = async_to_raw_response_wrapper(
            rules.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            rules.edit,
        )

class RulesResourceWithStreamingResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

        self.create = to_streamed_response_wrapper(
            rules.create,
        )
        self.delete = to_streamed_response_wrapper(
            rules.delete,
        )
        self.edit = to_streamed_response_wrapper(
            rules.edit,
        )

class AsyncRulesResourceWithStreamingResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

        self.create = async_to_streamed_response_wrapper(
            rules.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            rules.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            rules.edit,
        )