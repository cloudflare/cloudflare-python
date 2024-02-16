# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.emails.routings import (
    RuleUpdateResponse,
    RuleDeleteResponse,
    RuleEmailRoutingRoutingRulesCreateRoutingRuleResponse,
    RuleEmailRoutingRoutingRulesListRoutingRulesResponse,
    RuleGetResponse,
)

from typing import Any, cast, Optional

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.emails.routings import rule_update_params
from cloudflare.types.emails.routings import rule_email_routing_routing_rules_create_routing_rule_params
from cloudflare.types.emails.routings import rule_email_routing_routing_rules_list_routing_rules_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        rule = client.emails.routings.rules.update(
            "a7e6fb77503c41d8a7f3113c6918f10c",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
            ],
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        rule = client.emails.routings.rules.update(
            "a7e6fb77503c41d8a7f3113c6918f10c",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
            ],
            enabled=True,
            name="Send to user@example.net rule.",
            priority=0,
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.emails.routings.rules.with_raw_response.update(
            "a7e6fb77503c41d8a7f3113c6918f10c",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.emails.routings.rules.with_streaming_response.update(
            "a7e6fb77503c41d8a7f3113c6918f10c",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleUpdateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.emails.routings.rules.with_raw_response.update(
                "a7e6fb77503c41d8a7f3113c6918f10c",
                zone_identifier="",
                actions=[
                    {
                        "type": "forward",
                        "value": [
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                        ],
                    },
                    {
                        "type": "forward",
                        "value": [
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                        ],
                    },
                    {
                        "type": "forward",
                        "value": [
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                        ],
                    },
                ],
                matchers=[
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    },
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    },
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    },
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_identifier` but received ''"):
            client.emails.routings.rules.with_raw_response.update(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[
                    {
                        "type": "forward",
                        "value": [
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                        ],
                    },
                    {
                        "type": "forward",
                        "value": [
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                        ],
                    },
                    {
                        "type": "forward",
                        "value": [
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                        ],
                    },
                ],
                matchers=[
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    },
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    },
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    },
                ],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        rule = client.emails.routings.rules.delete(
            "a7e6fb77503c41d8a7f3113c6918f10c",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RuleDeleteResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.emails.routings.rules.with_raw_response.delete(
            "a7e6fb77503c41d8a7f3113c6918f10c",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleDeleteResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.emails.routings.rules.with_streaming_response.delete(
            "a7e6fb77503c41d8a7f3113c6918f10c",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleDeleteResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.emails.routings.rules.with_raw_response.delete(
                "a7e6fb77503c41d8a7f3113c6918f10c",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_identifier` but received ''"):
            client.emails.routings.rules.with_raw_response.delete(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_email_routing_routing_rules_create_routing_rule(self, client: Cloudflare) -> None:
        rule = client.emails.routings.rules.email_routing_routing_rules_create_routing_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
            ],
        )
        assert_matches_type(RuleEmailRoutingRoutingRulesCreateRoutingRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_email_routing_routing_rules_create_routing_rule_with_all_params(self, client: Cloudflare) -> None:
        rule = client.emails.routings.rules.email_routing_routing_rules_create_routing_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
            ],
            enabled=True,
            name="Send to user@example.net rule.",
            priority=0,
        )
        assert_matches_type(RuleEmailRoutingRoutingRulesCreateRoutingRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_email_routing_routing_rules_create_routing_rule(self, client: Cloudflare) -> None:
        response = client.emails.routings.rules.with_raw_response.email_routing_routing_rules_create_routing_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleEmailRoutingRoutingRulesCreateRoutingRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_email_routing_routing_rules_create_routing_rule(self, client: Cloudflare) -> None:
        with client.emails.routings.rules.with_streaming_response.email_routing_routing_rules_create_routing_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleEmailRoutingRoutingRulesCreateRoutingRuleResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_email_routing_routing_rules_create_routing_rule(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.emails.routings.rules.with_raw_response.email_routing_routing_rules_create_routing_rule(
                "",
                actions=[
                    {
                        "type": "forward",
                        "value": [
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                        ],
                    },
                    {
                        "type": "forward",
                        "value": [
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                        ],
                    },
                    {
                        "type": "forward",
                        "value": [
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                        ],
                    },
                ],
                matchers=[
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    },
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    },
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    },
                ],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_email_routing_routing_rules_list_routing_rules(self, client: Cloudflare) -> None:
        rule = client.emails.routings.rules.email_routing_routing_rules_list_routing_rules(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RuleEmailRoutingRoutingRulesListRoutingRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_email_routing_routing_rules_list_routing_rules_with_all_params(self, client: Cloudflare) -> None:
        rule = client.emails.routings.rules.email_routing_routing_rules_list_routing_rules(
            "023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            page=1,
            per_page=5,
        )
        assert_matches_type(Optional[RuleEmailRoutingRoutingRulesListRoutingRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_email_routing_routing_rules_list_routing_rules(self, client: Cloudflare) -> None:
        response = client.emails.routings.rules.with_raw_response.email_routing_routing_rules_list_routing_rules(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleEmailRoutingRoutingRulesListRoutingRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_email_routing_routing_rules_list_routing_rules(self, client: Cloudflare) -> None:
        with client.emails.routings.rules.with_streaming_response.email_routing_routing_rules_list_routing_rules(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleEmailRoutingRoutingRulesListRoutingRulesResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_email_routing_routing_rules_list_routing_rules(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.emails.routings.rules.with_raw_response.email_routing_routing_rules_list_routing_rules(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        rule = client.emails.routings.rules.get(
            "a7e6fb77503c41d8a7f3113c6918f10c",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RuleGetResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.emails.routings.rules.with_raw_response.get(
            "a7e6fb77503c41d8a7f3113c6918f10c",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(RuleGetResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.emails.routings.rules.with_streaming_response.get(
            "a7e6fb77503c41d8a7f3113c6918f10c",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(RuleGetResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.emails.routings.rules.with_raw_response.get(
                "a7e6fb77503c41d8a7f3113c6918f10c",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_identifier` but received ''"):
            client.emails.routings.rules.with_raw_response.get(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.emails.routings.rules.update(
            "a7e6fb77503c41d8a7f3113c6918f10c",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
            ],
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.emails.routings.rules.update(
            "a7e6fb77503c41d8a7f3113c6918f10c",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
            ],
            enabled=True,
            name="Send to user@example.net rule.",
            priority=0,
        )
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.emails.routings.rules.with_raw_response.update(
            "a7e6fb77503c41d8a7f3113c6918f10c",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleUpdateResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.emails.routings.rules.with_streaming_response.update(
            "a7e6fb77503c41d8a7f3113c6918f10c",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleUpdateResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.emails.routings.rules.with_raw_response.update(
                "a7e6fb77503c41d8a7f3113c6918f10c",
                zone_identifier="",
                actions=[
                    {
                        "type": "forward",
                        "value": [
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                        ],
                    },
                    {
                        "type": "forward",
                        "value": [
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                        ],
                    },
                    {
                        "type": "forward",
                        "value": [
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                        ],
                    },
                ],
                matchers=[
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    },
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    },
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    },
                ],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_identifier` but received ''"):
            await async_client.emails.routings.rules.with_raw_response.update(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                actions=[
                    {
                        "type": "forward",
                        "value": [
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                        ],
                    },
                    {
                        "type": "forward",
                        "value": [
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                        ],
                    },
                    {
                        "type": "forward",
                        "value": [
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                        ],
                    },
                ],
                matchers=[
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    },
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    },
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    },
                ],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.emails.routings.rules.delete(
            "a7e6fb77503c41d8a7f3113c6918f10c",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RuleDeleteResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.emails.routings.rules.with_raw_response.delete(
            "a7e6fb77503c41d8a7f3113c6918f10c",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleDeleteResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.emails.routings.rules.with_streaming_response.delete(
            "a7e6fb77503c41d8a7f3113c6918f10c",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleDeleteResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.emails.routings.rules.with_raw_response.delete(
                "a7e6fb77503c41d8a7f3113c6918f10c",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_identifier` but received ''"):
            await async_client.emails.routings.rules.with_raw_response.delete(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_email_routing_routing_rules_create_routing_rule(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.emails.routings.rules.email_routing_routing_rules_create_routing_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
            ],
        )
        assert_matches_type(RuleEmailRoutingRoutingRulesCreateRoutingRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_email_routing_routing_rules_create_routing_rule_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        rule = await async_client.emails.routings.rules.email_routing_routing_rules_create_routing_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
            ],
            enabled=True,
            name="Send to user@example.net rule.",
            priority=0,
        )
        assert_matches_type(RuleEmailRoutingRoutingRulesCreateRoutingRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_email_routing_routing_rules_create_routing_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.emails.routings.rules.with_raw_response.email_routing_routing_rules_create_routing_rule(
                "023e105f4ecef8ad9ca31a8372d0c353",
                actions=[
                    {
                        "type": "forward",
                        "value": [
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                        ],
                    },
                    {
                        "type": "forward",
                        "value": [
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                        ],
                    },
                    {
                        "type": "forward",
                        "value": [
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                        ],
                    },
                ],
                matchers=[
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    },
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    },
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    },
                ],
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleEmailRoutingRoutingRulesCreateRoutingRuleResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_email_routing_routing_rules_create_routing_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.emails.routings.rules.with_streaming_response.email_routing_routing_rules_create_routing_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
            actions=[
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
                {
                    "type": "forward",
                    "value": [
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                        "destinationaddress@example.net",
                    ],
                },
            ],
            matchers=[
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
                {
                    "field": "to",
                    "type": "literal",
                    "value": "test@example.com",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleEmailRoutingRoutingRulesCreateRoutingRuleResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_email_routing_routing_rules_create_routing_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.emails.routings.rules.with_raw_response.email_routing_routing_rules_create_routing_rule(
                "",
                actions=[
                    {
                        "type": "forward",
                        "value": [
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                        ],
                    },
                    {
                        "type": "forward",
                        "value": [
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                        ],
                    },
                    {
                        "type": "forward",
                        "value": [
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                            "destinationaddress@example.net",
                        ],
                    },
                ],
                matchers=[
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    },
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    },
                    {
                        "field": "to",
                        "type": "literal",
                        "value": "test@example.com",
                    },
                ],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_email_routing_routing_rules_list_routing_rules(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.emails.routings.rules.email_routing_routing_rules_list_routing_rules(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RuleEmailRoutingRoutingRulesListRoutingRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_email_routing_routing_rules_list_routing_rules_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        rule = await async_client.emails.routings.rules.email_routing_routing_rules_list_routing_rules(
            "023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            page=1,
            per_page=5,
        )
        assert_matches_type(Optional[RuleEmailRoutingRoutingRulesListRoutingRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_email_routing_routing_rules_list_routing_rules(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.emails.routings.rules.with_raw_response.email_routing_routing_rules_list_routing_rules(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleEmailRoutingRoutingRulesListRoutingRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_email_routing_routing_rules_list_routing_rules(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.emails.routings.rules.with_streaming_response.email_routing_routing_rules_list_routing_rules(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleEmailRoutingRoutingRulesListRoutingRulesResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_email_routing_routing_rules_list_routing_rules(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.emails.routings.rules.with_raw_response.email_routing_routing_rules_list_routing_rules(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.emails.routings.rules.get(
            "a7e6fb77503c41d8a7f3113c6918f10c",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RuleGetResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.emails.routings.rules.with_raw_response.get(
            "a7e6fb77503c41d8a7f3113c6918f10c",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(RuleGetResponse, rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.emails.routings.rules.with_streaming_response.get(
            "a7e6fb77503c41d8a7f3113c6918f10c",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(RuleGetResponse, rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.emails.routings.rules.with_raw_response.get(
                "a7e6fb77503c41d8a7f3113c6918f10c",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_identifier` but received ''"):
            await async_client.emails.routings.rules.with_raw_response.get(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )
