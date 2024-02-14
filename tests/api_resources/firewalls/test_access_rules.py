# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.firewalls import (
    AccessRuleCreateResponse,
    AccessRuleUpdateResponse,
    AccessRuleListResponse,
    AccessRuleDeleteResponse,
    AccessRuleGetResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.firewalls import access_rule_create_params
from cloudflare.types.firewalls import access_rule_update_params
from cloudflare.types.firewalls import access_rule_list_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccessRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        access_rule = client.firewalls.access_rules.create(
            {},
            account_or_zone="string",
            configuration={},
            mode="challenge",
        )
        assert_matches_type(Optional[AccessRuleCreateResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        access_rule = client.firewalls.access_rules.create(
            {},
            account_or_zone="string",
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            mode="challenge",
            notes="This rule is enabled because of an event that occurred on date X.",
        )
        assert_matches_type(Optional[AccessRuleCreateResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.firewalls.access_rules.with_raw_response.create(
            {},
            account_or_zone="string",
            configuration={},
            mode="challenge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = response.parse()
        assert_matches_type(Optional[AccessRuleCreateResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.firewalls.access_rules.with_streaming_response.create(
            {},
            account_or_zone="string",
            configuration={},
            mode="challenge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = response.parse()
            assert_matches_type(Optional[AccessRuleCreateResponse], access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.firewalls.access_rules.with_raw_response.create(
                {},
                account_or_zone="",
                configuration={},
                mode="challenge",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        access_rule = client.firewalls.access_rules.update(
            {},
            account_identifier={},
            configuration={},
            mode="challenge",
        )
        assert_matches_type(Optional[AccessRuleUpdateResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        access_rule = client.firewalls.access_rules.update(
            {},
            account_identifier={},
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            mode="challenge",
            notes="This rule is enabled because of an event that occurred on date X.",
        )
        assert_matches_type(Optional[AccessRuleUpdateResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.firewalls.access_rules.with_raw_response.update(
            {},
            account_identifier={},
            configuration={},
            mode="challenge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = response.parse()
        assert_matches_type(Optional[AccessRuleUpdateResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.firewalls.access_rules.with_streaming_response.update(
            {},
            account_identifier={},
            configuration={},
            mode="challenge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = response.parse()
            assert_matches_type(Optional[AccessRuleUpdateResponse], access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        access_rule = client.firewalls.access_rules.list(
            {},
            account_or_zone="string",
        )
        assert_matches_type(Optional[AccessRuleListResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        access_rule = client.firewalls.access_rules.list(
            {},
            account_or_zone="string",
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
        assert_matches_type(Optional[AccessRuleListResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.firewalls.access_rules.with_raw_response.list(
            {},
            account_or_zone="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = response.parse()
        assert_matches_type(Optional[AccessRuleListResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.firewalls.access_rules.with_streaming_response.list(
            {},
            account_or_zone="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = response.parse()
            assert_matches_type(Optional[AccessRuleListResponse], access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.firewalls.access_rules.with_raw_response.list(
                {},
                account_or_zone="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        access_rule = client.firewalls.access_rules.delete(
            {},
            account_or_zone="string",
            account_or_zone_id={},
        )
        assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.firewalls.access_rules.with_raw_response.delete(
            {},
            account_or_zone="string",
            account_or_zone_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = response.parse()
        assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.firewalls.access_rules.with_streaming_response.delete(
            {},
            account_or_zone="string",
            account_or_zone_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = response.parse()
            assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.firewalls.access_rules.with_raw_response.delete(
                {},
                account_or_zone="",
                account_or_zone_id={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        access_rule = client.firewalls.access_rules.get(
            {},
            account_or_zone="string",
            account_or_zone_id={},
        )
        assert_matches_type(Optional[AccessRuleGetResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.firewalls.access_rules.with_raw_response.get(
            {},
            account_or_zone="string",
            account_or_zone_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = response.parse()
        assert_matches_type(Optional[AccessRuleGetResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.firewalls.access_rules.with_streaming_response.get(
            {},
            account_or_zone="string",
            account_or_zone_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = response.parse()
            assert_matches_type(Optional[AccessRuleGetResponse], access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.firewalls.access_rules.with_raw_response.get(
                {},
                account_or_zone="",
                account_or_zone_id={},
            )


class TestAsyncAccessRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.firewalls.access_rules.create(
            {},
            account_or_zone="string",
            configuration={},
            mode="challenge",
        )
        assert_matches_type(Optional[AccessRuleCreateResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.firewalls.access_rules.create(
            {},
            account_or_zone="string",
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            mode="challenge",
            notes="This rule is enabled because of an event that occurred on date X.",
        )
        assert_matches_type(Optional[AccessRuleCreateResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.access_rules.with_raw_response.create(
            {},
            account_or_zone="string",
            configuration={},
            mode="challenge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = await response.parse()
        assert_matches_type(Optional[AccessRuleCreateResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.access_rules.with_streaming_response.create(
            {},
            account_or_zone="string",
            configuration={},
            mode="challenge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = await response.parse()
            assert_matches_type(Optional[AccessRuleCreateResponse], access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.firewalls.access_rules.with_raw_response.create(
                {},
                account_or_zone="",
                configuration={},
                mode="challenge",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.firewalls.access_rules.update(
            {},
            account_identifier={},
            configuration={},
            mode="challenge",
        )
        assert_matches_type(Optional[AccessRuleUpdateResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.firewalls.access_rules.update(
            {},
            account_identifier={},
            configuration={
                "target": "ip",
                "value": "198.51.100.4",
            },
            mode="challenge",
            notes="This rule is enabled because of an event that occurred on date X.",
        )
        assert_matches_type(Optional[AccessRuleUpdateResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.access_rules.with_raw_response.update(
            {},
            account_identifier={},
            configuration={},
            mode="challenge",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = await response.parse()
        assert_matches_type(Optional[AccessRuleUpdateResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.access_rules.with_streaming_response.update(
            {},
            account_identifier={},
            configuration={},
            mode="challenge",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = await response.parse()
            assert_matches_type(Optional[AccessRuleUpdateResponse], access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.firewalls.access_rules.list(
            {},
            account_or_zone="string",
        )
        assert_matches_type(Optional[AccessRuleListResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.firewalls.access_rules.list(
            {},
            account_or_zone="string",
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
        assert_matches_type(Optional[AccessRuleListResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.access_rules.with_raw_response.list(
            {},
            account_or_zone="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = await response.parse()
        assert_matches_type(Optional[AccessRuleListResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.access_rules.with_streaming_response.list(
            {},
            account_or_zone="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = await response.parse()
            assert_matches_type(Optional[AccessRuleListResponse], access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.firewalls.access_rules.with_raw_response.list(
                {},
                account_or_zone="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.firewalls.access_rules.delete(
            {},
            account_or_zone="string",
            account_or_zone_id={},
        )
        assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.access_rules.with_raw_response.delete(
            {},
            account_or_zone="string",
            account_or_zone_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = await response.parse()
        assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.access_rules.with_streaming_response.delete(
            {},
            account_or_zone="string",
            account_or_zone_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = await response.parse()
            assert_matches_type(Optional[AccessRuleDeleteResponse], access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.firewalls.access_rules.with_raw_response.delete(
                {},
                account_or_zone="",
                account_or_zone_id={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        access_rule = await async_client.firewalls.access_rules.get(
            {},
            account_or_zone="string",
            account_or_zone_id={},
        )
        assert_matches_type(Optional[AccessRuleGetResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewalls.access_rules.with_raw_response.get(
            {},
            account_or_zone="string",
            account_or_zone_id={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_rule = await response.parse()
        assert_matches_type(Optional[AccessRuleGetResponse], access_rule, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewalls.access_rules.with_streaming_response.get(
            {},
            account_or_zone="string",
            account_or_zone_id={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_rule = await response.parse()
            assert_matches_type(Optional[AccessRuleGetResponse], access_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.firewalls.access_rules.with_raw_response.get(
                {},
                account_or_zone="",
                account_or_zone_id={},
            )
