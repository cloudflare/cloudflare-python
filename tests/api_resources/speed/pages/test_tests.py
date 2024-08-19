# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.speed.pages import (
    Test,
    TestDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        test = client.speed.pages.tests.create(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Test], test, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        test = client.speed.pages.tests.create(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region="asia-east1",
        )
        assert_matches_type(Optional[Test], test, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.speed.pages.tests.with_raw_response.create(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(Optional[Test], test, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.speed.pages.tests.with_streaming_response.create(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(Optional[Test], test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.speed.pages.tests.with_raw_response.create(
                url="example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            client.speed.pages.tests.with_raw_response.create(
                url="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        test = client.speed.pages.tests.list(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[Test], test, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        test = client.speed.pages.tests.list(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=5,
            region="asia-east1",
        )
        assert_matches_type(SyncV4PagePaginationArray[Test], test, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.speed.pages.tests.with_raw_response.list(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[Test], test, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.speed.pages.tests.with_streaming_response.list(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[Test], test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.speed.pages.tests.with_raw_response.list(
                url="example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            client.speed.pages.tests.with_raw_response.list(
                url="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        test = client.speed.pages.tests.delete(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[TestDeleteResponse], test, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        test = client.speed.pages.tests.delete(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region="asia-east1",
        )
        assert_matches_type(Optional[TestDeleteResponse], test, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.speed.pages.tests.with_raw_response.delete(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(Optional[TestDeleteResponse], test, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.speed.pages.tests.with_streaming_response.delete(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(Optional[TestDeleteResponse], test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.speed.pages.tests.with_raw_response.delete(
                url="example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            client.speed.pages.tests.with_raw_response.delete(
                url="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        test = client.speed.pages.tests.get(
            test_id="test_id",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="example.com",
        )
        assert_matches_type(Optional[Test], test, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.speed.pages.tests.with_raw_response.get(
            test_id="test_id",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(Optional[Test], test, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.speed.pages.tests.with_streaming_response.get(
            test_id="test_id",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(Optional[Test], test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.speed.pages.tests.with_raw_response.get(
                test_id="test_id",
                zone_id="",
                url="example.com",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            client.speed.pages.tests.with_raw_response.get(
                test_id="test_id",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                url="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_id` but received ''"):
            client.speed.pages.tests.with_raw_response.get(
                test_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                url="example.com",
            )


class TestAsyncTests:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        test = await async_client.speed.pages.tests.create(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Test], test, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        test = await async_client.speed.pages.tests.create(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region="asia-east1",
        )
        assert_matches_type(Optional[Test], test, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.speed.pages.tests.with_raw_response.create(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(Optional[Test], test, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.speed.pages.tests.with_streaming_response.create(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(Optional[Test], test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.speed.pages.tests.with_raw_response.create(
                url="example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            await async_client.speed.pages.tests.with_raw_response.create(
                url="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        test = await async_client.speed.pages.tests.list(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[Test], test, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        test = await async_client.speed.pages.tests.list(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=5,
            region="asia-east1",
        )
        assert_matches_type(AsyncV4PagePaginationArray[Test], test, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.speed.pages.tests.with_raw_response.list(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[Test], test, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.speed.pages.tests.with_streaming_response.list(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[Test], test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.speed.pages.tests.with_raw_response.list(
                url="example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            await async_client.speed.pages.tests.with_raw_response.list(
                url="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        test = await async_client.speed.pages.tests.delete(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[TestDeleteResponse], test, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        test = await async_client.speed.pages.tests.delete(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region="asia-east1",
        )
        assert_matches_type(Optional[TestDeleteResponse], test, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.speed.pages.tests.with_raw_response.delete(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(Optional[TestDeleteResponse], test, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.speed.pages.tests.with_streaming_response.delete(
            url="example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(Optional[TestDeleteResponse], test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.speed.pages.tests.with_raw_response.delete(
                url="example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            await async_client.speed.pages.tests.with_raw_response.delete(
                url="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        test = await async_client.speed.pages.tests.get(
            test_id="test_id",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="example.com",
        )
        assert_matches_type(Optional[Test], test, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.speed.pages.tests.with_raw_response.get(
            test_id="test_id",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(Optional[Test], test, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.speed.pages.tests.with_streaming_response.get(
            test_id="test_id",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(Optional[Test], test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.speed.pages.tests.with_raw_response.get(
                test_id="test_id",
                zone_id="",
                url="example.com",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            await async_client.speed.pages.tests.with_raw_response.get(
                test_id="test_id",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                url="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_id` but received ''"):
            await async_client.speed.pages.tests.with_raw_response.get(
                test_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                url="example.com",
            )
