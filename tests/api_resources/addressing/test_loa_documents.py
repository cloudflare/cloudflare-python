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


class TestLOADocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="TODO: address broken spotlight error - https://github.com/cloudflare/cloudflare-typescript/actions/runs/9456639475/job/26048931174?pr=498#step:5:489"
    )
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/258def64c72dae45f3e4c8516e2111f2/addressing/loa_documents/d933b1530bc56c9953cf8ce166da8004/download"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        loa_document = client.addressing.loa_documents.get(
            loa_document_id="d933b1530bc56c9953cf8ce166da8004",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert loa_document.is_closed
        assert loa_document.json() == {"foo": "bar"}
        assert cast(Any, loa_document.is_closed) is True
        assert isinstance(loa_document, BinaryAPIResponse)

    @pytest.mark.skip(
        reason="TODO: address broken spotlight error - https://github.com/cloudflare/cloudflare-typescript/actions/runs/9456639475/job/26048931174?pr=498#step:5:489"
    )
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/258def64c72dae45f3e4c8516e2111f2/addressing/loa_documents/d933b1530bc56c9953cf8ce166da8004/download"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        loa_document = client.addressing.loa_documents.with_raw_response.get(
            loa_document_id="d933b1530bc56c9953cf8ce166da8004",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert loa_document.is_closed is True
        assert loa_document.http_request.headers.get("X-Stainless-Lang") == "python"
        assert loa_document.json() == {"foo": "bar"}
        assert isinstance(loa_document, BinaryAPIResponse)

    @pytest.mark.skip(
        reason="TODO: address broken spotlight error - https://github.com/cloudflare/cloudflare-typescript/actions/runs/9456639475/job/26048931174?pr=498#step:5:489"
    )
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/258def64c72dae45f3e4c8516e2111f2/addressing/loa_documents/d933b1530bc56c9953cf8ce166da8004/download"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.addressing.loa_documents.with_streaming_response.get(
            loa_document_id="d933b1530bc56c9953cf8ce166da8004",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as loa_document:
            assert not loa_document.is_closed
            assert loa_document.http_request.headers.get("X-Stainless-Lang") == "python"

            assert loa_document.json() == {"foo": "bar"}
            assert cast(Any, loa_document.is_closed) is True
            assert isinstance(loa_document, StreamedBinaryAPIResponse)

        assert cast(Any, loa_document.is_closed) is True

    @pytest.mark.skip(
        reason="TODO: address broken spotlight error - https://github.com/cloudflare/cloudflare-typescript/actions/runs/9456639475/job/26048931174?pr=498#step:5:489"
    )
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.loa_documents.with_raw_response.get(
                loa_document_id="d933b1530bc56c9953cf8ce166da8004",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `loa_document_id` but received ''"):
            client.addressing.loa_documents.with_raw_response.get(
                loa_document_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
            )


class TestAsyncLOADocuments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(
        reason="TODO: address broken spotlight error - https://github.com/cloudflare/cloudflare-typescript/actions/runs/9456639475/job/26048931174?pr=498#step:5:489"
    )
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/258def64c72dae45f3e4c8516e2111f2/addressing/loa_documents/d933b1530bc56c9953cf8ce166da8004/download"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        loa_document = await async_client.addressing.loa_documents.get(
            loa_document_id="d933b1530bc56c9953cf8ce166da8004",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert loa_document.is_closed
        assert await loa_document.json() == {"foo": "bar"}
        assert cast(Any, loa_document.is_closed) is True
        assert isinstance(loa_document, AsyncBinaryAPIResponse)

    @pytest.mark.skip(
        reason="TODO: address broken spotlight error - https://github.com/cloudflare/cloudflare-typescript/actions/runs/9456639475/job/26048931174?pr=498#step:5:489"
    )
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/258def64c72dae45f3e4c8516e2111f2/addressing/loa_documents/d933b1530bc56c9953cf8ce166da8004/download"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        loa_document = await async_client.addressing.loa_documents.with_raw_response.get(
            loa_document_id="d933b1530bc56c9953cf8ce166da8004",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert loa_document.is_closed is True
        assert loa_document.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await loa_document.json() == {"foo": "bar"}
        assert isinstance(loa_document, AsyncBinaryAPIResponse)

    @pytest.mark.skip(
        reason="TODO: address broken spotlight error - https://github.com/cloudflare/cloudflare-typescript/actions/runs/9456639475/job/26048931174?pr=498#step:5:489"
    )
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/258def64c72dae45f3e4c8516e2111f2/addressing/loa_documents/d933b1530bc56c9953cf8ce166da8004/download"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.addressing.loa_documents.with_streaming_response.get(
            loa_document_id="d933b1530bc56c9953cf8ce166da8004",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as loa_document:
            assert not loa_document.is_closed
            assert loa_document.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await loa_document.json() == {"foo": "bar"}
            assert cast(Any, loa_document.is_closed) is True
            assert isinstance(loa_document, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, loa_document.is_closed) is True

    @pytest.mark.skip(
        reason="TODO: address broken spotlight error - https://github.com/cloudflare/cloudflare-typescript/actions/runs/9456639475/job/26048931174?pr=498#step:5:489"
    )
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.loa_documents.with_raw_response.get(
                loa_document_id="d933b1530bc56c9953cf8ce166da8004",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `loa_document_id` but received ''"):
            await async_client.addressing.loa_documents.with_raw_response.get(
                loa_document_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
            )
