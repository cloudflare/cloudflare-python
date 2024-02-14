# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDownloads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        download = client.addresses.loa_documents.downloads.list(
            "d933b1530bc56c9953cf8ce166da8004",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, download, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.addresses.loa_documents.downloads.with_raw_response.list(
            "d933b1530bc56c9953cf8ce166da8004",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        download = response.parse()
        assert_matches_type(object, download, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.addresses.loa_documents.downloads.with_streaming_response.list(
            "d933b1530bc56c9953cf8ce166da8004",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            download = response.parse()
            assert_matches_type(object, download, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.addresses.loa_documents.downloads.with_raw_response.list(
                "d933b1530bc56c9953cf8ce166da8004",
                account_identifier="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `loa_document_identifier` but received ''"
        ):
            client.addresses.loa_documents.downloads.with_raw_response.list(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncDownloads:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        download = await async_client.addresses.loa_documents.downloads.list(
            "d933b1530bc56c9953cf8ce166da8004",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, download, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addresses.loa_documents.downloads.with_raw_response.list(
            "d933b1530bc56c9953cf8ce166da8004",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        download = await response.parse()
        assert_matches_type(object, download, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addresses.loa_documents.downloads.with_streaming_response.list(
            "d933b1530bc56c9953cf8ce166da8004",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            download = await response.parse()
            assert_matches_type(object, download, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.addresses.loa_documents.downloads.with_raw_response.list(
                "d933b1530bc56c9953cf8ce166da8004",
                account_identifier="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `loa_document_identifier` but received ''"
        ):
            await async_client.addresses.loa_documents.downloads.with_raw_response.list(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )
