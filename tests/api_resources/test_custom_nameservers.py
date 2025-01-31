# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.custom_nameservers import (
    CustomNameserver,
    CustomNameserverDeleteResponse,
    CustomNameserverAvailabiltyResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomNameservers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        custom_nameserver = client.custom_nameservers.create(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            ns_name="ns1.example.com",
        )
        assert_matches_type(Optional[CustomNameserver], custom_nameserver, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        custom_nameserver = client.custom_nameservers.create(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            ns_name="ns1.example.com",
            ns_set=1,
        )
        assert_matches_type(Optional[CustomNameserver], custom_nameserver, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.custom_nameservers.with_raw_response.create(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            ns_name="ns1.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_nameserver = response.parse()
        assert_matches_type(Optional[CustomNameserver], custom_nameserver, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.custom_nameservers.with_streaming_response.create(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            ns_name="ns1.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_nameserver = response.parse()
            assert_matches_type(Optional[CustomNameserver], custom_nameserver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.custom_nameservers.with_raw_response.create(
                account_id="",
                ns_name="ns1.example.com",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        custom_nameserver = client.custom_nameservers.delete(
            custom_ns_id="ns1.example.com",
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        )
        assert_matches_type(SyncSinglePage[CustomNameserverDeleteResponse], custom_nameserver, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.custom_nameservers.with_raw_response.delete(
            custom_ns_id="ns1.example.com",
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_nameserver = response.parse()
        assert_matches_type(SyncSinglePage[CustomNameserverDeleteResponse], custom_nameserver, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.custom_nameservers.with_streaming_response.delete(
            custom_ns_id="ns1.example.com",
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_nameserver = response.parse()
            assert_matches_type(SyncSinglePage[CustomNameserverDeleteResponse], custom_nameserver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.custom_nameservers.with_raw_response.delete(
                custom_ns_id="ns1.example.com",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `custom_ns_id` but received ''"):
            client.custom_nameservers.with_raw_response.delete(
                custom_ns_id="",
                account_id="372e67954025e0ba6aaa6d586b9e0b59",
            )

    @parametrize
    def test_method_availabilty(self, client: Cloudflare) -> None:
        custom_nameserver = client.custom_nameservers.availabilty(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        )
        assert_matches_type(SyncSinglePage[CustomNameserverAvailabiltyResponse], custom_nameserver, path=["response"])

    @parametrize
    def test_raw_response_availabilty(self, client: Cloudflare) -> None:
        response = client.custom_nameservers.with_raw_response.availabilty(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_nameserver = response.parse()
        assert_matches_type(SyncSinglePage[CustomNameserverAvailabiltyResponse], custom_nameserver, path=["response"])

    @parametrize
    def test_streaming_response_availabilty(self, client: Cloudflare) -> None:
        with client.custom_nameservers.with_streaming_response.availabilty(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_nameserver = response.parse()
            assert_matches_type(
                SyncSinglePage[CustomNameserverAvailabiltyResponse], custom_nameserver, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_availabilty(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.custom_nameservers.with_raw_response.availabilty(
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        custom_nameserver = client.custom_nameservers.get(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        )
        assert_matches_type(SyncSinglePage[CustomNameserver], custom_nameserver, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.custom_nameservers.with_raw_response.get(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_nameserver = response.parse()
        assert_matches_type(SyncSinglePage[CustomNameserver], custom_nameserver, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.custom_nameservers.with_streaming_response.get(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_nameserver = response.parse()
            assert_matches_type(SyncSinglePage[CustomNameserver], custom_nameserver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.custom_nameservers.with_raw_response.get(
                account_id="",
            )


class TestAsyncCustomNameservers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        custom_nameserver = await async_client.custom_nameservers.create(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            ns_name="ns1.example.com",
        )
        assert_matches_type(Optional[CustomNameserver], custom_nameserver, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom_nameserver = await async_client.custom_nameservers.create(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            ns_name="ns1.example.com",
            ns_set=1,
        )
        assert_matches_type(Optional[CustomNameserver], custom_nameserver, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_nameservers.with_raw_response.create(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            ns_name="ns1.example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_nameserver = await response.parse()
        assert_matches_type(Optional[CustomNameserver], custom_nameserver, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_nameservers.with_streaming_response.create(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
            ns_name="ns1.example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_nameserver = await response.parse()
            assert_matches_type(Optional[CustomNameserver], custom_nameserver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.custom_nameservers.with_raw_response.create(
                account_id="",
                ns_name="ns1.example.com",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        custom_nameserver = await async_client.custom_nameservers.delete(
            custom_ns_id="ns1.example.com",
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        )
        assert_matches_type(AsyncSinglePage[CustomNameserverDeleteResponse], custom_nameserver, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_nameservers.with_raw_response.delete(
            custom_ns_id="ns1.example.com",
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_nameserver = await response.parse()
        assert_matches_type(AsyncSinglePage[CustomNameserverDeleteResponse], custom_nameserver, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_nameservers.with_streaming_response.delete(
            custom_ns_id="ns1.example.com",
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_nameserver = await response.parse()
            assert_matches_type(AsyncSinglePage[CustomNameserverDeleteResponse], custom_nameserver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.custom_nameservers.with_raw_response.delete(
                custom_ns_id="ns1.example.com",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `custom_ns_id` but received ''"):
            await async_client.custom_nameservers.with_raw_response.delete(
                custom_ns_id="",
                account_id="372e67954025e0ba6aaa6d586b9e0b59",
            )

    @parametrize
    async def test_method_availabilty(self, async_client: AsyncCloudflare) -> None:
        custom_nameserver = await async_client.custom_nameservers.availabilty(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        )
        assert_matches_type(AsyncSinglePage[CustomNameserverAvailabiltyResponse], custom_nameserver, path=["response"])

    @parametrize
    async def test_raw_response_availabilty(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_nameservers.with_raw_response.availabilty(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_nameserver = await response.parse()
        assert_matches_type(AsyncSinglePage[CustomNameserverAvailabiltyResponse], custom_nameserver, path=["response"])

    @parametrize
    async def test_streaming_response_availabilty(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_nameservers.with_streaming_response.availabilty(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_nameserver = await response.parse()
            assert_matches_type(
                AsyncSinglePage[CustomNameserverAvailabiltyResponse], custom_nameserver, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_availabilty(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.custom_nameservers.with_raw_response.availabilty(
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        custom_nameserver = await async_client.custom_nameservers.get(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        )
        assert_matches_type(AsyncSinglePage[CustomNameserver], custom_nameserver, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_nameservers.with_raw_response.get(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_nameserver = await response.parse()
        assert_matches_type(AsyncSinglePage[CustomNameserver], custom_nameserver, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_nameservers.with_streaming_response.get(
            account_id="372e67954025e0ba6aaa6d586b9e0b59",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_nameserver = await response.parse()
            assert_matches_type(AsyncSinglePage[CustomNameserver], custom_nameserver, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.custom_nameservers.with_raw_response.get(
                account_id="",
            )
