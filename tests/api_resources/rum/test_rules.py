# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.rum import (
    RUMRule,
    RuleListResponse,
    RuleDeleteResponse,
    RuleBulkCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        rule = client.rum.rules.create(
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RUMRule], rule, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        rule = client.rum.rules.create(
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="example.com",
            inclusive=True,
            is_paused=False,
            paths=["*"],
        )
        assert_matches_type(Optional[RUMRule], rule, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.rum.rules.with_raw_response.create(
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RUMRule], rule, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.rum.rules.with_streaming_response.create(
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RUMRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rum.rules.with_raw_response.create(
                ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rum.rules.with_raw_response.create(
                ruleset_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        rule = client.rum.rules.update(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(Optional[RUMRule], rule, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        rule = client.rum.rules.update(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            host="example.com",
            inclusive=True,
            is_paused=False,
            paths=["*"],
        )
        assert_matches_type(Optional[RUMRule], rule, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.rum.rules.with_raw_response.update(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RUMRule], rule, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.rum.rules.with_streaming_response.update(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RUMRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rum.rules.with_raw_response.update(
                rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rum.rules.with_raw_response.update(
                rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                ruleset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rum.rules.with_raw_response.update(
                rule_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        rule = client.rum.rules.list(
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RuleListResponse], rule, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.rum.rules.with_raw_response.list(
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleListResponse], rule, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.rum.rules.with_streaming_response.list(
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleListResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rum.rules.with_raw_response.list(
                ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rum.rules.with_raw_response.list(
                ruleset_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        rule = client.rum.rules.delete(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.rum.rules.with_raw_response.delete(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.rum.rules.with_streaming_response.delete(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rum.rules.with_raw_response.delete(
                rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rum.rules.with_raw_response.delete(
                rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                ruleset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.rum.rules.with_raw_response.delete(
                rule_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

    @parametrize
    def test_method_bulk_create(self, client: Cloudflare) -> None:
        rule = client.rum.rules.bulk_create(
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RuleBulkCreateResponse], rule, path=["response"])

    @parametrize
    def test_method_bulk_create_with_all_params(self, client: Cloudflare) -> None:
        rule = client.rum.rules.bulk_create(
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            delete_rules=["f174e90a-fafe-4643-bbbc-4a0ed4fc8415"],
            rules=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "host": "example.com",
                    "inclusive": True,
                    "is_paused": False,
                    "paths": ["*"],
                }
            ],
        )
        assert_matches_type(Optional[RuleBulkCreateResponse], rule, path=["response"])

    @parametrize
    def test_raw_response_bulk_create(self, client: Cloudflare) -> None:
        response = client.rum.rules.with_raw_response.bulk_create(
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleBulkCreateResponse], rule, path=["response"])

    @parametrize
    def test_streaming_response_bulk_create(self, client: Cloudflare) -> None:
        with client.rum.rules.with_streaming_response.bulk_create(
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleBulkCreateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rum.rules.with_raw_response.bulk_create(
                ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            client.rum.rules.with_raw_response.bulk_create(
                ruleset_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rum.rules.create(
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RUMRule], rule, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rum.rules.create(
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host="example.com",
            inclusive=True,
            is_paused=False,
            paths=["*"],
        )
        assert_matches_type(Optional[RUMRule], rule, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rum.rules.with_raw_response.create(
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RUMRule], rule, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rum.rules.with_streaming_response.create(
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RUMRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rum.rules.with_raw_response.create(
                ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rum.rules.with_raw_response.create(
                ruleset_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rum.rules.update(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(Optional[RUMRule], rule, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rum.rules.update(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            host="example.com",
            inclusive=True,
            is_paused=False,
            paths=["*"],
        )
        assert_matches_type(Optional[RUMRule], rule, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rum.rules.with_raw_response.update(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RUMRule], rule, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rum.rules.with_streaming_response.update(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RUMRule], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rum.rules.with_raw_response.update(
                rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rum.rules.with_raw_response.update(
                rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                ruleset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rum.rules.with_raw_response.update(
                rule_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rum.rules.list(
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RuleListResponse], rule, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rum.rules.with_raw_response.list(
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleListResponse], rule, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rum.rules.with_streaming_response.list(
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleListResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rum.rules.with_raw_response.list(
                ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rum.rules.with_raw_response.list(
                ruleset_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rum.rules.delete(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rum.rules.with_raw_response.delete(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rum.rules.with_streaming_response.delete(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rum.rules.with_raw_response.delete(
                rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rum.rules.with_raw_response.delete(
                rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                ruleset_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.rum.rules.with_raw_response.delete(
                rule_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            )

    @parametrize
    async def test_method_bulk_create(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rum.rules.bulk_create(
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RuleBulkCreateResponse], rule, path=["response"])

    @parametrize
    async def test_method_bulk_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.rum.rules.bulk_create(
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            delete_rules=["f174e90a-fafe-4643-bbbc-4a0ed4fc8415"],
            rules=[
                {
                    "id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                    "host": "example.com",
                    "inclusive": True,
                    "is_paused": False,
                    "paths": ["*"],
                }
            ],
        )
        assert_matches_type(Optional[RuleBulkCreateResponse], rule, path=["response"])

    @parametrize
    async def test_raw_response_bulk_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rum.rules.with_raw_response.bulk_create(
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleBulkCreateResponse], rule, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rum.rules.with_streaming_response.bulk_create(
            ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleBulkCreateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rum.rules.with_raw_response.bulk_create(
                ruleset_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ruleset_id` but received ''"):
            await async_client.rum.rules.with_raw_response.bulk_create(
                ruleset_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
