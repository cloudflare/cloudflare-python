# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.workers.observability import (
    DestinationListResponse,
    DestinationCreateResponse,
    DestinationDeleteResponse,
    DestinationUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDestinations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        destination = client.workers.observability.destinations.create(
            account_id="account_id",
            configuration={
                "headers": {"foo": "string"},
                "logpush_dataset": "opentelemetry-traces",
                "type": "logpush",
                "url": "url",
            },
            enabled=True,
            name="name",
        )
        assert_matches_type(DestinationCreateResponse, destination, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        destination = client.workers.observability.destinations.create(
            account_id="account_id",
            configuration={
                "headers": {"foo": "string"},
                "logpush_dataset": "opentelemetry-traces",
                "type": "logpush",
                "url": "url",
            },
            enabled=True,
            name="name",
            skip_preflight_check=True,
        )
        assert_matches_type(DestinationCreateResponse, destination, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.workers.observability.destinations.with_raw_response.create(
            account_id="account_id",
            configuration={
                "headers": {"foo": "string"},
                "logpush_dataset": "opentelemetry-traces",
                "type": "logpush",
                "url": "url",
            },
            enabled=True,
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        destination = response.parse()
        assert_matches_type(DestinationCreateResponse, destination, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.workers.observability.destinations.with_streaming_response.create(
            account_id="account_id",
            configuration={
                "headers": {"foo": "string"},
                "logpush_dataset": "opentelemetry-traces",
                "type": "logpush",
                "url": "url",
            },
            enabled=True,
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            destination = response.parse()
            assert_matches_type(DestinationCreateResponse, destination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.observability.destinations.with_raw_response.create(
                account_id="",
                configuration={
                    "headers": {"foo": "string"},
                    "logpush_dataset": "opentelemetry-traces",
                    "type": "logpush",
                    "url": "url",
                },
                enabled=True,
                name="name",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        destination = client.workers.observability.destinations.update(
            slug="slug",
            account_id="account_id",
            configuration={
                "headers": {"foo": "string"},
                "type": "logpush",
                "url": "url",
            },
            enabled=True,
        )
        assert_matches_type(DestinationUpdateResponse, destination, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.workers.observability.destinations.with_raw_response.update(
            slug="slug",
            account_id="account_id",
            configuration={
                "headers": {"foo": "string"},
                "type": "logpush",
                "url": "url",
            },
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        destination = response.parse()
        assert_matches_type(DestinationUpdateResponse, destination, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.workers.observability.destinations.with_streaming_response.update(
            slug="slug",
            account_id="account_id",
            configuration={
                "headers": {"foo": "string"},
                "type": "logpush",
                "url": "url",
            },
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            destination = response.parse()
            assert_matches_type(DestinationUpdateResponse, destination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.observability.destinations.with_raw_response.update(
                slug="slug",
                account_id="",
                configuration={
                    "headers": {"foo": "string"},
                    "type": "logpush",
                    "url": "url",
                },
                enabled=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.workers.observability.destinations.with_raw_response.update(
                slug="",
                account_id="account_id",
                configuration={
                    "headers": {"foo": "string"},
                    "type": "logpush",
                    "url": "url",
                },
                enabled=True,
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        destination = client.workers.observability.destinations.list(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[DestinationListResponse], destination, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        destination = client.workers.observability.destinations.list(
            account_id="account_id",
            order="asc",
            order_by="created",
            page=1,
            per_page=5,
        )
        assert_matches_type(SyncSinglePage[DestinationListResponse], destination, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.workers.observability.destinations.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        destination = response.parse()
        assert_matches_type(SyncSinglePage[DestinationListResponse], destination, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.workers.observability.destinations.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            destination = response.parse()
            assert_matches_type(SyncSinglePage[DestinationListResponse], destination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.observability.destinations.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        destination = client.workers.observability.destinations.delete(
            slug="slug",
            account_id="account_id",
        )
        assert_matches_type(Optional[DestinationDeleteResponse], destination, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.workers.observability.destinations.with_raw_response.delete(
            slug="slug",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        destination = response.parse()
        assert_matches_type(Optional[DestinationDeleteResponse], destination, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.workers.observability.destinations.with_streaming_response.delete(
            slug="slug",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            destination = response.parse()
            assert_matches_type(Optional[DestinationDeleteResponse], destination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.observability.destinations.with_raw_response.delete(
                slug="slug",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            client.workers.observability.destinations.with_raw_response.delete(
                slug="",
                account_id="account_id",
            )


class TestAsyncDestinations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        destination = await async_client.workers.observability.destinations.create(
            account_id="account_id",
            configuration={
                "headers": {"foo": "string"},
                "logpush_dataset": "opentelemetry-traces",
                "type": "logpush",
                "url": "url",
            },
            enabled=True,
            name="name",
        )
        assert_matches_type(DestinationCreateResponse, destination, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        destination = await async_client.workers.observability.destinations.create(
            account_id="account_id",
            configuration={
                "headers": {"foo": "string"},
                "logpush_dataset": "opentelemetry-traces",
                "type": "logpush",
                "url": "url",
            },
            enabled=True,
            name="name",
            skip_preflight_check=True,
        )
        assert_matches_type(DestinationCreateResponse, destination, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.observability.destinations.with_raw_response.create(
            account_id="account_id",
            configuration={
                "headers": {"foo": "string"},
                "logpush_dataset": "opentelemetry-traces",
                "type": "logpush",
                "url": "url",
            },
            enabled=True,
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        destination = await response.parse()
        assert_matches_type(DestinationCreateResponse, destination, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.observability.destinations.with_streaming_response.create(
            account_id="account_id",
            configuration={
                "headers": {"foo": "string"},
                "logpush_dataset": "opentelemetry-traces",
                "type": "logpush",
                "url": "url",
            },
            enabled=True,
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            destination = await response.parse()
            assert_matches_type(DestinationCreateResponse, destination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.observability.destinations.with_raw_response.create(
                account_id="",
                configuration={
                    "headers": {"foo": "string"},
                    "logpush_dataset": "opentelemetry-traces",
                    "type": "logpush",
                    "url": "url",
                },
                enabled=True,
                name="name",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        destination = await async_client.workers.observability.destinations.update(
            slug="slug",
            account_id="account_id",
            configuration={
                "headers": {"foo": "string"},
                "type": "logpush",
                "url": "url",
            },
            enabled=True,
        )
        assert_matches_type(DestinationUpdateResponse, destination, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.observability.destinations.with_raw_response.update(
            slug="slug",
            account_id="account_id",
            configuration={
                "headers": {"foo": "string"},
                "type": "logpush",
                "url": "url",
            },
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        destination = await response.parse()
        assert_matches_type(DestinationUpdateResponse, destination, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.observability.destinations.with_streaming_response.update(
            slug="slug",
            account_id="account_id",
            configuration={
                "headers": {"foo": "string"},
                "type": "logpush",
                "url": "url",
            },
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            destination = await response.parse()
            assert_matches_type(DestinationUpdateResponse, destination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.observability.destinations.with_raw_response.update(
                slug="slug",
                account_id="",
                configuration={
                    "headers": {"foo": "string"},
                    "type": "logpush",
                    "url": "url",
                },
                enabled=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.workers.observability.destinations.with_raw_response.update(
                slug="",
                account_id="account_id",
                configuration={
                    "headers": {"foo": "string"},
                    "type": "logpush",
                    "url": "url",
                },
                enabled=True,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        destination = await async_client.workers.observability.destinations.list(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[DestinationListResponse], destination, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        destination = await async_client.workers.observability.destinations.list(
            account_id="account_id",
            order="asc",
            order_by="created",
            page=1,
            per_page=5,
        )
        assert_matches_type(AsyncSinglePage[DestinationListResponse], destination, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.observability.destinations.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        destination = await response.parse()
        assert_matches_type(AsyncSinglePage[DestinationListResponse], destination, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.observability.destinations.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            destination = await response.parse()
            assert_matches_type(AsyncSinglePage[DestinationListResponse], destination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.observability.destinations.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        destination = await async_client.workers.observability.destinations.delete(
            slug="slug",
            account_id="account_id",
        )
        assert_matches_type(Optional[DestinationDeleteResponse], destination, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.observability.destinations.with_raw_response.delete(
            slug="slug",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        destination = await response.parse()
        assert_matches_type(Optional[DestinationDeleteResponse], destination, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.observability.destinations.with_streaming_response.delete(
            slug="slug",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            destination = await response.parse()
            assert_matches_type(Optional[DestinationDeleteResponse], destination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.observability.destinations.with_raw_response.delete(
                slug="slug",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `slug` but received ''"):
            await async_client.workers.observability.destinations.with_raw_response.delete(
                slug="",
                account_id="account_id",
            )
