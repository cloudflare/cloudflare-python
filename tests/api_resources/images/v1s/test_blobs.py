# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, cast

from cloudflare._response import (
    BinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBlobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_cloudflare_images_base_image(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/023e105f4ecef8ad9ca31a8372d0c353/images/v1/string/blob").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        blob = client.images.v1s.blobs.cloudflare_images_base_image(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert blob.is_closed
        assert blob.json() == {"foo": "bar"}
        assert cast(Any, blob.is_closed) is True
        assert isinstance(blob, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_cloudflare_images_base_image(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/023e105f4ecef8ad9ca31a8372d0c353/images/v1/string/blob").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        blob = client.images.v1s.blobs.with_raw_response.cloudflare_images_base_image(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert blob.is_closed is True
        assert blob.http_request.headers.get("X-Stainless-Lang") == "python"
        assert blob.json() == {"foo": "bar"}
        assert isinstance(blob, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_cloudflare_images_base_image(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/023e105f4ecef8ad9ca31a8372d0c353/images/v1/string/blob").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.images.v1s.blobs.with_streaming_response.cloudflare_images_base_image(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as blob:
            assert not blob.is_closed
            assert blob.http_request.headers.get("X-Stainless-Lang") == "python"

            assert blob.json() == {"foo": "bar"}
            assert cast(Any, blob.is_closed) is True
            assert isinstance(blob, StreamedBinaryAPIResponse)

        assert cast(Any, blob.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_cloudflare_images_base_image(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.images.v1s.blobs.with_raw_response.cloudflare_images_base_image(
                "string",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `image_id` but received ''"):
            client.images.v1s.blobs.with_raw_response.cloudflare_images_base_image(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncBlobs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_cloudflare_images_base_image(
        self, async_client: AsyncCloudflare, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/accounts/023e105f4ecef8ad9ca31a8372d0c353/images/v1/string/blob").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        blob = await async_client.images.v1s.blobs.cloudflare_images_base_image(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert blob.is_closed
        assert await blob.json() == {"foo": "bar"}
        assert cast(Any, blob.is_closed) is True
        assert isinstance(blob, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_cloudflare_images_base_image(
        self, async_client: AsyncCloudflare, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/accounts/023e105f4ecef8ad9ca31a8372d0c353/images/v1/string/blob").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        blob = await async_client.images.v1s.blobs.with_raw_response.cloudflare_images_base_image(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert blob.is_closed is True
        assert blob.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await blob.json() == {"foo": "bar"}
        assert isinstance(blob, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_cloudflare_images_base_image(
        self, async_client: AsyncCloudflare, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/accounts/023e105f4ecef8ad9ca31a8372d0c353/images/v1/string/blob").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.images.v1s.blobs.with_streaming_response.cloudflare_images_base_image(
            "string",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as blob:
            assert not blob.is_closed
            assert blob.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await blob.json() == {"foo": "bar"}
            assert cast(Any, blob.is_closed) is True
            assert isinstance(blob, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, blob.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_cloudflare_images_base_image(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.images.v1s.blobs.with_raw_response.cloudflare_images_base_image(
                "string",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `image_id` but received ''"):
            await async_client.images.v1s.blobs.with_raw_response.cloudflare_images_base_image(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
