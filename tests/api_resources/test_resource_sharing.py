# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.resource_sharing import (
    ResourceSharingGetResponse,
    ResourceSharingListResponse,
    ResourceSharingCreateResponse,
    ResourceSharingDeleteResponse,
    ResourceSharingUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResourceSharing:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        resource_sharing = client.resource_sharing.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My Shared WAF Managed Rule",
            recipients=[{}],
            resources=[
                {
                    "meta": {},
                    "resource_account_id": "023e105f4ecef8ad9ca31a8372d0c353",
                    "resource_id": "023e105f4ecef8ad9ca31a8372d0c353",
                    "resource_type": "custom-ruleset",
                }
            ],
        )
        assert_matches_type(Optional[ResourceSharingCreateResponse], resource_sharing, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.resource_sharing.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My Shared WAF Managed Rule",
            recipients=[{}],
            resources=[
                {
                    "meta": {},
                    "resource_account_id": "023e105f4ecef8ad9ca31a8372d0c353",
                    "resource_id": "023e105f4ecef8ad9ca31a8372d0c353",
                    "resource_type": "custom-ruleset",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_sharing = response.parse()
        assert_matches_type(Optional[ResourceSharingCreateResponse], resource_sharing, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.resource_sharing.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My Shared WAF Managed Rule",
            recipients=[{}],
            resources=[
                {
                    "meta": {},
                    "resource_account_id": "023e105f4ecef8ad9ca31a8372d0c353",
                    "resource_id": "023e105f4ecef8ad9ca31a8372d0c353",
                    "resource_type": "custom-ruleset",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_sharing = response.parse()
            assert_matches_type(Optional[ResourceSharingCreateResponse], resource_sharing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.resource_sharing.with_raw_response.create(
                account_id="",
                name="My Shared WAF Managed Rule",
                recipients=[{}],
                resources=[
                    {
                        "meta": {},
                        "resource_account_id": "023e105f4ecef8ad9ca31a8372d0c353",
                        "resource_id": "023e105f4ecef8ad9ca31a8372d0c353",
                        "resource_type": "custom-ruleset",
                    }
                ],
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        resource_sharing = client.resource_sharing.update(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My Shared WAF Managed Rule",
        )
        assert_matches_type(Optional[ResourceSharingUpdateResponse], resource_sharing, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.resource_sharing.with_raw_response.update(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My Shared WAF Managed Rule",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_sharing = response.parse()
        assert_matches_type(Optional[ResourceSharingUpdateResponse], resource_sharing, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.resource_sharing.with_streaming_response.update(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My Shared WAF Managed Rule",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_sharing = response.parse()
            assert_matches_type(Optional[ResourceSharingUpdateResponse], resource_sharing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.resource_sharing.with_raw_response.update(
                share_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="",
                name="My Shared WAF Managed Rule",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_id` but received ''"):
            client.resource_sharing.with_raw_response.update(
                share_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="My Shared WAF Managed Rule",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        resource_sharing = client.resource_sharing.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[ResourceSharingListResponse], resource_sharing, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        resource_sharing = client.resource_sharing.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            kind="sent",
            order="name",
            page=2,
            per_page=20,
            status="active",
            target_type="account",
        )
        assert_matches_type(SyncV4PagePaginationArray[ResourceSharingListResponse], resource_sharing, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.resource_sharing.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_sharing = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[ResourceSharingListResponse], resource_sharing, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.resource_sharing.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_sharing = response.parse()
            assert_matches_type(
                SyncV4PagePaginationArray[ResourceSharingListResponse], resource_sharing, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.resource_sharing.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        resource_sharing = client.resource_sharing.delete(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ResourceSharingDeleteResponse], resource_sharing, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.resource_sharing.with_raw_response.delete(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_sharing = response.parse()
        assert_matches_type(Optional[ResourceSharingDeleteResponse], resource_sharing, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.resource_sharing.with_streaming_response.delete(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_sharing = response.parse()
            assert_matches_type(Optional[ResourceSharingDeleteResponse], resource_sharing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.resource_sharing.with_raw_response.delete(
                share_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_id` but received ''"):
            client.resource_sharing.with_raw_response.delete(
                share_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        resource_sharing = client.resource_sharing.get(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ResourceSharingGetResponse], resource_sharing, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.resource_sharing.with_raw_response.get(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_sharing = response.parse()
        assert_matches_type(Optional[ResourceSharingGetResponse], resource_sharing, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.resource_sharing.with_streaming_response.get(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_sharing = response.parse()
            assert_matches_type(Optional[ResourceSharingGetResponse], resource_sharing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.resource_sharing.with_raw_response.get(
                share_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_id` but received ''"):
            client.resource_sharing.with_raw_response.get(
                share_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncResourceSharing:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        resource_sharing = await async_client.resource_sharing.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My Shared WAF Managed Rule",
            recipients=[{}],
            resources=[
                {
                    "meta": {},
                    "resource_account_id": "023e105f4ecef8ad9ca31a8372d0c353",
                    "resource_id": "023e105f4ecef8ad9ca31a8372d0c353",
                    "resource_type": "custom-ruleset",
                }
            ],
        )
        assert_matches_type(Optional[ResourceSharingCreateResponse], resource_sharing, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.resource_sharing.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My Shared WAF Managed Rule",
            recipients=[{}],
            resources=[
                {
                    "meta": {},
                    "resource_account_id": "023e105f4ecef8ad9ca31a8372d0c353",
                    "resource_id": "023e105f4ecef8ad9ca31a8372d0c353",
                    "resource_type": "custom-ruleset",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_sharing = await response.parse()
        assert_matches_type(Optional[ResourceSharingCreateResponse], resource_sharing, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.resource_sharing.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My Shared WAF Managed Rule",
            recipients=[{}],
            resources=[
                {
                    "meta": {},
                    "resource_account_id": "023e105f4ecef8ad9ca31a8372d0c353",
                    "resource_id": "023e105f4ecef8ad9ca31a8372d0c353",
                    "resource_type": "custom-ruleset",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_sharing = await response.parse()
            assert_matches_type(Optional[ResourceSharingCreateResponse], resource_sharing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.resource_sharing.with_raw_response.create(
                account_id="",
                name="My Shared WAF Managed Rule",
                recipients=[{}],
                resources=[
                    {
                        "meta": {},
                        "resource_account_id": "023e105f4ecef8ad9ca31a8372d0c353",
                        "resource_id": "023e105f4ecef8ad9ca31a8372d0c353",
                        "resource_type": "custom-ruleset",
                    }
                ],
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        resource_sharing = await async_client.resource_sharing.update(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My Shared WAF Managed Rule",
        )
        assert_matches_type(Optional[ResourceSharingUpdateResponse], resource_sharing, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.resource_sharing.with_raw_response.update(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My Shared WAF Managed Rule",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_sharing = await response.parse()
        assert_matches_type(Optional[ResourceSharingUpdateResponse], resource_sharing, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.resource_sharing.with_streaming_response.update(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="My Shared WAF Managed Rule",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_sharing = await response.parse()
            assert_matches_type(Optional[ResourceSharingUpdateResponse], resource_sharing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.resource_sharing.with_raw_response.update(
                share_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="",
                name="My Shared WAF Managed Rule",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_id` but received ''"):
            await async_client.resource_sharing.with_raw_response.update(
                share_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="My Shared WAF Managed Rule",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        resource_sharing = await async_client.resource_sharing.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            AsyncV4PagePaginationArray[ResourceSharingListResponse], resource_sharing, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        resource_sharing = await async_client.resource_sharing.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            kind="sent",
            order="name",
            page=2,
            per_page=20,
            status="active",
            target_type="account",
        )
        assert_matches_type(
            AsyncV4PagePaginationArray[ResourceSharingListResponse], resource_sharing, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.resource_sharing.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_sharing = await response.parse()
        assert_matches_type(
            AsyncV4PagePaginationArray[ResourceSharingListResponse], resource_sharing, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.resource_sharing.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_sharing = await response.parse()
            assert_matches_type(
                AsyncV4PagePaginationArray[ResourceSharingListResponse], resource_sharing, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.resource_sharing.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        resource_sharing = await async_client.resource_sharing.delete(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ResourceSharingDeleteResponse], resource_sharing, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.resource_sharing.with_raw_response.delete(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_sharing = await response.parse()
        assert_matches_type(Optional[ResourceSharingDeleteResponse], resource_sharing, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.resource_sharing.with_streaming_response.delete(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_sharing = await response.parse()
            assert_matches_type(Optional[ResourceSharingDeleteResponse], resource_sharing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.resource_sharing.with_raw_response.delete(
                share_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_id` but received ''"):
            await async_client.resource_sharing.with_raw_response.delete(
                share_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        resource_sharing = await async_client.resource_sharing.get(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ResourceSharingGetResponse], resource_sharing, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.resource_sharing.with_raw_response.get(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        resource_sharing = await response.parse()
        assert_matches_type(Optional[ResourceSharingGetResponse], resource_sharing, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.resource_sharing.with_streaming_response.get(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            resource_sharing = await response.parse()
            assert_matches_type(Optional[ResourceSharingGetResponse], resource_sharing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.resource_sharing.with_raw_response.get(
                share_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_id` but received ''"):
            await async_client.resource_sharing.with_raw_response.get(
                share_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
