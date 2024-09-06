# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

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


class TestDownloads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="TODO: address broken spotlight error - https://github.com/cloudflare/cloudflare-typescript/actions/runs/9456639475/job/26048931174?pr=498#step:5:489"
    )
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/addressing/loa_documents/d933b1530bc56c9953cf8ce166da8004/download"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        download = client.addressing.loa_documents.downloads.get(
            loa_document_id="d933b1530bc56c9953cf8ce166da8004",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert download.is_closed
        assert download.json() == {"foo": "bar"}
        assert cast(Any, download.is_closed) is True
        assert isinstance(download, BinaryAPIResponse)

    @pytest.mark.skip(
        reason="TODO: address broken spotlight error - https://github.com/cloudflare/cloudflare-typescript/actions/runs/9456639475/job/26048931174?pr=498#step:5:489"
    )
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/addressing/loa_documents/d933b1530bc56c9953cf8ce166da8004/download"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        download = client.addressing.loa_documents.downloads.with_raw_response.get(
            loa_document_id="d933b1530bc56c9953cf8ce166da8004",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert download.is_closed is True
        assert download.http_request.headers.get("X-Stainless-Lang") == "python"
        assert download.json() == {"foo": "bar"}
        assert isinstance(download, BinaryAPIResponse)

    @pytest.mark.skip(
        reason="TODO: address broken spotlight error - https://github.com/cloudflare/cloudflare-typescript/actions/runs/9456639475/job/26048931174?pr=498#step:5:489"
    )
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/addressing/loa_documents/d933b1530bc56c9953cf8ce166da8004/download"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.addressing.loa_documents.downloads.with_streaming_response.get(
            loa_document_id="d933b1530bc56c9953cf8ce166da8004",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as download:
            assert not download.is_closed
            assert download.http_request.headers.get("X-Stainless-Lang") == "python"

            assert download.json() == {"foo": "bar"}
            assert cast(Any, download.is_closed) is True
            assert isinstance(download, StreamedBinaryAPIResponse)

        assert cast(Any, download.is_closed) is True

    @pytest.mark.skip(
        reason="TODO: address broken spotlight error - https://github.com/cloudflare/cloudflare-typescript/actions/runs/9456639475/job/26048931174?pr=498#step:5:489"
    )
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.loa_documents.downloads.with_raw_response.get(
                loa_document_id="d933b1530bc56c9953cf8ce166da8004",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `loa_document_id` but received ''"):
            client.addressing.loa_documents.downloads.with_raw_response.get(
                loa_document_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncDownloads:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="TODO: address broken spotlight error - https://github.com/cloudflare/cloudflare-typescript/actions/runs/9456639475/job/26048931174?pr=498#step:5:489"
    )
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/addressing/loa_documents/d933b1530bc56c9953cf8ce166da8004/download"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        download = await async_client.addressing.loa_documents.downloads.get(
            loa_document_id="d933b1530bc56c9953cf8ce166da8004",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert download.is_closed
        assert await download.json() == {"foo": "bar"}
        assert cast(Any, download.is_closed) is True
        assert isinstance(download, AsyncBinaryAPIResponse)

    @pytest.mark.skip(
        reason="TODO: address broken spotlight error - https://github.com/cloudflare/cloudflare-typescript/actions/runs/9456639475/job/26048931174?pr=498#step:5:489"
    )
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/addressing/loa_documents/d933b1530bc56c9953cf8ce166da8004/download"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        download = await async_client.addressing.loa_documents.downloads.with_raw_response.get(
            loa_document_id="d933b1530bc56c9953cf8ce166da8004",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert download.is_closed is True
        assert download.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await download.json() == {"foo": "bar"}
        assert isinstance(download, AsyncBinaryAPIResponse)

    @pytest.mark.skip(
        reason="TODO: address broken spotlight error - https://github.com/cloudflare/cloudflare-typescript/actions/runs/9456639475/job/26048931174?pr=498#step:5:489"
    )
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/addressing/loa_documents/d933b1530bc56c9953cf8ce166da8004/download"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.addressing.loa_documents.downloads.with_streaming_response.get(
            loa_document_id="d933b1530bc56c9953cf8ce166da8004",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as download:
            assert not download.is_closed
            assert download.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await download.json() == {"foo": "bar"}
            assert cast(Any, download.is_closed) is True
            assert isinstance(download, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, download.is_closed) is True

    @pytest.mark.skip(
        reason="TODO: address broken spotlight error - https://github.com/cloudflare/cloudflare-typescript/actions/runs/9456639475/job/26048931174?pr=498#step:5:489"
    )
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.loa_documents.downloads.with_raw_response.get(
                loa_document_id="d933b1530bc56c9953cf8ce166da8004",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `loa_document_id` but received ''"):
            await async_client.addressing.loa_documents.downloads.with_raw_response.get(
                loa_document_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
