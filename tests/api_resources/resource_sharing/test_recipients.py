# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.resource_sharing import (
    RecipientGetResponse,
    RecipientListResponse,
    RecipientCreateResponse,
    RecipientDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRecipients:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        recipient = client.resource_sharing.recipients.create(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            path_account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecipientCreateResponse], recipient, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        recipient = client.resource_sharing.recipients.create(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            path_account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body_account_id="023e105f4ecef8ad9ca31a8372d0c353",
            organization_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecipientCreateResponse], recipient, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.resource_sharing.recipients.with_raw_response.create(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            path_account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recipient = response.parse()
        assert_matches_type(Optional[RecipientCreateResponse], recipient, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.resource_sharing.recipients.with_streaming_response.create(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            path_account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recipient = response.parse()
            assert_matches_type(Optional[RecipientCreateResponse], recipient, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_account_id` but received ''"):
            client.resource_sharing.recipients.with_raw_response.create(
                share_id="3fd85f74b32742f1bff64a85009dda07",
                path_account_id="",
                body_account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_id` but received ''"):
            client.resource_sharing.recipients.with_raw_response.create(
                share_id="",
                path_account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        recipient = client.resource_sharing.recipients.list(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[RecipientListResponse], recipient, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        recipient = client.resource_sharing.recipients.list(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=2,
            per_page=20,
        )
        assert_matches_type(SyncV4PagePaginationArray[RecipientListResponse], recipient, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.resource_sharing.recipients.with_raw_response.list(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recipient = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[RecipientListResponse], recipient, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.resource_sharing.recipients.with_streaming_response.list(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recipient = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[RecipientListResponse], recipient, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.resource_sharing.recipients.with_raw_response.list(
                share_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_id` but received ''"):
            client.resource_sharing.recipients.with_raw_response.list(
                share_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        recipient = client.resource_sharing.recipients.delete(
            recipient_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            share_id="3fd85f74b32742f1bff64a85009dda07",
        )
        assert_matches_type(Optional[RecipientDeleteResponse], recipient, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.resource_sharing.recipients.with_raw_response.delete(
            recipient_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            share_id="3fd85f74b32742f1bff64a85009dda07",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recipient = response.parse()
        assert_matches_type(Optional[RecipientDeleteResponse], recipient, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.resource_sharing.recipients.with_streaming_response.delete(
            recipient_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            share_id="3fd85f74b32742f1bff64a85009dda07",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recipient = response.parse()
            assert_matches_type(Optional[RecipientDeleteResponse], recipient, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.resource_sharing.recipients.with_raw_response.delete(
                recipient_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="",
                share_id="3fd85f74b32742f1bff64a85009dda07",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_id` but received ''"):
            client.resource_sharing.recipients.with_raw_response.delete(
                recipient_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                share_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recipient_id` but received ''"):
            client.resource_sharing.recipients.with_raw_response.delete(
                recipient_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                share_id="3fd85f74b32742f1bff64a85009dda07",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        recipient = client.resource_sharing.recipients.get(
            recipient_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            share_id="3fd85f74b32742f1bff64a85009dda07",
        )
        assert_matches_type(Optional[RecipientGetResponse], recipient, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.resource_sharing.recipients.with_raw_response.get(
            recipient_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            share_id="3fd85f74b32742f1bff64a85009dda07",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recipient = response.parse()
        assert_matches_type(Optional[RecipientGetResponse], recipient, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.resource_sharing.recipients.with_streaming_response.get(
            recipient_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            share_id="3fd85f74b32742f1bff64a85009dda07",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recipient = response.parse()
            assert_matches_type(Optional[RecipientGetResponse], recipient, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.resource_sharing.recipients.with_raw_response.get(
                recipient_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="",
                share_id="3fd85f74b32742f1bff64a85009dda07",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_id` but received ''"):
            client.resource_sharing.recipients.with_raw_response.get(
                recipient_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                share_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recipient_id` but received ''"):
            client.resource_sharing.recipients.with_raw_response.get(
                recipient_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                share_id="3fd85f74b32742f1bff64a85009dda07",
            )


class TestAsyncRecipients:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        recipient = await async_client.resource_sharing.recipients.create(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            path_account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecipientCreateResponse], recipient, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        recipient = await async_client.resource_sharing.recipients.create(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            path_account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body_account_id="023e105f4ecef8ad9ca31a8372d0c353",
            organization_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[RecipientCreateResponse], recipient, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.resource_sharing.recipients.with_raw_response.create(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            path_account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recipient = await response.parse()
        assert_matches_type(Optional[RecipientCreateResponse], recipient, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.resource_sharing.recipients.with_streaming_response.create(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            path_account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recipient = await response.parse()
            assert_matches_type(Optional[RecipientCreateResponse], recipient, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_account_id` but received ''"):
            await async_client.resource_sharing.recipients.with_raw_response.create(
                share_id="3fd85f74b32742f1bff64a85009dda07",
                path_account_id="",
                body_account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_id` but received ''"):
            await async_client.resource_sharing.recipients.with_raw_response.create(
                share_id="",
                path_account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        recipient = await async_client.resource_sharing.recipients.list(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[RecipientListResponse], recipient, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        recipient = await async_client.resource_sharing.recipients.list(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=2,
            per_page=20,
        )
        assert_matches_type(AsyncV4PagePaginationArray[RecipientListResponse], recipient, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.resource_sharing.recipients.with_raw_response.list(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recipient = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[RecipientListResponse], recipient, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.resource_sharing.recipients.with_streaming_response.list(
            share_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recipient = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[RecipientListResponse], recipient, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.resource_sharing.recipients.with_raw_response.list(
                share_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_id` but received ''"):
            await async_client.resource_sharing.recipients.with_raw_response.list(
                share_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        recipient = await async_client.resource_sharing.recipients.delete(
            recipient_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            share_id="3fd85f74b32742f1bff64a85009dda07",
        )
        assert_matches_type(Optional[RecipientDeleteResponse], recipient, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.resource_sharing.recipients.with_raw_response.delete(
            recipient_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            share_id="3fd85f74b32742f1bff64a85009dda07",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recipient = await response.parse()
        assert_matches_type(Optional[RecipientDeleteResponse], recipient, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.resource_sharing.recipients.with_streaming_response.delete(
            recipient_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            share_id="3fd85f74b32742f1bff64a85009dda07",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recipient = await response.parse()
            assert_matches_type(Optional[RecipientDeleteResponse], recipient, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.resource_sharing.recipients.with_raw_response.delete(
                recipient_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="",
                share_id="3fd85f74b32742f1bff64a85009dda07",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_id` but received ''"):
            await async_client.resource_sharing.recipients.with_raw_response.delete(
                recipient_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                share_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recipient_id` but received ''"):
            await async_client.resource_sharing.recipients.with_raw_response.delete(
                recipient_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                share_id="3fd85f74b32742f1bff64a85009dda07",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        recipient = await async_client.resource_sharing.recipients.get(
            recipient_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            share_id="3fd85f74b32742f1bff64a85009dda07",
        )
        assert_matches_type(Optional[RecipientGetResponse], recipient, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.resource_sharing.recipients.with_raw_response.get(
            recipient_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            share_id="3fd85f74b32742f1bff64a85009dda07",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recipient = await response.parse()
        assert_matches_type(Optional[RecipientGetResponse], recipient, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.resource_sharing.recipients.with_streaming_response.get(
            recipient_id="3fd85f74b32742f1bff64a85009dda07",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            share_id="3fd85f74b32742f1bff64a85009dda07",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recipient = await response.parse()
            assert_matches_type(Optional[RecipientGetResponse], recipient, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.resource_sharing.recipients.with_raw_response.get(
                recipient_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="",
                share_id="3fd85f74b32742f1bff64a85009dda07",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_id` but received ''"):
            await async_client.resource_sharing.recipients.with_raw_response.get(
                recipient_id="3fd85f74b32742f1bff64a85009dda07",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                share_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recipient_id` but received ''"):
            await async_client.resource_sharing.recipients.with_raw_response.get(
                recipient_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                share_id="3fd85f74b32742f1bff64a85009dda07",
            )
