# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.r2.buckets import EventNotificationGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEventNotifications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        event_notification = client.r2.buckets.event_notifications.update(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert_matches_type(object, event_notification, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        event_notification = client.r2.buckets.event_notifications.update(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
            rules=[
                {
                    "actions": ["PutObject", "CopyObject"],
                    "description": "Notifications from source bucket to queue",
                    "prefix": "img/",
                    "suffix": ".jpeg",
                }
            ],
            jurisdiction="default",
        )
        assert_matches_type(object, event_notification, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.r2.buckets.event_notifications.with_raw_response.update(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_notification = response.parse()
        assert_matches_type(object, event_notification, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.r2.buckets.event_notifications.with_streaming_response.update(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_notification = response.parse()
            assert_matches_type(object, event_notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.buckets.event_notifications.with_raw_response.update(
                queue_id="queue_id",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2.buckets.event_notifications.with_raw_response.update(
                queue_id="queue_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.r2.buckets.event_notifications.with_raw_response.update(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        event_notification = client.r2.buckets.event_notifications.delete(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert_matches_type(object, event_notification, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        event_notification = client.r2.buckets.event_notifications.delete(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
            jurisdiction="default",
        )
        assert_matches_type(object, event_notification, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.r2.buckets.event_notifications.with_raw_response.delete(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_notification = response.parse()
        assert_matches_type(object, event_notification, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.r2.buckets.event_notifications.with_streaming_response.delete(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_notification = response.parse()
            assert_matches_type(object, event_notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.buckets.event_notifications.with_raw_response.delete(
                queue_id="queue_id",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2.buckets.event_notifications.with_raw_response.delete(
                queue_id="queue_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.r2.buckets.event_notifications.with_raw_response.delete(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        event_notification = client.r2.buckets.event_notifications.get(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(EventNotificationGetResponse, event_notification, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        event_notification = client.r2.buckets.event_notifications.get(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            jurisdiction="default",
        )
        assert_matches_type(EventNotificationGetResponse, event_notification, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.r2.buckets.event_notifications.with_raw_response.get(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_notification = response.parse()
        assert_matches_type(EventNotificationGetResponse, event_notification, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.r2.buckets.event_notifications.with_streaming_response.get(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_notification = response.parse()
            assert_matches_type(EventNotificationGetResponse, event_notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2.buckets.event_notifications.with_raw_response.get(
                bucket_name="example-bucket",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2.buckets.event_notifications.with_raw_response.get(
                bucket_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncEventNotifications:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        event_notification = await async_client.r2.buckets.event_notifications.update(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert_matches_type(object, event_notification, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        event_notification = await async_client.r2.buckets.event_notifications.update(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
            rules=[
                {
                    "actions": ["PutObject", "CopyObject"],
                    "description": "Notifications from source bucket to queue",
                    "prefix": "img/",
                    "suffix": ".jpeg",
                }
            ],
            jurisdiction="default",
        )
        assert_matches_type(object, event_notification, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.buckets.event_notifications.with_raw_response.update(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_notification = await response.parse()
        assert_matches_type(object, event_notification, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.buckets.event_notifications.with_streaming_response.update(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_notification = await response.parse()
            assert_matches_type(object, event_notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.buckets.event_notifications.with_raw_response.update(
                queue_id="queue_id",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2.buckets.event_notifications.with_raw_response.update(
                queue_id="queue_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.r2.buckets.event_notifications.with_raw_response.update(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        event_notification = await async_client.r2.buckets.event_notifications.delete(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )
        assert_matches_type(object, event_notification, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        event_notification = await async_client.r2.buckets.event_notifications.delete(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
            jurisdiction="default",
        )
        assert_matches_type(object, event_notification, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.buckets.event_notifications.with_raw_response.delete(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_notification = await response.parse()
        assert_matches_type(object, event_notification, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.buckets.event_notifications.with_streaming_response.delete(
            queue_id="queue_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            bucket_name="example-bucket",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_notification = await response.parse()
            assert_matches_type(object, event_notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.buckets.event_notifications.with_raw_response.delete(
                queue_id="queue_id",
                account_id="",
                bucket_name="example-bucket",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2.buckets.event_notifications.with_raw_response.delete(
                queue_id="queue_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.r2.buckets.event_notifications.with_raw_response.delete(
                queue_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                bucket_name="example-bucket",
            )

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        event_notification = await async_client.r2.buckets.event_notifications.get(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(EventNotificationGetResponse, event_notification, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        event_notification = await async_client.r2.buckets.event_notifications.get(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            jurisdiction="default",
        )
        assert_matches_type(EventNotificationGetResponse, event_notification, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2.buckets.event_notifications.with_raw_response.get(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_notification = await response.parse()
        assert_matches_type(EventNotificationGetResponse, event_notification, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2.buckets.event_notifications.with_streaming_response.get(
            bucket_name="example-bucket",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_notification = await response.parse()
            assert_matches_type(EventNotificationGetResponse, event_notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2.buckets.event_notifications.with_raw_response.get(
                bucket_name="example-bucket",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2.buckets.event_notifications.with_raw_response.get(
                bucket_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
