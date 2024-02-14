# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.stream import (
    DownloadDeleteResponse,
    DownloadStreamMP4DownloadsListDownloadsResponse,
    DownloadStreamMP4DownloadsCreateDownloadsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDownloads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        download = client.stream.downloads.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DownloadDeleteResponse, download, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.stream.downloads.with_raw_response.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        download = response.parse()
        assert_matches_type(DownloadDeleteResponse, download, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.stream.downloads.with_streaming_response.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            download = response.parse()
            assert_matches_type(DownloadDeleteResponse, download, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.downloads.with_raw_response.delete(
                "ea95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.stream.downloads.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_m_p_4_downloads_create_downloads(self, client: Cloudflare) -> None:
        download = client.stream.downloads.stream_m_p_4_downloads_create_downloads(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DownloadStreamMP4DownloadsCreateDownloadsResponse, download, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stream_m_p_4_downloads_create_downloads(self, client: Cloudflare) -> None:
        response = client.stream.downloads.with_raw_response.stream_m_p_4_downloads_create_downloads(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        download = response.parse()
        assert_matches_type(DownloadStreamMP4DownloadsCreateDownloadsResponse, download, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stream_m_p_4_downloads_create_downloads(self, client: Cloudflare) -> None:
        with client.stream.downloads.with_streaming_response.stream_m_p_4_downloads_create_downloads(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            download = response.parse()
            assert_matches_type(DownloadStreamMP4DownloadsCreateDownloadsResponse, download, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_stream_m_p_4_downloads_create_downloads(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.downloads.with_raw_response.stream_m_p_4_downloads_create_downloads(
                "ea95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.stream.downloads.with_raw_response.stream_m_p_4_downloads_create_downloads(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_m_p_4_downloads_list_downloads(self, client: Cloudflare) -> None:
        download = client.stream.downloads.stream_m_p_4_downloads_list_downloads(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DownloadStreamMP4DownloadsListDownloadsResponse, download, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stream_m_p_4_downloads_list_downloads(self, client: Cloudflare) -> None:
        response = client.stream.downloads.with_raw_response.stream_m_p_4_downloads_list_downloads(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        download = response.parse()
        assert_matches_type(DownloadStreamMP4DownloadsListDownloadsResponse, download, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stream_m_p_4_downloads_list_downloads(self, client: Cloudflare) -> None:
        with client.stream.downloads.with_streaming_response.stream_m_p_4_downloads_list_downloads(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            download = response.parse()
            assert_matches_type(DownloadStreamMP4DownloadsListDownloadsResponse, download, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_stream_m_p_4_downloads_list_downloads(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.downloads.with_raw_response.stream_m_p_4_downloads_list_downloads(
                "ea95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.stream.downloads.with_raw_response.stream_m_p_4_downloads_list_downloads(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncDownloads:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        download = await async_client.stream.downloads.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DownloadDeleteResponse, download, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.downloads.with_raw_response.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        download = await response.parse()
        assert_matches_type(DownloadDeleteResponse, download, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.downloads.with_streaming_response.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            download = await response.parse()
            assert_matches_type(DownloadDeleteResponse, download, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.downloads.with_raw_response.delete(
                "ea95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.stream.downloads.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_m_p_4_downloads_create_downloads(self, async_client: AsyncCloudflare) -> None:
        download = await async_client.stream.downloads.stream_m_p_4_downloads_create_downloads(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DownloadStreamMP4DownloadsCreateDownloadsResponse, download, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stream_m_p_4_downloads_create_downloads(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.downloads.with_raw_response.stream_m_p_4_downloads_create_downloads(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        download = await response.parse()
        assert_matches_type(DownloadStreamMP4DownloadsCreateDownloadsResponse, download, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stream_m_p_4_downloads_create_downloads(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.stream.downloads.with_streaming_response.stream_m_p_4_downloads_create_downloads(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            download = await response.parse()
            assert_matches_type(DownloadStreamMP4DownloadsCreateDownloadsResponse, download, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_stream_m_p_4_downloads_create_downloads(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.downloads.with_raw_response.stream_m_p_4_downloads_create_downloads(
                "ea95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.stream.downloads.with_raw_response.stream_m_p_4_downloads_create_downloads(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_m_p_4_downloads_list_downloads(self, async_client: AsyncCloudflare) -> None:
        download = await async_client.stream.downloads.stream_m_p_4_downloads_list_downloads(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DownloadStreamMP4DownloadsListDownloadsResponse, download, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stream_m_p_4_downloads_list_downloads(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.downloads.with_raw_response.stream_m_p_4_downloads_list_downloads(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        download = await response.parse()
        assert_matches_type(DownloadStreamMP4DownloadsListDownloadsResponse, download, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stream_m_p_4_downloads_list_downloads(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.stream.downloads.with_streaming_response.stream_m_p_4_downloads_list_downloads(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            download = await response.parse()
            assert_matches_type(DownloadStreamMP4DownloadsListDownloadsResponse, download, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_stream_m_p_4_downloads_list_downloads(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.downloads.with_raw_response.stream_m_p_4_downloads_list_downloads(
                "ea95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.stream.downloads.with_raw_response.stream_m_p_4_downloads_list_downloads(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
