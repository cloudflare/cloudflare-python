# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.emails.routings.rules import (
    CatchAllEmailRoutingRoutingRulesGetCatchAllRuleResponse,
    CatchAllEmailRoutingRoutingRulesUpdateCatchAllRuleResponse,
)

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.emails.routings.rules import catch_all_email_routing_routing_rules_update_catch_all_rule_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCatchAlls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_email_routing_routing_rules_get_catch_all_rule(self, client: Cloudflare) -> None:
        catch_all = client.emails.routings.rules.catch_alls.email_routing_routing_rules_get_catch_all_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CatchAllEmailRoutingRoutingRulesGetCatchAllRuleResponse, catch_all, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_email_routing_routing_rules_get_catch_all_rule(self, client: Cloudflare) -> None:
        response = (
            client.emails.routings.rules.catch_alls.with_raw_response.email_routing_routing_rules_get_catch_all_rule(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catch_all = response.parse()
        assert_matches_type(CatchAllEmailRoutingRoutingRulesGetCatchAllRuleResponse, catch_all, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_email_routing_routing_rules_get_catch_all_rule(self, client: Cloudflare) -> None:
        with client.emails.routings.rules.catch_alls.with_streaming_response.email_routing_routing_rules_get_catch_all_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catch_all = response.parse()
            assert_matches_type(CatchAllEmailRoutingRoutingRulesGetCatchAllRuleResponse, catch_all, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_email_routing_routing_rules_get_catch_all_rule(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.emails.routings.rules.catch_alls.with_raw_response.email_routing_routing_rules_get_catch_all_rule(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_email_routing_routing_rules_update_catch_all_rule(self, client: Cloudflare) -> None:
        catch_all = client.emails.routings.rules.catch_alls.email_routing_routing_rules_update_catch_all_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{"type": "forward"}, {"type": "forward"}, {"type": "forward"}],
            matchers=[{"type": "all"}, {"type": "all"}, {"type": "all"}],
        )
        assert_matches_type(CatchAllEmailRoutingRoutingRulesUpdateCatchAllRuleResponse, catch_all, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_email_routing_routing_rules_update_catch_all_rule_with_all_params(self, client: Cloudflare) -> None:
        catch_all = client.emails.routings.rules.catch_alls.email_routing_routing_rules_update_catch_all_rule(
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
            matchers=[{"type": "all"}, {"type": "all"}, {"type": "all"}],
            enabled=True,
            name="Send to user@example.net rule.",
        )
        assert_matches_type(CatchAllEmailRoutingRoutingRulesUpdateCatchAllRuleResponse, catch_all, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_email_routing_routing_rules_update_catch_all_rule(self, client: Cloudflare) -> None:
        response = (
            client.emails.routings.rules.catch_alls.with_raw_response.email_routing_routing_rules_update_catch_all_rule(
                "023e105f4ecef8ad9ca31a8372d0c353",
                actions=[{"type": "forward"}, {"type": "forward"}, {"type": "forward"}],
                matchers=[{"type": "all"}, {"type": "all"}, {"type": "all"}],
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catch_all = response.parse()
        assert_matches_type(CatchAllEmailRoutingRoutingRulesUpdateCatchAllRuleResponse, catch_all, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_email_routing_routing_rules_update_catch_all_rule(self, client: Cloudflare) -> None:
        with client.emails.routings.rules.catch_alls.with_streaming_response.email_routing_routing_rules_update_catch_all_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{"type": "forward"}, {"type": "forward"}, {"type": "forward"}],
            matchers=[{"type": "all"}, {"type": "all"}, {"type": "all"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catch_all = response.parse()
            assert_matches_type(
                CatchAllEmailRoutingRoutingRulesUpdateCatchAllRuleResponse, catch_all, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_email_routing_routing_rules_update_catch_all_rule(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.emails.routings.rules.catch_alls.with_raw_response.email_routing_routing_rules_update_catch_all_rule(
                "",
                actions=[{"type": "forward"}, {"type": "forward"}, {"type": "forward"}],
                matchers=[{"type": "all"}, {"type": "all"}, {"type": "all"}],
            )


class TestAsyncCatchAlls:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_email_routing_routing_rules_get_catch_all_rule(self, async_client: AsyncCloudflare) -> None:
        catch_all = await async_client.emails.routings.rules.catch_alls.email_routing_routing_rules_get_catch_all_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CatchAllEmailRoutingRoutingRulesGetCatchAllRuleResponse, catch_all, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_email_routing_routing_rules_get_catch_all_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.emails.routings.rules.catch_alls.with_raw_response.email_routing_routing_rules_get_catch_all_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catch_all = await response.parse()
        assert_matches_type(CatchAllEmailRoutingRoutingRulesGetCatchAllRuleResponse, catch_all, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_email_routing_routing_rules_get_catch_all_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.emails.routings.rules.catch_alls.with_streaming_response.email_routing_routing_rules_get_catch_all_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catch_all = await response.parse()
            assert_matches_type(CatchAllEmailRoutingRoutingRulesGetCatchAllRuleResponse, catch_all, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_email_routing_routing_rules_get_catch_all_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.emails.routings.rules.catch_alls.with_raw_response.email_routing_routing_rules_get_catch_all_rule(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_email_routing_routing_rules_update_catch_all_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        catch_all = (
            await async_client.emails.routings.rules.catch_alls.email_routing_routing_rules_update_catch_all_rule(
                "023e105f4ecef8ad9ca31a8372d0c353",
                actions=[{"type": "forward"}, {"type": "forward"}, {"type": "forward"}],
                matchers=[{"type": "all"}, {"type": "all"}, {"type": "all"}],
            )
        )
        assert_matches_type(CatchAllEmailRoutingRoutingRulesUpdateCatchAllRuleResponse, catch_all, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_email_routing_routing_rules_update_catch_all_rule_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        catch_all = (
            await async_client.emails.routings.rules.catch_alls.email_routing_routing_rules_update_catch_all_rule(
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
                matchers=[{"type": "all"}, {"type": "all"}, {"type": "all"}],
                enabled=True,
                name="Send to user@example.net rule.",
            )
        )
        assert_matches_type(CatchAllEmailRoutingRoutingRulesUpdateCatchAllRuleResponse, catch_all, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_email_routing_routing_rules_update_catch_all_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.emails.routings.rules.catch_alls.with_raw_response.email_routing_routing_rules_update_catch_all_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{"type": "forward"}, {"type": "forward"}, {"type": "forward"}],
            matchers=[{"type": "all"}, {"type": "all"}, {"type": "all"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catch_all = await response.parse()
        assert_matches_type(CatchAllEmailRoutingRoutingRulesUpdateCatchAllRuleResponse, catch_all, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_email_routing_routing_rules_update_catch_all_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.emails.routings.rules.catch_alls.with_streaming_response.email_routing_routing_rules_update_catch_all_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
            actions=[{"type": "forward"}, {"type": "forward"}, {"type": "forward"}],
            matchers=[{"type": "all"}, {"type": "all"}, {"type": "all"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catch_all = await response.parse()
            assert_matches_type(
                CatchAllEmailRoutingRoutingRulesUpdateCatchAllRuleResponse, catch_all, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_email_routing_routing_rules_update_catch_all_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.emails.routings.rules.catch_alls.with_raw_response.email_routing_routing_rules_update_catch_all_rule(
                "",
                actions=[{"type": "forward"}, {"type": "forward"}, {"type": "forward"}],
                matchers=[{"type": "all"}, {"type": "all"}, {"type": "all"}],
            )
