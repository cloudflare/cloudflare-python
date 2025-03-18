# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.magic_cloud_networking.catalog_syncs import (
    PrebuiltPolicyListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrebuiltPolicies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        prebuilt_policy = client.magic_cloud_networking.catalog_syncs.prebuilt_policies.list(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[PrebuiltPolicyListResponse], prebuilt_policy, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        prebuilt_policy = client.magic_cloud_networking.catalog_syncs.prebuilt_policies.list(
            account_id="account_id",
            destination_type="NONE",
        )
        assert_matches_type(SyncSinglePage[PrebuiltPolicyListResponse], prebuilt_policy, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.catalog_syncs.prebuilt_policies.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prebuilt_policy = response.parse()
        assert_matches_type(SyncSinglePage[PrebuiltPolicyListResponse], prebuilt_policy, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.catalog_syncs.prebuilt_policies.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prebuilt_policy = response.parse()
            assert_matches_type(SyncSinglePage[PrebuiltPolicyListResponse], prebuilt_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.catalog_syncs.prebuilt_policies.with_raw_response.list(
                account_id="",
            )


class TestAsyncPrebuiltPolicies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        prebuilt_policy = await async_client.magic_cloud_networking.catalog_syncs.prebuilt_policies.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[PrebuiltPolicyListResponse], prebuilt_policy, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        prebuilt_policy = await async_client.magic_cloud_networking.catalog_syncs.prebuilt_policies.list(
            account_id="account_id",
            destination_type="NONE",
        )
        assert_matches_type(AsyncSinglePage[PrebuiltPolicyListResponse], prebuilt_policy, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.catalog_syncs.prebuilt_policies.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prebuilt_policy = await response.parse()
        assert_matches_type(AsyncSinglePage[PrebuiltPolicyListResponse], prebuilt_policy, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.catalog_syncs.prebuilt_policies.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prebuilt_policy = await response.parse()
            assert_matches_type(AsyncSinglePage[PrebuiltPolicyListResponse], prebuilt_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.catalog_syncs.prebuilt_policies.with_raw_response.list(
                account_id="",
            )
