# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.intel import (
    IndicatorFeedCreateResponse,
    IndicatorFeedListResponse,
    IndicatorFeedDataResponse,
    IndicatorFeedGetResponse,
    IndicatorFeedPermissionsAddResponse,
    IndicatorFeedPermissionsRemoveResponse,
    IndicatorFeedPermissionsViewResponse,
    IndicatorFeedSnapshotResponse,
)

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.intel import indicator_feed_create_params
from cloudflare.types.intel import indicator_feed_permissions_add_params
from cloudflare.types.intel import indicator_feed_permissions_remove_params
from cloudflare.types.intel import indicator_feed_snapshot_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIndicatorFeeds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        indicator_feed = client.intel.indicator_feeds.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IndicatorFeedCreateResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        indicator_feed = client.intel.indicator_feeds.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            description="example feed description",
            name="example_feed_1",
        )
        assert_matches_type(IndicatorFeedCreateResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.intel.indicator_feeds.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = response.parse()
        assert_matches_type(IndicatorFeedCreateResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.intel.indicator_feeds.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = response.parse()
            assert_matches_type(IndicatorFeedCreateResponse, indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.intel.indicator_feeds.with_raw_response.create(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        indicator_feed = client.intel.indicator_feeds.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IndicatorFeedListResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.intel.indicator_feeds.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = response.parse()
        assert_matches_type(IndicatorFeedListResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.intel.indicator_feeds.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = response.parse()
            assert_matches_type(IndicatorFeedListResponse, indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.intel.indicator_feeds.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_data(self, client: Cloudflare) -> None:
        indicator_feed = client.intel.indicator_feeds.data(
            12,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(str, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_data(self, client: Cloudflare) -> None:
        response = client.intel.indicator_feeds.with_raw_response.data(
            12,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = response.parse()
        assert_matches_type(str, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_data(self, client: Cloudflare) -> None:
        with client.intel.indicator_feeds.with_streaming_response.data(
            12,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = response.parse()
            assert_matches_type(str, indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_data(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.intel.indicator_feeds.with_raw_response.data(
                12,
                account_identifier="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        indicator_feed = client.intel.indicator_feeds.get(
            12,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IndicatorFeedGetResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.intel.indicator_feeds.with_raw_response.get(
            12,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = response.parse()
        assert_matches_type(IndicatorFeedGetResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.intel.indicator_feeds.with_streaming_response.get(
            12,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = response.parse()
            assert_matches_type(IndicatorFeedGetResponse, indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.intel.indicator_feeds.with_raw_response.get(
                12,
                account_identifier="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_permissions_add(self, client: Cloudflare) -> None:
        indicator_feed = client.intel.indicator_feeds.permissions_add(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IndicatorFeedPermissionsAddResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_permissions_add_with_all_params(self, client: Cloudflare) -> None:
        indicator_feed = client.intel.indicator_feeds.permissions_add(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_tag="823f45f16fd2f7e21e1e054aga4d2859",
            feed_id=1,
        )
        assert_matches_type(IndicatorFeedPermissionsAddResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_permissions_add(self, client: Cloudflare) -> None:
        response = client.intel.indicator_feeds.with_raw_response.permissions_add(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = response.parse()
        assert_matches_type(IndicatorFeedPermissionsAddResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_permissions_add(self, client: Cloudflare) -> None:
        with client.intel.indicator_feeds.with_streaming_response.permissions_add(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = response.parse()
            assert_matches_type(IndicatorFeedPermissionsAddResponse, indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_permissions_add(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.intel.indicator_feeds.with_raw_response.permissions_add(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_permissions_remove(self, client: Cloudflare) -> None:
        indicator_feed = client.intel.indicator_feeds.permissions_remove(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IndicatorFeedPermissionsRemoveResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_permissions_remove_with_all_params(self, client: Cloudflare) -> None:
        indicator_feed = client.intel.indicator_feeds.permissions_remove(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_tag="823f45f16fd2f7e21e1e054aga4d2859",
            feed_id=1,
        )
        assert_matches_type(IndicatorFeedPermissionsRemoveResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_permissions_remove(self, client: Cloudflare) -> None:
        response = client.intel.indicator_feeds.with_raw_response.permissions_remove(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = response.parse()
        assert_matches_type(IndicatorFeedPermissionsRemoveResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_permissions_remove(self, client: Cloudflare) -> None:
        with client.intel.indicator_feeds.with_streaming_response.permissions_remove(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = response.parse()
            assert_matches_type(IndicatorFeedPermissionsRemoveResponse, indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_permissions_remove(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.intel.indicator_feeds.with_raw_response.permissions_remove(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_permissions_view(self, client: Cloudflare) -> None:
        indicator_feed = client.intel.indicator_feeds.permissions_view(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IndicatorFeedPermissionsViewResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_permissions_view(self, client: Cloudflare) -> None:
        response = client.intel.indicator_feeds.with_raw_response.permissions_view(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = response.parse()
        assert_matches_type(IndicatorFeedPermissionsViewResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_permissions_view(self, client: Cloudflare) -> None:
        with client.intel.indicator_feeds.with_streaming_response.permissions_view(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = response.parse()
            assert_matches_type(IndicatorFeedPermissionsViewResponse, indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_permissions_view(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.intel.indicator_feeds.with_raw_response.permissions_view(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_snapshot(self, client: Cloudflare) -> None:
        indicator_feed = client.intel.indicator_feeds.snapshot(
            12,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IndicatorFeedSnapshotResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_snapshot_with_all_params(self, client: Cloudflare) -> None:
        indicator_feed = client.intel.indicator_feeds.snapshot(
            12,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            source="@/Users/me/test.stix2",
        )
        assert_matches_type(IndicatorFeedSnapshotResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_snapshot(self, client: Cloudflare) -> None:
        response = client.intel.indicator_feeds.with_raw_response.snapshot(
            12,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = response.parse()
        assert_matches_type(IndicatorFeedSnapshotResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_snapshot(self, client: Cloudflare) -> None:
        with client.intel.indicator_feeds.with_streaming_response.snapshot(
            12,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = response.parse()
            assert_matches_type(IndicatorFeedSnapshotResponse, indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_snapshot(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.intel.indicator_feeds.with_raw_response.snapshot(
                12,
                account_identifier="",
            )


class TestAsyncIndicatorFeeds:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        indicator_feed = await async_client.intel.indicator_feeds.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IndicatorFeedCreateResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        indicator_feed = await async_client.intel.indicator_feeds.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            description="example feed description",
            name="example_feed_1",
        )
        assert_matches_type(IndicatorFeedCreateResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.indicator_feeds.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = await response.parse()
        assert_matches_type(IndicatorFeedCreateResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.indicator_feeds.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = await response.parse()
            assert_matches_type(IndicatorFeedCreateResponse, indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.intel.indicator_feeds.with_raw_response.create(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        indicator_feed = await async_client.intel.indicator_feeds.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IndicatorFeedListResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.indicator_feeds.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = await response.parse()
        assert_matches_type(IndicatorFeedListResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.indicator_feeds.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = await response.parse()
            assert_matches_type(IndicatorFeedListResponse, indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.intel.indicator_feeds.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_data(self, async_client: AsyncCloudflare) -> None:
        indicator_feed = await async_client.intel.indicator_feeds.data(
            12,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(str, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_data(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.indicator_feeds.with_raw_response.data(
            12,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = await response.parse()
        assert_matches_type(str, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_data(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.indicator_feeds.with_streaming_response.data(
            12,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = await response.parse()
            assert_matches_type(str, indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_data(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.intel.indicator_feeds.with_raw_response.data(
                12,
                account_identifier="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        indicator_feed = await async_client.intel.indicator_feeds.get(
            12,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IndicatorFeedGetResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.indicator_feeds.with_raw_response.get(
            12,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = await response.parse()
        assert_matches_type(IndicatorFeedGetResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.indicator_feeds.with_streaming_response.get(
            12,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = await response.parse()
            assert_matches_type(IndicatorFeedGetResponse, indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.intel.indicator_feeds.with_raw_response.get(
                12,
                account_identifier="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_permissions_add(self, async_client: AsyncCloudflare) -> None:
        indicator_feed = await async_client.intel.indicator_feeds.permissions_add(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IndicatorFeedPermissionsAddResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_permissions_add_with_all_params(self, async_client: AsyncCloudflare) -> None:
        indicator_feed = await async_client.intel.indicator_feeds.permissions_add(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_tag="823f45f16fd2f7e21e1e054aga4d2859",
            feed_id=1,
        )
        assert_matches_type(IndicatorFeedPermissionsAddResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_permissions_add(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.indicator_feeds.with_raw_response.permissions_add(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = await response.parse()
        assert_matches_type(IndicatorFeedPermissionsAddResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_permissions_add(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.indicator_feeds.with_streaming_response.permissions_add(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = await response.parse()
            assert_matches_type(IndicatorFeedPermissionsAddResponse, indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_permissions_add(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.intel.indicator_feeds.with_raw_response.permissions_add(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_permissions_remove(self, async_client: AsyncCloudflare) -> None:
        indicator_feed = await async_client.intel.indicator_feeds.permissions_remove(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IndicatorFeedPermissionsRemoveResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_permissions_remove_with_all_params(self, async_client: AsyncCloudflare) -> None:
        indicator_feed = await async_client.intel.indicator_feeds.permissions_remove(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_tag="823f45f16fd2f7e21e1e054aga4d2859",
            feed_id=1,
        )
        assert_matches_type(IndicatorFeedPermissionsRemoveResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_permissions_remove(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.indicator_feeds.with_raw_response.permissions_remove(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = await response.parse()
        assert_matches_type(IndicatorFeedPermissionsRemoveResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_permissions_remove(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.indicator_feeds.with_streaming_response.permissions_remove(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = await response.parse()
            assert_matches_type(IndicatorFeedPermissionsRemoveResponse, indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_permissions_remove(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.intel.indicator_feeds.with_raw_response.permissions_remove(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_permissions_view(self, async_client: AsyncCloudflare) -> None:
        indicator_feed = await async_client.intel.indicator_feeds.permissions_view(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IndicatorFeedPermissionsViewResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_permissions_view(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.indicator_feeds.with_raw_response.permissions_view(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = await response.parse()
        assert_matches_type(IndicatorFeedPermissionsViewResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_permissions_view(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.indicator_feeds.with_streaming_response.permissions_view(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = await response.parse()
            assert_matches_type(IndicatorFeedPermissionsViewResponse, indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_permissions_view(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.intel.indicator_feeds.with_raw_response.permissions_view(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_snapshot(self, async_client: AsyncCloudflare) -> None:
        indicator_feed = await async_client.intel.indicator_feeds.snapshot(
            12,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IndicatorFeedSnapshotResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_snapshot_with_all_params(self, async_client: AsyncCloudflare) -> None:
        indicator_feed = await async_client.intel.indicator_feeds.snapshot(
            12,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            source="@/Users/me/test.stix2",
        )
        assert_matches_type(IndicatorFeedSnapshotResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_snapshot(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.indicator_feeds.with_raw_response.snapshot(
            12,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        indicator_feed = await response.parse()
        assert_matches_type(IndicatorFeedSnapshotResponse, indicator_feed, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_snapshot(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.indicator_feeds.with_streaming_response.snapshot(
            12,
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            indicator_feed = await response.parse()
            assert_matches_type(IndicatorFeedSnapshotResponse, indicator_feed, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_snapshot(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.intel.indicator_feeds.with_raw_response.snapshot(
                12,
                account_identifier="",
            )
