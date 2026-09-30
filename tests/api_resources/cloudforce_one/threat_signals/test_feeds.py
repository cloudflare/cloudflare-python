# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePagination, AsyncV4PagePagination
from cloudflare.types.cloudforce_one.threat_signals import (
    FeedEditResponse,
    FeedListResponse,
    FeedPollResponse,
    FeedCreateResponse,
    FeedDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeeds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        feed = client.cloudforce_one.threat_signals.feeds.create(
            account_id="account_id",
        )
        assert_matches_type(FeedCreateResponse, feed, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        feed = client.cloudforce_one.threat_signals.feeds.create(
            account_id="account_id",
            category_id="b12a0fd6-f7b9-5393-9ef3-f888d506c550",
            curated_feed_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_name="display_name",
            enabled=True,
            poll_interval_s=60,
            title="title",
            url="https://example.com",
        )
        assert_matches_type(FeedCreateResponse, feed, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_signals.feeds.with_raw_response.create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feed = response.parse()
        assert_matches_type(FeedCreateResponse, feed, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_signals.feeds.with_streaming_response.create(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feed = response.parse()
            assert_matches_type(FeedCreateResponse, feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_signals.feeds.with_raw_response.create(
                account_id="",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        feed = client.cloudforce_one.threat_signals.feeds.list(
            account_id="account_id",
        )
        assert_matches_type(SyncV4PagePagination[FeedListResponse], feed, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        feed = client.cloudforce_one.threat_signals.feeds.list(
            account_id="account_id",
            category="category",
            enabled=True,
            limit=1,
            page=1,
            per_page=1,
            sort="sort",
            source_type="curated",
            status="status",
        )
        assert_matches_type(SyncV4PagePagination[FeedListResponse], feed, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_signals.feeds.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feed = response.parse()
        assert_matches_type(SyncV4PagePagination[FeedListResponse], feed, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_signals.feeds.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feed = response.parse()
            assert_matches_type(SyncV4PagePagination[FeedListResponse], feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_signals.feeds.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        feed = client.cloudforce_one.threat_signals.feeds.delete(
            feed_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(FeedDeleteResponse, feed, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_signals.feeds.with_raw_response.delete(
            feed_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feed = response.parse()
        assert_matches_type(FeedDeleteResponse, feed, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_signals.feeds.with_streaming_response.delete(
            feed_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feed = response.parse()
            assert_matches_type(FeedDeleteResponse, feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_signals.feeds.with_raw_response.delete(
                feed_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feed_id` but received ''"):
            client.cloudforce_one.threat_signals.feeds.with_raw_response.delete(
                feed_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        feed = client.cloudforce_one.threat_signals.feeds.edit(
            feed_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(FeedEditResponse, feed, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        feed = client.cloudforce_one.threat_signals.feeds.edit(
            feed_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            category_id="b12a0fd6-f7b9-5393-9ef3-f888d506c550",
            display_name="display_name",
            enabled=True,
            poll_interval_s=60,
            title="title",
        )
        assert_matches_type(FeedEditResponse, feed, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_signals.feeds.with_raw_response.edit(
            feed_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feed = response.parse()
        assert_matches_type(FeedEditResponse, feed, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_signals.feeds.with_streaming_response.edit(
            feed_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feed = response.parse()
            assert_matches_type(FeedEditResponse, feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_signals.feeds.with_raw_response.edit(
                feed_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feed_id` but received ''"):
            client.cloudforce_one.threat_signals.feeds.with_raw_response.edit(
                feed_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_poll(self, client: Cloudflare) -> None:
        feed = client.cloudforce_one.threat_signals.feeds.poll(
            account_id="account_id",
        )
        assert_matches_type(FeedPollResponse, feed, path=["response"])

    @parametrize
    def test_method_poll_with_all_params(self, client: Cloudflare) -> None:
        feed = client.cloudforce_one.threat_signals.feeds.poll(
            account_id="account_id",
            feed_id="all",
        )
        assert_matches_type(FeedPollResponse, feed, path=["response"])

    @parametrize
    def test_raw_response_poll(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_signals.feeds.with_raw_response.poll(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feed = response.parse()
        assert_matches_type(FeedPollResponse, feed, path=["response"])

    @parametrize
    def test_streaming_response_poll(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_signals.feeds.with_streaming_response.poll(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feed = response.parse()
            assert_matches_type(FeedPollResponse, feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_poll(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_signals.feeds.with_raw_response.poll(
                account_id="",
            )


class TestAsyncFeeds:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        feed = await async_client.cloudforce_one.threat_signals.feeds.create(
            account_id="account_id",
        )
        assert_matches_type(FeedCreateResponse, feed, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        feed = await async_client.cloudforce_one.threat_signals.feeds.create(
            account_id="account_id",
            category_id="b12a0fd6-f7b9-5393-9ef3-f888d506c550",
            curated_feed_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            display_name="display_name",
            enabled=True,
            poll_interval_s=60,
            title="title",
            url="https://example.com",
        )
        assert_matches_type(FeedCreateResponse, feed, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_signals.feeds.with_raw_response.create(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feed = await response.parse()
        assert_matches_type(FeedCreateResponse, feed, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_signals.feeds.with_streaming_response.create(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feed = await response.parse()
            assert_matches_type(FeedCreateResponse, feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.feeds.with_raw_response.create(
                account_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        feed = await async_client.cloudforce_one.threat_signals.feeds.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncV4PagePagination[FeedListResponse], feed, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        feed = await async_client.cloudforce_one.threat_signals.feeds.list(
            account_id="account_id",
            category="category",
            enabled=True,
            limit=1,
            page=1,
            per_page=1,
            sort="sort",
            source_type="curated",
            status="status",
        )
        assert_matches_type(AsyncV4PagePagination[FeedListResponse], feed, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_signals.feeds.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feed = await response.parse()
        assert_matches_type(AsyncV4PagePagination[FeedListResponse], feed, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_signals.feeds.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feed = await response.parse()
            assert_matches_type(AsyncV4PagePagination[FeedListResponse], feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.feeds.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        feed = await async_client.cloudforce_one.threat_signals.feeds.delete(
            feed_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(FeedDeleteResponse, feed, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_signals.feeds.with_raw_response.delete(
            feed_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feed = await response.parse()
        assert_matches_type(FeedDeleteResponse, feed, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_signals.feeds.with_streaming_response.delete(
            feed_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feed = await response.parse()
            assert_matches_type(FeedDeleteResponse, feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.feeds.with_raw_response.delete(
                feed_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feed_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.feeds.with_raw_response.delete(
                feed_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        feed = await async_client.cloudforce_one.threat_signals.feeds.edit(
            feed_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(FeedEditResponse, feed, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        feed = await async_client.cloudforce_one.threat_signals.feeds.edit(
            feed_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            category_id="b12a0fd6-f7b9-5393-9ef3-f888d506c550",
            display_name="display_name",
            enabled=True,
            poll_interval_s=60,
            title="title",
        )
        assert_matches_type(FeedEditResponse, feed, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_signals.feeds.with_raw_response.edit(
            feed_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feed = await response.parse()
        assert_matches_type(FeedEditResponse, feed, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_signals.feeds.with_streaming_response.edit(
            feed_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feed = await response.parse()
            assert_matches_type(FeedEditResponse, feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.feeds.with_raw_response.edit(
                feed_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feed_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.feeds.with_raw_response.edit(
                feed_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_poll(self, async_client: AsyncCloudflare) -> None:
        feed = await async_client.cloudforce_one.threat_signals.feeds.poll(
            account_id="account_id",
        )
        assert_matches_type(FeedPollResponse, feed, path=["response"])

    @parametrize
    async def test_method_poll_with_all_params(self, async_client: AsyncCloudflare) -> None:
        feed = await async_client.cloudforce_one.threat_signals.feeds.poll(
            account_id="account_id",
            feed_id="all",
        )
        assert_matches_type(FeedPollResponse, feed, path=["response"])

    @parametrize
    async def test_raw_response_poll(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_signals.feeds.with_raw_response.poll(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feed = await response.parse()
        assert_matches_type(FeedPollResponse, feed, path=["response"])

    @parametrize
    async def test_streaming_response_poll(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_signals.feeds.with_streaming_response.poll(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feed = await response.parse()
            assert_matches_type(FeedPollResponse, feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_poll(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_signals.feeds.with_raw_response.poll(
                account_id="",
            )
