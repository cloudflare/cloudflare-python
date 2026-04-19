# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePagination, AsyncV4PagePagination
from cloudflare.types.zero_trust.dex import (
    RuleGetResponse,
    RuleListResponse,
    RuleCreateResponse,
    RuleDeleteResponse,
    RuleUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        rule = client.zero_trust.dex.rules.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            match="match",
            name="name",
        )
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        rule = client.zero_trust.dex.rules.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            match="match",
            name="name",
            description="description",
        )
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.dex.rules.with_raw_response.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            match="match",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.dex.rules.with_streaming_response.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            match="match",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dex.rules.with_raw_response.create(
                account_id="",
                match="match",
                name="name",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        rule = client.zero_trust.dex.rules.update(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        rule = client.zero_trust.dex.rules.update(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            description="description",
            match="match",
            name="name",
        )
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.dex.rules.with_raw_response.update(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.dex.rules.with_streaming_response.update(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dex.rules.with_raw_response.update(
                rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.zero_trust.dex.rules.with_raw_response.update(
                rule_id="",
                account_id="01a7362d577a6c3019a474fd6f485823",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        rule = client.zero_trust.dex.rules.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            page=1,
            per_page=1,
        )
        assert_matches_type(SyncV4PagePagination[Optional[RuleListResponse]], rule, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        rule = client.zero_trust.dex.rules.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            page=1,
            per_page=1,
            name="name",
            sort_by="name",
            sort_order="ASC",
        )
        assert_matches_type(SyncV4PagePagination[Optional[RuleListResponse]], rule, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.dex.rules.with_raw_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            page=1,
            per_page=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(SyncV4PagePagination[Optional[RuleListResponse]], rule, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.dex.rules.with_streaming_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            page=1,
            per_page=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(SyncV4PagePagination[Optional[RuleListResponse]], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dex.rules.with_raw_response.list(
                account_id="",
                page=1,
                per_page=1,
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        rule = client.zero_trust.dex.rules.delete(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.dex.rules.with_raw_response.delete(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.dex.rules.with_streaming_response.delete(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dex.rules.with_raw_response.delete(
                rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.zero_trust.dex.rules.with_raw_response.delete(
                rule_id="",
                account_id="01a7362d577a6c3019a474fd6f485823",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        rule = client.zero_trust.dex.rules.get(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(Optional[RuleGetResponse], rule, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.dex.rules.with_raw_response.get(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = response.parse()
        assert_matches_type(Optional[RuleGetResponse], rule, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.dex.rules.with_streaming_response.get(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = response.parse()
            assert_matches_type(Optional[RuleGetResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dex.rules.with_raw_response.get(
                rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.zero_trust.dex.rules.with_raw_response.get(
                rule_id="",
                account_id="01a7362d577a6c3019a474fd6f485823",
            )


class TestAsyncRules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.zero_trust.dex.rules.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            match="match",
            name="name",
        )
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.zero_trust.dex.rules.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            match="match",
            name="name",
            description="description",
        )
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dex.rules.with_raw_response.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            match="match",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dex.rules.with_streaming_response.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            match="match",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleCreateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dex.rules.with_raw_response.create(
                account_id="",
                match="match",
                name="name",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.zero_trust.dex.rules.update(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.zero_trust.dex.rules.update(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
            description="description",
            match="match",
            name="name",
        )
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dex.rules.with_raw_response.update(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dex.rules.with_streaming_response.update(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleUpdateResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dex.rules.with_raw_response.update(
                rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.zero_trust.dex.rules.with_raw_response.update(
                rule_id="",
                account_id="01a7362d577a6c3019a474fd6f485823",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.zero_trust.dex.rules.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            page=1,
            per_page=1,
        )
        assert_matches_type(AsyncV4PagePagination[Optional[RuleListResponse]], rule, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.zero_trust.dex.rules.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            page=1,
            per_page=1,
            name="name",
            sort_by="name",
            sort_order="ASC",
        )
        assert_matches_type(AsyncV4PagePagination[Optional[RuleListResponse]], rule, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dex.rules.with_raw_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            page=1,
            per_page=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(AsyncV4PagePagination[Optional[RuleListResponse]], rule, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dex.rules.with_streaming_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            page=1,
            per_page=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(AsyncV4PagePagination[Optional[RuleListResponse]], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dex.rules.with_raw_response.list(
                account_id="",
                page=1,
                per_page=1,
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.zero_trust.dex.rules.delete(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dex.rules.with_raw_response.delete(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dex.rules.with_streaming_response.delete(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleDeleteResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dex.rules.with_raw_response.delete(
                rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.zero_trust.dex.rules.with_raw_response.delete(
                rule_id="",
                account_id="01a7362d577a6c3019a474fd6f485823",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        rule = await async_client.zero_trust.dex.rules.get(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(Optional[RuleGetResponse], rule, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dex.rules.with_raw_response.get(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rule = await response.parse()
        assert_matches_type(Optional[RuleGetResponse], rule, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dex.rules.with_streaming_response.get(
            rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rule = await response.parse()
            assert_matches_type(Optional[RuleGetResponse], rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dex.rules.with_raw_response.get(
                rule_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.zero_trust.dex.rules.with_raw_response.get(
                rule_id="",
                account_id="01a7362d577a6c3019a474fd6f485823",
            )
