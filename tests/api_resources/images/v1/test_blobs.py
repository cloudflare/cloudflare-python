# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from cloudflare import Cloudflare, AsyncCloudflare
from cloudflare._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBlobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/023e105f4ecef8ad9ca31a8372d0c353/images/v1/image_id/blob").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        blob = client.images.v1.blobs.get(
            image_id="image_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert blob.is_closed
        assert blob.json() == {"foo": "bar"}
        assert cast(Any, blob.is_closed) is True
        assert isinstance(blob, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/023e105f4ecef8ad9ca31a8372d0c353/images/v1/image_id/blob").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        blob = client.images.v1.blobs.with_raw_response.get(
            image_id="image_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert blob.is_closed is True
        assert blob.http_request.headers.get("X-Stainless-Lang") == "python"
        assert blob.json() == {"foo": "bar"}
        assert isinstance(blob, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/023e105f4ecef8ad9ca31a8372d0c353/images/v1/image_id/blob").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.images.v1.blobs.with_streaming_response.get(
            image_id="image_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as blob:
            assert not blob.is_closed
            assert blob.http_request.headers.get("X-Stainless-Lang") == "python"

            assert blob.json() == {"foo": "bar"}
            assert cast(Any, blob.is_closed) is True
            assert isinstance(blob, StreamedBinaryAPIResponse)

        assert cast(Any, blob.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v1.blobs.with_raw_response.get(
                image_id="image_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `image_id` but received ''"):
            client.images.v1.blobs.with_raw_response.get(
                image_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncBlobs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/023e105f4ecef8ad9ca31a8372d0c353/images/v1/image_id/blob").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        blob = await async_client.images.v1.blobs.get(
            image_id="image_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert blob.is_closed
        assert await blob.json() == {"foo": "bar"}
        assert cast(Any, blob.is_closed) is True
        assert isinstance(blob, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/023e105f4ecef8ad9ca31a8372d0c353/images/v1/image_id/blob").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        blob = await async_client.images.v1.blobs.with_raw_response.get(
            image_id="image_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert blob.is_closed is True
        assert blob.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await blob.json() == {"foo": "bar"}
        assert isinstance(blob, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/023e105f4ecef8ad9ca31a8372d0c353/images/v1/image_id/blob").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.images.v1.blobs.with_streaming_response.get(
            image_id="image_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as blob:
            assert not blob.is_closed
            assert blob.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await blob.json() == {"foo": "bar"}
            assert cast(Any, blob.is_closed) is True
            assert isinstance(blob, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, blob.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v1.blobs.with_raw_response.get(
                image_id="image_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `image_id` but received ''"):
            await async_client.images.v1.blobs.with_raw_response.get(
                image_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
