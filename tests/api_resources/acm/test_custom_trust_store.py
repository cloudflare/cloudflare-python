# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.acm import (
    CustomTrustStore,
    CustomTrustStoreDeleteResponse,
)
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomTrustStore:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        custom_trust_store = client.acm.custom_trust_store.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate="-----BEGIN CERTIFICATE-----\nMIIDdjCCAl6gAwIBAgIJAPnMg0Fs+/B0MA0GCSqGSIb3DQEBCwUAMFsx...\n-----END CERTIFICATE-----\n",
        )
        assert_matches_type(Optional[CustomTrustStore], custom_trust_store, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.acm.custom_trust_store.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate="-----BEGIN CERTIFICATE-----\nMIIDdjCCAl6gAwIBAgIJAPnMg0Fs+/B0MA0GCSqGSIb3DQEBCwUAMFsx...\n-----END CERTIFICATE-----\n",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_trust_store = response.parse()
        assert_matches_type(Optional[CustomTrustStore], custom_trust_store, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.acm.custom_trust_store.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate="-----BEGIN CERTIFICATE-----\nMIIDdjCCAl6gAwIBAgIJAPnMg0Fs+/B0MA0GCSqGSIb3DQEBCwUAMFsx...\n-----END CERTIFICATE-----\n",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_trust_store = response.parse()
            assert_matches_type(Optional[CustomTrustStore], custom_trust_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.acm.custom_trust_store.with_raw_response.create(
                zone_id="",
                certificate="-----BEGIN CERTIFICATE-----\nMIIDdjCCAl6gAwIBAgIJAPnMg0Fs+/B0MA0GCSqGSIb3DQEBCwUAMFsx...\n-----END CERTIFICATE-----\n",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        custom_trust_store = client.acm.custom_trust_store.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[CustomTrustStore], custom_trust_store, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        custom_trust_store = client.acm.custom_trust_store.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            limit=10,
            offset=10,
            page=1,
            per_page=5,
        )
        assert_matches_type(SyncV4PagePaginationArray[CustomTrustStore], custom_trust_store, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.acm.custom_trust_store.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_trust_store = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[CustomTrustStore], custom_trust_store, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.acm.custom_trust_store.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_trust_store = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[CustomTrustStore], custom_trust_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.acm.custom_trust_store.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        custom_trust_store = client.acm.custom_trust_store.delete(
            custom_origin_trust_store_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CustomTrustStoreDeleteResponse], custom_trust_store, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.acm.custom_trust_store.with_raw_response.delete(
            custom_origin_trust_store_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_trust_store = response.parse()
        assert_matches_type(Optional[CustomTrustStoreDeleteResponse], custom_trust_store, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.acm.custom_trust_store.with_streaming_response.delete(
            custom_origin_trust_store_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_trust_store = response.parse()
            assert_matches_type(Optional[CustomTrustStoreDeleteResponse], custom_trust_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.acm.custom_trust_store.with_raw_response.delete(
                custom_origin_trust_store_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `custom_origin_trust_store_id` but received ''"
        ):
            client.acm.custom_trust_store.with_raw_response.delete(
                custom_origin_trust_store_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        custom_trust_store = client.acm.custom_trust_store.get(
            custom_origin_trust_store_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CustomTrustStore], custom_trust_store, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.acm.custom_trust_store.with_raw_response.get(
            custom_origin_trust_store_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_trust_store = response.parse()
        assert_matches_type(Optional[CustomTrustStore], custom_trust_store, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.acm.custom_trust_store.with_streaming_response.get(
            custom_origin_trust_store_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_trust_store = response.parse()
            assert_matches_type(Optional[CustomTrustStore], custom_trust_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.acm.custom_trust_store.with_raw_response.get(
                custom_origin_trust_store_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `custom_origin_trust_store_id` but received ''"
        ):
            client.acm.custom_trust_store.with_raw_response.get(
                custom_origin_trust_store_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncCustomTrustStore:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        custom_trust_store = await async_client.acm.custom_trust_store.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate="-----BEGIN CERTIFICATE-----\nMIIDdjCCAl6gAwIBAgIJAPnMg0Fs+/B0MA0GCSqGSIb3DQEBCwUAMFsx...\n-----END CERTIFICATE-----\n",
        )
        assert_matches_type(Optional[CustomTrustStore], custom_trust_store, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.acm.custom_trust_store.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate="-----BEGIN CERTIFICATE-----\nMIIDdjCCAl6gAwIBAgIJAPnMg0Fs+/B0MA0GCSqGSIb3DQEBCwUAMFsx...\n-----END CERTIFICATE-----\n",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_trust_store = await response.parse()
        assert_matches_type(Optional[CustomTrustStore], custom_trust_store, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.acm.custom_trust_store.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate="-----BEGIN CERTIFICATE-----\nMIIDdjCCAl6gAwIBAgIJAPnMg0Fs+/B0MA0GCSqGSIb3DQEBCwUAMFsx...\n-----END CERTIFICATE-----\n",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_trust_store = await response.parse()
            assert_matches_type(Optional[CustomTrustStore], custom_trust_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.acm.custom_trust_store.with_raw_response.create(
                zone_id="",
                certificate="-----BEGIN CERTIFICATE-----\nMIIDdjCCAl6gAwIBAgIJAPnMg0Fs+/B0MA0GCSqGSIb3DQEBCwUAMFsx...\n-----END CERTIFICATE-----\n",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        custom_trust_store = await async_client.acm.custom_trust_store.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[CustomTrustStore], custom_trust_store, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom_trust_store = await async_client.acm.custom_trust_store.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            limit=10,
            offset=10,
            page=1,
            per_page=5,
        )
        assert_matches_type(AsyncV4PagePaginationArray[CustomTrustStore], custom_trust_store, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.acm.custom_trust_store.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_trust_store = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[CustomTrustStore], custom_trust_store, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.acm.custom_trust_store.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_trust_store = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[CustomTrustStore], custom_trust_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.acm.custom_trust_store.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        custom_trust_store = await async_client.acm.custom_trust_store.delete(
            custom_origin_trust_store_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CustomTrustStoreDeleteResponse], custom_trust_store, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.acm.custom_trust_store.with_raw_response.delete(
            custom_origin_trust_store_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_trust_store = await response.parse()
        assert_matches_type(Optional[CustomTrustStoreDeleteResponse], custom_trust_store, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.acm.custom_trust_store.with_streaming_response.delete(
            custom_origin_trust_store_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_trust_store = await response.parse()
            assert_matches_type(Optional[CustomTrustStoreDeleteResponse], custom_trust_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.acm.custom_trust_store.with_raw_response.delete(
                custom_origin_trust_store_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `custom_origin_trust_store_id` but received ''"
        ):
            await async_client.acm.custom_trust_store.with_raw_response.delete(
                custom_origin_trust_store_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        custom_trust_store = await async_client.acm.custom_trust_store.get(
            custom_origin_trust_store_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[CustomTrustStore], custom_trust_store, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.acm.custom_trust_store.with_raw_response.get(
            custom_origin_trust_store_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_trust_store = await response.parse()
        assert_matches_type(Optional[CustomTrustStore], custom_trust_store, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.acm.custom_trust_store.with_streaming_response.get(
            custom_origin_trust_store_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_trust_store = await response.parse()
            assert_matches_type(Optional[CustomTrustStore], custom_trust_store, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.acm.custom_trust_store.with_raw_response.get(
                custom_origin_trust_store_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `custom_origin_trust_store_id` but received ''"
        ):
            await async_client.acm.custom_trust_store.with_raw_response.get(
                custom_origin_trust_store_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
