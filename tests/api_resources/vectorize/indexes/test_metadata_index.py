# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.vectorize.indexes import (
    MetadataIndexListResponse,
    MetadataIndexCreateResponse,
    MetadataIndexDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetadataIndex:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        metadata_index = client.vectorize.indexes.metadata_index.create(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            index_type="string",
            property_name="random_metadata_property",
        )
        assert_matches_type(Optional[MetadataIndexCreateResponse], metadata_index, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.vectorize.indexes.metadata_index.with_raw_response.create(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            index_type="string",
            property_name="random_metadata_property",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata_index = response.parse()
        assert_matches_type(Optional[MetadataIndexCreateResponse], metadata_index, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.vectorize.indexes.metadata_index.with_streaming_response.create(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            index_type="string",
            property_name="random_metadata_property",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata_index = response.parse()
            assert_matches_type(Optional[MetadataIndexCreateResponse], metadata_index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.vectorize.indexes.metadata_index.with_raw_response.create(
                index_name="example-index",
                account_id="",
                index_type="string",
                property_name="random_metadata_property",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            client.vectorize.indexes.metadata_index.with_raw_response.create(
                index_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                index_type="string",
                property_name="random_metadata_property",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        metadata_index = client.vectorize.indexes.metadata_index.list(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[MetadataIndexListResponse], metadata_index, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.vectorize.indexes.metadata_index.with_raw_response.list(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata_index = response.parse()
        assert_matches_type(Optional[MetadataIndexListResponse], metadata_index, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.vectorize.indexes.metadata_index.with_streaming_response.list(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata_index = response.parse()
            assert_matches_type(Optional[MetadataIndexListResponse], metadata_index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.vectorize.indexes.metadata_index.with_raw_response.list(
                index_name="example-index",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            client.vectorize.indexes.metadata_index.with_raw_response.list(
                index_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        metadata_index = client.vectorize.indexes.metadata_index.delete(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            property_name="random_metadata_property",
        )
        assert_matches_type(Optional[MetadataIndexDeleteResponse], metadata_index, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.vectorize.indexes.metadata_index.with_raw_response.delete(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            property_name="random_metadata_property",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata_index = response.parse()
        assert_matches_type(Optional[MetadataIndexDeleteResponse], metadata_index, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.vectorize.indexes.metadata_index.with_streaming_response.delete(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            property_name="random_metadata_property",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata_index = response.parse()
            assert_matches_type(Optional[MetadataIndexDeleteResponse], metadata_index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.vectorize.indexes.metadata_index.with_raw_response.delete(
                index_name="example-index",
                account_id="",
                property_name="random_metadata_property",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            client.vectorize.indexes.metadata_index.with_raw_response.delete(
                index_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                property_name="random_metadata_property",
            )


class TestAsyncMetadataIndex:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        metadata_index = await async_client.vectorize.indexes.metadata_index.create(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            index_type="string",
            property_name="random_metadata_property",
        )
        assert_matches_type(Optional[MetadataIndexCreateResponse], metadata_index, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.vectorize.indexes.metadata_index.with_raw_response.create(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            index_type="string",
            property_name="random_metadata_property",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata_index = await response.parse()
        assert_matches_type(Optional[MetadataIndexCreateResponse], metadata_index, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.vectorize.indexes.metadata_index.with_streaming_response.create(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            index_type="string",
            property_name="random_metadata_property",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata_index = await response.parse()
            assert_matches_type(Optional[MetadataIndexCreateResponse], metadata_index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.vectorize.indexes.metadata_index.with_raw_response.create(
                index_name="example-index",
                account_id="",
                index_type="string",
                property_name="random_metadata_property",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            await async_client.vectorize.indexes.metadata_index.with_raw_response.create(
                index_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                index_type="string",
                property_name="random_metadata_property",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        metadata_index = await async_client.vectorize.indexes.metadata_index.list(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[MetadataIndexListResponse], metadata_index, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.vectorize.indexes.metadata_index.with_raw_response.list(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata_index = await response.parse()
        assert_matches_type(Optional[MetadataIndexListResponse], metadata_index, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.vectorize.indexes.metadata_index.with_streaming_response.list(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata_index = await response.parse()
            assert_matches_type(Optional[MetadataIndexListResponse], metadata_index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.vectorize.indexes.metadata_index.with_raw_response.list(
                index_name="example-index",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            await async_client.vectorize.indexes.metadata_index.with_raw_response.list(
                index_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        metadata_index = await async_client.vectorize.indexes.metadata_index.delete(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            property_name="random_metadata_property",
        )
        assert_matches_type(Optional[MetadataIndexDeleteResponse], metadata_index, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.vectorize.indexes.metadata_index.with_raw_response.delete(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            property_name="random_metadata_property",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata_index = await response.parse()
        assert_matches_type(Optional[MetadataIndexDeleteResponse], metadata_index, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.vectorize.indexes.metadata_index.with_streaming_response.delete(
            index_name="example-index",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            property_name="random_metadata_property",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata_index = await response.parse()
            assert_matches_type(Optional[MetadataIndexDeleteResponse], metadata_index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.vectorize.indexes.metadata_index.with_raw_response.delete(
                index_name="example-index",
                account_id="",
                property_name="random_metadata_property",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_name` but received ''"):
            await async_client.vectorize.indexes.metadata_index.with_raw_response.delete(
                index_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                property_name="random_metadata_property",
            )
