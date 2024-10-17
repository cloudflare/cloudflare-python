# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.intel import (
    IndicatorFeedGetResponse,
    IndicatorFeedListResponse,
    IndicatorFeedCreateResponse,
    IndicatorFeedUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIndicatorFeeds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        indicator_feed = client.intel.indicator_feeds.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IndicatorFeedCreateResponse], indicator_feed, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        indicator_feed = client.intel.indicator_feeds.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="example feed description",
            name="example_feed_1",
        )
        assert_matches_type(Optional[IndicatorFeedCreateResponse], indicator_feed, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.intel.indicator_feeds.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = response.parse()
        assert_matches_type(Optional[IndicatorFeedCreateResponse], indicator_feed, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.intel.indicator_feeds.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = response.parse()
            assert_matches_type(Optional[IndicatorFeedCreateResponse], indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.intel.indicator_feeds.with_raw_response.create(
                account_id="",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        indicator_feed = client.intel.indicator_feeds.update(
            feed_id=12,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IndicatorFeedUpdateResponse], indicator_feed, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        indicator_feed = client.intel.indicator_feeds.update(
            feed_id=12,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="This is an example description",
            is_attributable=True,
            is_downloadable=True,
            is_public=True,
            name="indicator_list",
        )
        assert_matches_type(Optional[IndicatorFeedUpdateResponse], indicator_feed, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.intel.indicator_feeds.with_raw_response.update(
            feed_id=12,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = response.parse()
        assert_matches_type(Optional[IndicatorFeedUpdateResponse], indicator_feed, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.intel.indicator_feeds.with_streaming_response.update(
            feed_id=12,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = response.parse()
            assert_matches_type(Optional[IndicatorFeedUpdateResponse], indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.intel.indicator_feeds.with_raw_response.update(
                feed_id=12,
                account_id="",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        indicator_feed = client.intel.indicator_feeds.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[IndicatorFeedListResponse], indicator_feed, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.intel.indicator_feeds.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = response.parse()
        assert_matches_type(SyncSinglePage[IndicatorFeedListResponse], indicator_feed, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.intel.indicator_feeds.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = response.parse()
            assert_matches_type(SyncSinglePage[IndicatorFeedListResponse], indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.intel.indicator_feeds.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_data(self, client: Cloudflare) -> None:
        indicator_feed = client.intel.indicator_feeds.data(
            feed_id=12,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(str, indicator_feed, path=["response"])

    @parametrize
    def test_raw_response_data(self, client: Cloudflare) -> None:
        response = client.intel.indicator_feeds.with_raw_response.data(
            feed_id=12,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = response.parse()
        assert_matches_type(str, indicator_feed, path=["response"])

    @parametrize
    def test_streaming_response_data(self, client: Cloudflare) -> None:
        with client.intel.indicator_feeds.with_streaming_response.data(
            feed_id=12,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = response.parse()
            assert_matches_type(str, indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_data(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.intel.indicator_feeds.with_raw_response.data(
                feed_id=12,
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        indicator_feed = client.intel.indicator_feeds.get(
            feed_id=12,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IndicatorFeedGetResponse], indicator_feed, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.intel.indicator_feeds.with_raw_response.get(
            feed_id=12,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = response.parse()
        assert_matches_type(Optional[IndicatorFeedGetResponse], indicator_feed, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.intel.indicator_feeds.with_streaming_response.get(
            feed_id=12,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = response.parse()
            assert_matches_type(Optional[IndicatorFeedGetResponse], indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.intel.indicator_feeds.with_raw_response.get(
                feed_id=12,
                account_id="",
            )


class TestAsyncIndicatorFeeds:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        indicator_feed = await async_client.intel.indicator_feeds.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IndicatorFeedCreateResponse], indicator_feed, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        indicator_feed = await async_client.intel.indicator_feeds.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="example feed description",
            name="example_feed_1",
        )
        assert_matches_type(Optional[IndicatorFeedCreateResponse], indicator_feed, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.indicator_feeds.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = await response.parse()
        assert_matches_type(Optional[IndicatorFeedCreateResponse], indicator_feed, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.indicator_feeds.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = await response.parse()
            assert_matches_type(Optional[IndicatorFeedCreateResponse], indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.intel.indicator_feeds.with_raw_response.create(
                account_id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        indicator_feed = await async_client.intel.indicator_feeds.update(
            feed_id=12,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IndicatorFeedUpdateResponse], indicator_feed, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        indicator_feed = await async_client.intel.indicator_feeds.update(
            feed_id=12,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="This is an example description",
            is_attributable=True,
            is_downloadable=True,
            is_public=True,
            name="indicator_list",
        )
        assert_matches_type(Optional[IndicatorFeedUpdateResponse], indicator_feed, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.indicator_feeds.with_raw_response.update(
            feed_id=12,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = await response.parse()
        assert_matches_type(Optional[IndicatorFeedUpdateResponse], indicator_feed, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.indicator_feeds.with_streaming_response.update(
            feed_id=12,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = await response.parse()
            assert_matches_type(Optional[IndicatorFeedUpdateResponse], indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.intel.indicator_feeds.with_raw_response.update(
                feed_id=12,
                account_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        indicator_feed = await async_client.intel.indicator_feeds.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[IndicatorFeedListResponse], indicator_feed, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.indicator_feeds.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = await response.parse()
        assert_matches_type(AsyncSinglePage[IndicatorFeedListResponse], indicator_feed, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.indicator_feeds.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = await response.parse()
            assert_matches_type(AsyncSinglePage[IndicatorFeedListResponse], indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.intel.indicator_feeds.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_data(self, async_client: AsyncCloudflare) -> None:
        indicator_feed = await async_client.intel.indicator_feeds.data(
            feed_id=12,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(str, indicator_feed, path=["response"])

    @parametrize
    async def test_raw_response_data(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.indicator_feeds.with_raw_response.data(
            feed_id=12,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = await response.parse()
        assert_matches_type(str, indicator_feed, path=["response"])

    @parametrize
    async def test_streaming_response_data(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.indicator_feeds.with_streaming_response.data(
            feed_id=12,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = await response.parse()
            assert_matches_type(str, indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_data(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.intel.indicator_feeds.with_raw_response.data(
                feed_id=12,
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        indicator_feed = await async_client.intel.indicator_feeds.get(
            feed_id=12,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[IndicatorFeedGetResponse], indicator_feed, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.indicator_feeds.with_raw_response.get(
            feed_id=12,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = await response.parse()
        assert_matches_type(Optional[IndicatorFeedGetResponse], indicator_feed, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.indicator_feeds.with_streaming_response.get(
            feed_id=12,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = await response.parse()
            assert_matches_type(Optional[IndicatorFeedGetResponse], indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.intel.indicator_feeds.with_raw_response.get(
                feed_id=12,
                account_id="",
            )
