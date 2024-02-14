# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.firewalls import (
    UaRuleUpdateResponse,
    UaRuleDeleteResponse,
    UaRuleGetResponse,
    UaRuleUserAgentBlockingRulesCreateAUserAgentBlockingRuleResponse,
    UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.firewalls import ua_rule_update_params
from cloudflare.types.firewalls import ua_rule_user_agent_blocking_rules_create_a_user_agent_blocking_rule_params
from cloudflare.types.firewalls import ua_rule_user_agent_blocking_rules_list_user_agent_blocking_rules_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUaRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        ua_rule = client.firewalls.ua_rules.update(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[UaRuleUpdateResponse], ua_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.firewalls.ua_rules.with_raw_response.update(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ua_rule = response.parse()
        assert_matches_type(Optional[UaRuleUpdateResponse], ua_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.firewalls.ua_rules.with_streaming_response.update(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ua_rule = response.parse()
            assert_matches_type(Optional[UaRuleUpdateResponse], ua_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewalls.ua_rules.with_raw_response.update(
                "372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.firewalls.ua_rules.with_raw_response.update(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        ua_rule = client.firewalls.ua_rules.delete(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[UaRuleDeleteResponse], ua_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.firewalls.ua_rules.with_raw_response.delete(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ua_rule = response.parse()
        assert_matches_type(Optional[UaRuleDeleteResponse], ua_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.firewalls.ua_rules.with_streaming_response.delete(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ua_rule = response.parse()
            assert_matches_type(Optional[UaRuleDeleteResponse], ua_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewalls.ua_rules.with_raw_response.delete(
                "372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.firewalls.ua_rules.with_raw_response.delete(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        ua_rule = client.firewalls.ua_rules.get(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[UaRuleGetResponse], ua_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.firewalls.ua_rules.with_raw_response.get(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ua_rule = response.parse()
        assert_matches_type(Optional[UaRuleGetResponse], ua_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.firewalls.ua_rules.with_streaming_response.get(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ua_rule = response.parse()
            assert_matches_type(Optional[UaRuleGetResponse], ua_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewalls.ua_rules.with_raw_response.get(
                "372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.firewalls.ua_rules.with_raw_response.get(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_user_agent_blocking_rules_create_a_user_agent_blocking_rule(self, client: Cloudflare) -> None:
        ua_rule = client.firewalls.ua_rules.user_agent_blocking_rules_create_a_user_agent_blocking_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(
            Optional[UaRuleUserAgentBlockingRulesCreateAUserAgentBlockingRuleResponse], ua_rule, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_user_agent_blocking_rules_create_a_user_agent_blocking_rule(self, client: Cloudflare) -> None:
        response = (
            client.firewalls.ua_rules.with_raw_response.user_agent_blocking_rules_create_a_user_agent_blocking_rule(
                "023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ua_rule = response.parse()
        assert_matches_type(
            Optional[UaRuleUserAgentBlockingRulesCreateAUserAgentBlockingRuleResponse], ua_rule, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_user_agent_blocking_rules_create_a_user_agent_blocking_rule(
        self, client: Cloudflare
    ) -> None:
        with client.firewalls.ua_rules.with_streaming_response.user_agent_blocking_rules_create_a_user_agent_blocking_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ua_rule = response.parse()
            assert_matches_type(
                Optional[UaRuleUserAgentBlockingRulesCreateAUserAgentBlockingRuleResponse], ua_rule, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_user_agent_blocking_rules_create_a_user_agent_blocking_rule(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewalls.ua_rules.with_raw_response.user_agent_blocking_rules_create_a_user_agent_blocking_rule(
                "",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_user_agent_blocking_rules_list_user_agent_blocking_rules(self, client: Cloudflare) -> None:
        ua_rule = client.firewalls.ua_rules.user_agent_blocking_rules_list_user_agent_blocking_rules(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponse], ua_rule, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_user_agent_blocking_rules_list_user_agent_blocking_rules_with_all_params(
        self, client: Cloudflare
    ) -> None:
        ua_rule = client.firewalls.ua_rules.user_agent_blocking_rules_list_user_agent_blocking_rules(
            "023e105f4ecef8ad9ca31a8372d0c353",
            description="abusive",
            description_search="abusive",
            page=1,
            per_page=1,
            ua_search="Safari",
        )
        assert_matches_type(
            Optional[UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponse], ua_rule, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_user_agent_blocking_rules_list_user_agent_blocking_rules(self, client: Cloudflare) -> None:
        response = client.firewalls.ua_rules.with_raw_response.user_agent_blocking_rules_list_user_agent_blocking_rules(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ua_rule = response.parse()
        assert_matches_type(
            Optional[UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponse], ua_rule, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_user_agent_blocking_rules_list_user_agent_blocking_rules(
        self, client: Cloudflare
    ) -> None:
        with client.firewalls.ua_rules.with_streaming_response.user_agent_blocking_rules_list_user_agent_blocking_rules(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ua_rule = response.parse()
            assert_matches_type(
                Optional[UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponse], ua_rule, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_user_agent_blocking_rules_list_user_agent_blocking_rules(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.firewalls.ua_rules.with_raw_response.user_agent_blocking_rules_list_user_agent_blocking_rules(
                "",
            )


class TestAsyncUaRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        ua_rule = await async_client.firewalls.ua_rules.update(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(Optional[UaRuleUpdateResponse], ua_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.ua_rules.with_raw_response.update(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ua_rule = await response.parse()
        assert_matches_type(Optional[UaRuleUpdateResponse], ua_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.ua_rules.with_streaming_response.update(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ua_rule = await response.parse()
            assert_matches_type(Optional[UaRuleUpdateResponse], ua_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewalls.ua_rules.with_raw_response.update(
                "372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.firewalls.ua_rules.with_raw_response.update(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        ua_rule = await async_client.firewalls.ua_rules.delete(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[UaRuleDeleteResponse], ua_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.ua_rules.with_raw_response.delete(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ua_rule = await response.parse()
        assert_matches_type(Optional[UaRuleDeleteResponse], ua_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.ua_rules.with_streaming_response.delete(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ua_rule = await response.parse()
            assert_matches_type(Optional[UaRuleDeleteResponse], ua_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewalls.ua_rules.with_raw_response.delete(
                "372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.firewalls.ua_rules.with_raw_response.delete(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        ua_rule = await async_client.firewalls.ua_rules.get(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[UaRuleGetResponse], ua_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.ua_rules.with_raw_response.get(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ua_rule = await response.parse()
        assert_matches_type(Optional[UaRuleGetResponse], ua_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.ua_rules.with_streaming_response.get(
            "372e67954025e0ba6aaa6d586b9e0b59",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ua_rule = await response.parse()
            assert_matches_type(Optional[UaRuleGetResponse], ua_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewalls.ua_rules.with_raw_response.get(
                "372e67954025e0ba6aaa6d586b9e0b59",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.firewalls.ua_rules.with_raw_response.get(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_user_agent_blocking_rules_create_a_user_agent_blocking_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        ua_rule = await async_client.firewalls.ua_rules.user_agent_blocking_rules_create_a_user_agent_blocking_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(
            Optional[UaRuleUserAgentBlockingRulesCreateAUserAgentBlockingRuleResponse], ua_rule, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_user_agent_blocking_rules_create_a_user_agent_blocking_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.firewalls.ua_rules.with_raw_response.user_agent_blocking_rules_create_a_user_agent_blocking_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ua_rule = await response.parse()
        assert_matches_type(
            Optional[UaRuleUserAgentBlockingRulesCreateAUserAgentBlockingRuleResponse], ua_rule, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_user_agent_blocking_rules_create_a_user_agent_blocking_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.firewalls.ua_rules.with_streaming_response.user_agent_blocking_rules_create_a_user_agent_blocking_rule(
            "023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ua_rule = await response.parse()
            assert_matches_type(
                Optional[UaRuleUserAgentBlockingRulesCreateAUserAgentBlockingRuleResponse], ua_rule, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_user_agent_blocking_rules_create_a_user_agent_blocking_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewalls.ua_rules.with_raw_response.user_agent_blocking_rules_create_a_user_agent_blocking_rule(
                "",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_user_agent_blocking_rules_list_user_agent_blocking_rules(
        self, async_client: AsyncCloudflare
    ) -> None:
        ua_rule = await async_client.firewalls.ua_rules.user_agent_blocking_rules_list_user_agent_blocking_rules(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponse], ua_rule, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_user_agent_blocking_rules_list_user_agent_blocking_rules_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        ua_rule = await async_client.firewalls.ua_rules.user_agent_blocking_rules_list_user_agent_blocking_rules(
            "023e105f4ecef8ad9ca31a8372d0c353",
            description="abusive",
            description_search="abusive",
            page=1,
            per_page=1,
            ua_search="Safari",
        )
        assert_matches_type(
            Optional[UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponse], ua_rule, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_user_agent_blocking_rules_list_user_agent_blocking_rules(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.firewalls.ua_rules.with_raw_response.user_agent_blocking_rules_list_user_agent_blocking_rules(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ua_rule = await response.parse()
        assert_matches_type(
            Optional[UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponse], ua_rule, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_user_agent_blocking_rules_list_user_agent_blocking_rules(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.firewalls.ua_rules.with_streaming_response.user_agent_blocking_rules_list_user_agent_blocking_rules(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ua_rule = await response.parse()
            assert_matches_type(
                Optional[UaRuleUserAgentBlockingRulesListUserAgentBlockingRulesResponse], ua_rule, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_user_agent_blocking_rules_list_user_agent_blocking_rules(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.firewalls.ua_rules.with_raw_response.user_agent_blocking_rules_list_user_agent_blocking_rules(
                "",
            )
