# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.access.logs.scim import UpdateListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUpdates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        update = client.zero_trust.access.logs.scim.updates.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            idp_id=["df7e2w5f-02b7-4d9d-af26-8d1988fca630", "0194ae2c-efcf-7cfb-8884-055f1a161fa5"],
        )
        assert_matches_type(SyncSinglePage[UpdateListResponse], update, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        update = client.zero_trust.access.logs.scim.updates.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            idp_id=["df7e2w5f-02b7-4d9d-af26-8d1988fca630", "0194ae2c-efcf-7cfb-8884-055f1a161fa5"],
            cf_resource_id="bd97ef8d-7986-43e3-9ee0-c25dda33e4b0",
            direction="desc",
            idp_resource_id="idp_resource_id",
            limit=10,
            request_method=["DELETE", "PATCH"],
            resource_group_name="ALL_EMPLOYEES",
            resource_type=["USER", "GROUP"],
            resource_user_email="john.smith@example.com",
            since=parse_datetime("2025-01-01T00:00:00Z"),
            status=["FAILURE", "SUCCESS"],
            until=parse_datetime("2025-01-02T00:00:00Z"),
        )
        assert_matches_type(SyncSinglePage[UpdateListResponse], update, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.logs.scim.updates.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            idp_id=["df7e2w5f-02b7-4d9d-af26-8d1988fca630", "0194ae2c-efcf-7cfb-8884-055f1a161fa5"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        update = response.parse()
        assert_matches_type(SyncSinglePage[UpdateListResponse], update, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.access.logs.scim.updates.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            idp_id=["df7e2w5f-02b7-4d9d-af26-8d1988fca630", "0194ae2c-efcf-7cfb-8884-055f1a161fa5"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            update = response.parse()
            assert_matches_type(SyncSinglePage[UpdateListResponse], update, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.logs.scim.updates.with_raw_response.list(
                account_id="",
                idp_id=["df7e2w5f-02b7-4d9d-af26-8d1988fca630", "0194ae2c-efcf-7cfb-8884-055f1a161fa5"],
            )


class TestAsyncUpdates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        update = await async_client.zero_trust.access.logs.scim.updates.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            idp_id=["df7e2w5f-02b7-4d9d-af26-8d1988fca630", "0194ae2c-efcf-7cfb-8884-055f1a161fa5"],
        )
        assert_matches_type(AsyncSinglePage[UpdateListResponse], update, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        update = await async_client.zero_trust.access.logs.scim.updates.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            idp_id=["df7e2w5f-02b7-4d9d-af26-8d1988fca630", "0194ae2c-efcf-7cfb-8884-055f1a161fa5"],
            cf_resource_id="bd97ef8d-7986-43e3-9ee0-c25dda33e4b0",
            direction="desc",
            idp_resource_id="idp_resource_id",
            limit=10,
            request_method=["DELETE", "PATCH"],
            resource_group_name="ALL_EMPLOYEES",
            resource_type=["USER", "GROUP"],
            resource_user_email="john.smith@example.com",
            since=parse_datetime("2025-01-01T00:00:00Z"),
            status=["FAILURE", "SUCCESS"],
            until=parse_datetime("2025-01-02T00:00:00Z"),
        )
        assert_matches_type(AsyncSinglePage[UpdateListResponse], update, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.logs.scim.updates.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            idp_id=["df7e2w5f-02b7-4d9d-af26-8d1988fca630", "0194ae2c-efcf-7cfb-8884-055f1a161fa5"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        update = await response.parse()
        assert_matches_type(AsyncSinglePage[UpdateListResponse], update, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.logs.scim.updates.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            idp_id=["df7e2w5f-02b7-4d9d-af26-8d1988fca630", "0194ae2c-efcf-7cfb-8884-055f1a161fa5"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            update = await response.parse()
            assert_matches_type(AsyncSinglePage[UpdateListResponse], update, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.logs.scim.updates.with_raw_response.list(
                account_id="",
                idp_id=["df7e2w5f-02b7-4d9d-af26-8d1988fca630", "0194ae2c-efcf-7cfb-8884-055f1a161fa5"],
            )
