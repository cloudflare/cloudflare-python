# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.users.firewalls.access_rules import (
    RuleDeleteResponse,
    RuleUpdateResponse,
    RuleIPAccessRulesForAUserListIPAccessRulesResponse,
    RuleIPAccessRulesForAUserCreateAnIPAccessRuleResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        rule = client.users.firewalls.access_rules.rules.update(
            "92f17202ed8bd63d69a66b86a49a8f6b",
        )
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        rule = client.users.firewalls.access_rules.rules.update(
            "92f17202ed8bd63d69a66b86a49a8f6b",
            mode="challenge",
            notes="This rule is enabled because of an event that occurred on date X.",
        )
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.users.firewalls.access_rules.rules.with_raw_response.update(
            "92f17202ed8bd63d69a66b86a49a8f6b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.users.firewalls.access_rules.rules.with_streaming_response.update(
            "92f17202ed8bd63d69a66b86a49a8f6b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.users.firewalls.access_rules.rules.with_raw_response.update(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        rule = client.users.firewalls.access_rules.rules.delete(
            "92f17202ed8bd63d69a66b86a49a8f6b",
        )
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.users.firewalls.access_rules.rules.with_raw_response.delete(
            "92f17202ed8bd63d69a66b86a49a8f6b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.users.firewalls.access_rules.rules.with_streaming_response.delete(
            "92f17202ed8bd63d69a66b86a49a8f6b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.users.firewalls.access_rules.rules.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_ip_access_rules_for_a_user_create_an_ip_access_rule(self, client: Cloudflare) -> None:
        rule = client.users.firewalls.access_rules.rules.ip_access_rules_for_a_user_create_an_ip_access_rule(
            configuration={},
            mode="challenge",
        )
        assert_matches_type(Optional[RuleIPAccessRulesForAUserCreateAnIPAccessRuleResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_ip_access_rules_for_a_user_create_an_ip_access_rule_with_all_params(
        self, client: Cloudflare
    ) -> None:
        rule = client.users.firewalls.access_rules.rules.ip_access_rules_for_a_user_create_an_ip_access_rule(
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            mode="challenge",
            notes="This rule is enabled because of an event that occurred on date X.",
        )
        assert_matches_type(Optional[RuleIPAccessRulesForAUserCreateAnIPAccessRuleResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_ip_access_rules_for_a_user_create_an_ip_access_rule(self, client: Cloudflare) -> None:
        response = client.users.firewalls.access_rules.rules.with_raw_response.ip_access_rules_for_a_user_create_an_ip_access_rule(
            configuration={},
            mode="challenge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleIPAccessRulesForAUserCreateAnIPAccessRuleResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_ip_access_rules_for_a_user_create_an_ip_access_rule(self, client: Cloudflare) -> None:
        with client.users.firewalls.access_rules.rules.with_streaming_response.ip_access_rules_for_a_user_create_an_ip_access_rule(
            configuration={},
            mode="challenge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(
                Optional[RuleIPAccessRulesForAUserCreateAnIPAccessRuleResponse], rule, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_ip_access_rules_for_a_user_list_ip_access_rules(self, client: Cloudflare) -> None:
        rule = client.users.firewalls.access_rules.rules.ip_access_rules_for_a_user_list_ip_access_rules()
        assert_matches_type(Optional[RuleIPAccessRulesForAUserListIPAccessRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_ip_access_rules_for_a_user_list_ip_access_rules_with_all_params(self, client: Cloudflare) -> None:
        rule = client.users.firewalls.access_rules.rules.ip_access_rules_for_a_user_list_ip_access_rules(
            direction="desc",
            egs_pagination={
                "json": {
                    "page": 1,
                    "per_page": 1,
                }
            },
            filters={
                "configuration_target": "ip",
                "configuration_value": "198.51.100.4",
                "match": "any",
                "mode": "challenge",
                "notes": "my note",
            },
            order="mode",
            page=1,
            per_page=20,
        )
        assert_matches_type(Optional[RuleIPAccessRulesForAUserListIPAccessRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_ip_access_rules_for_a_user_list_ip_access_rules(self, client: Cloudflare) -> None:
        response = client.users.firewalls.access_rules.rules.with_raw_response.ip_access_rules_for_a_user_list_ip_access_rules()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleIPAccessRulesForAUserListIPAccessRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_ip_access_rules_for_a_user_list_ip_access_rules(self, client: Cloudflare) -> None:
        with client.users.firewalls.access_rules.rules.with_streaming_response.ip_access_rules_for_a_user_list_ip_access_rules() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleIPAccessRulesForAUserListIPAccessRulesResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.users.firewalls.access_rules.rules.update(
            "92f17202ed8bd63d69a66b86a49a8f6b",
        )
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.users.firewalls.access_rules.rules.update(
            "92f17202ed8bd63d69a66b86a49a8f6b",
            mode="challenge",
            notes="This rule is enabled because of an event that occurred on date X.",
        )
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.firewalls.access_rules.rules.with_raw_response.update(
            "92f17202ed8bd63d69a66b86a49a8f6b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.users.firewalls.access_rules.rules.with_streaming_response.update(
            "92f17202ed8bd63d69a66b86a49a8f6b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.users.firewalls.access_rules.rules.with_raw_response.update(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.users.firewalls.access_rules.rules.delete(
            "92f17202ed8bd63d69a66b86a49a8f6b",
        )
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.firewalls.access_rules.rules.with_raw_response.delete(
            "92f17202ed8bd63d69a66b86a49a8f6b",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.users.firewalls.access_rules.rules.with_streaming_response.delete(
            "92f17202ed8bd63d69a66b86a49a8f6b",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.users.firewalls.access_rules.rules.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_ip_access_rules_for_a_user_create_an_ip_access_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        rule = (
            await async_client.users.firewalls.access_rules.rules.ip_access_rules_for_a_user_create_an_ip_access_rule(
                configuration={},
                mode="challenge",
            )
        )
        assert_matches_type(Optional[RuleIPAccessRulesForAUserCreateAnIPAccessRuleResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_ip_access_rules_for_a_user_create_an_ip_access_rule_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        rule = (
            await async_client.users.firewalls.access_rules.rules.ip_access_rules_for_a_user_create_an_ip_access_rule(
                configuration={
                    "target": "ip",
                    "value": "198.51.100.4",
                },
                mode="challenge",
                notes="This rule is enabled because of an event that occurred on date X.",
            )
        )
        assert_matches_type(Optional[RuleIPAccessRulesForAUserCreateAnIPAccessRuleResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_ip_access_rules_for_a_user_create_an_ip_access_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.users.firewalls.access_rules.rules.with_raw_response.ip_access_rules_for_a_user_create_an_ip_access_rule(
            configuration={},
            mode="challenge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleIPAccessRulesForAUserCreateAnIPAccessRuleResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_ip_access_rules_for_a_user_create_an_ip_access_rule(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.users.firewalls.access_rules.rules.with_streaming_response.ip_access_rules_for_a_user_create_an_ip_access_rule(
            configuration={},
            mode="challenge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(
                Optional[RuleIPAccessRulesForAUserCreateAnIPAccessRuleResponse], rule, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_ip_access_rules_for_a_user_list_ip_access_rules(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.users.firewalls.access_rules.rules.ip_access_rules_for_a_user_list_ip_access_rules()
        assert_matches_type(Optional[RuleIPAccessRulesForAUserListIPAccessRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_ip_access_rules_for_a_user_list_ip_access_rules_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        rule = await async_client.users.firewalls.access_rules.rules.ip_access_rules_for_a_user_list_ip_access_rules(
            direction="desc",
            egs_pagination={
                "json": {
                    "page": 1,
                    "per_page": 1,
                }
            },
            filters={
                "configuration_target": "ip",
                "configuration_value": "198.51.100.4",
                "match": "any",
                "mode": "challenge",
                "notes": "my note",
            },
            order="mode",
            page=1,
            per_page=20,
        )
        assert_matches_type(Optional[RuleIPAccessRulesForAUserListIPAccessRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_ip_access_rules_for_a_user_list_ip_access_rules(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.users.firewalls.access_rules.rules.with_raw_response.ip_access_rules_for_a_user_list_ip_access_rules()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleIPAccessRulesForAUserListIPAccessRulesResponse], rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_ip_access_rules_for_a_user_list_ip_access_rules(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.users.firewalls.access_rules.rules.with_streaming_response.ip_access_rules_for_a_user_list_ip_access_rules() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleIPAccessRulesForAUserListIPAccessRulesResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True
