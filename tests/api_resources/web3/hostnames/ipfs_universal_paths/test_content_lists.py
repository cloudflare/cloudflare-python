# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.web3.hostnames.ipfs_universal_paths import ContentList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContentLists:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        content_list = client.web3.hostnames.ipfs_universal_paths.content_lists.update(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="block",
            entries=[{}],
        )
        assert_matches_type(ContentList, content_list, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.web3.hostnames.ipfs_universal_paths.content_lists.with_raw_response.update(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="block",
            entries=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_list = response.parse()
        assert_matches_type(ContentList, content_list, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.web3.hostnames.ipfs_universal_paths.content_lists.with_streaming_response.update(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="block",
            entries=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_list = response.parse()
            assert_matches_type(ContentList, content_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.web3.hostnames.ipfs_universal_paths.content_lists.with_raw_response.update(
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                action="block",
                entries=[{}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.web3.hostnames.ipfs_universal_paths.content_lists.with_raw_response.update(
                identifier="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action="block",
                entries=[{}],
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        content_list = client.web3.hostnames.ipfs_universal_paths.content_lists.get(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ContentList, content_list, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.web3.hostnames.ipfs_universal_paths.content_lists.with_raw_response.get(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_list = response.parse()
        assert_matches_type(ContentList, content_list, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.web3.hostnames.ipfs_universal_paths.content_lists.with_streaming_response.get(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_list = response.parse()
            assert_matches_type(ContentList, content_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.web3.hostnames.ipfs_universal_paths.content_lists.with_raw_response.get(
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.web3.hostnames.ipfs_universal_paths.content_lists.with_raw_response.get(
                identifier="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncContentLists:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        content_list = await async_client.web3.hostnames.ipfs_universal_paths.content_lists.update(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="block",
            entries=[{}],
        )
        assert_matches_type(ContentList, content_list, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.web3.hostnames.ipfs_universal_paths.content_lists.with_raw_response.update(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="block",
            entries=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_list = await response.parse()
        assert_matches_type(ContentList, content_list, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.web3.hostnames.ipfs_universal_paths.content_lists.with_streaming_response.update(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="block",
            entries=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_list = await response.parse()
            assert_matches_type(ContentList, content_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.web3.hostnames.ipfs_universal_paths.content_lists.with_raw_response.update(
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                action="block",
                entries=[{}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.web3.hostnames.ipfs_universal_paths.content_lists.with_raw_response.update(
                identifier="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                action="block",
                entries=[{}],
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        content_list = await async_client.web3.hostnames.ipfs_universal_paths.content_lists.get(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ContentList, content_list, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.web3.hostnames.ipfs_universal_paths.content_lists.with_raw_response.get(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        content_list = await response.parse()
        assert_matches_type(ContentList, content_list, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.web3.hostnames.ipfs_universal_paths.content_lists.with_streaming_response.get(
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            content_list = await response.parse()
            assert_matches_type(ContentList, content_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.web3.hostnames.ipfs_universal_paths.content_lists.with_raw_response.get(
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.web3.hostnames.ipfs_universal_paths.content_lists.with_raw_response.get(
                identifier="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
