# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncCursorPaginationAfter, AsyncCursorPaginationAfter
from cloudflare.types.zero_trust.resource_library import (
    ApplicationGetResponse,
    ApplicationListResponse,
    ApplicationCreateResponse,
    ApplicationUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApplications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Cloudflare) -> None:
        application = client.zero_trust.resource_library.applications.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostnames=["example.com", "foo.com"],
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Cloudflare) -> None:
        application = client.zero_trust.resource_library.applications.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostnames=["example.com", "foo.com"],
            category_id=12,
            human_id="HR",
            ip_subnets=["192.168.1.0/24", "2001:db8::/48"],
            name="HR",
            port_protocols=["tcp/443", "udp/10000-20000"],
            support_domains=["example.com", "foo.com"],
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:
        response = client.zero_trust.resource_library.applications.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostnames=["example.com", "foo.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloudflare) -> None:
        with client.zero_trust.resource_library.applications.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostnames=["example.com", "foo.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.resource_library.applications.with_raw_response.create(
                account_id="",
                hostnames=["example.com", "foo.com"],
            )

    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        application = client.zero_trust.resource_library.applications.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ip_subnets=["192.168.1.0/24", "2001:db8::/48"],
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Cloudflare) -> None:
        application = client.zero_trust.resource_library.applications.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ip_subnets=["192.168.1.0/24", "2001:db8::/48"],
            category_id=12,
            hostnames=["example.com", "foo.com"],
            human_id="HR",
            name="HR",
            port_protocols=["tcp/443", "udp/10000-20000"],
            support_domains=["example.com", "foo.com"],
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:
        response = client.zero_trust.resource_library.applications.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ip_subnets=["192.168.1.0/24", "2001:db8::/48"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloudflare) -> None:
        with client.zero_trust.resource_library.applications.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ip_subnets=["192.168.1.0/24", "2001:db8::/48"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.resource_library.applications.with_raw_response.create(
                account_id="",
                ip_subnets=["192.168.1.0/24", "2001:db8::/48"],
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        application = client.zero_trust.resource_library.applications.update(
            id=498,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        application = client.zero_trust.resource_library.applications.update(
            id=498,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostnames=["example.com", "foo.com"],
            ip_subnets=["192.168.1.0/24", "2001:db8::/48"],
            port_protocols=["tcp/443", "udp/10000-20000"],
            support_domains=["example.com", "foo.com"],
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.resource_library.applications.with_raw_response.update(
            id=498,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.resource_library.applications.with_streaming_response.update(
            id=498,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.resource_library.applications.with_raw_response.update(
                id=498,
                account_id="",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        application = client.zero_trust.resource_library.applications.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncCursorPaginationAfter[ApplicationListResponse], application, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        application = client.zero_trust.resource_library.applications.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cursor="cursor",
            fields="fields",
            filter="filter",
            limit=0,
            lookup="xx",
            offset=0,
            order_by="order_by",
            search="xx",
        )
        assert_matches_type(SyncCursorPaginationAfter[ApplicationListResponse], application, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.resource_library.applications.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(SyncCursorPaginationAfter[ApplicationListResponse], application, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.resource_library.applications.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(SyncCursorPaginationAfter[ApplicationListResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.resource_library.applications.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        application = client.zero_trust.resource_library.applications.delete(
            id=498,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, application, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.resource_library.applications.with_raw_response.delete(
            id=498,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(object, application, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.resource_library.applications.with_streaming_response.delete(
            id=498,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(object, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.resource_library.applications.with_raw_response.delete(
                id=498,
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        application = client.zero_trust.resource_library.applications.get(
            id=498,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ApplicationGetResponse], application, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.resource_library.applications.with_raw_response.get(
            id=498,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(Optional[ApplicationGetResponse], application, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.resource_library.applications.with_streaming_response.get(
            id=498,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(Optional[ApplicationGetResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.resource_library.applications.with_raw_response.get(
                id=498,
                account_id="",
            )


class TestAsyncApplications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.resource_library.applications.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostnames=["example.com", "foo.com"],
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.resource_library.applications.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostnames=["example.com", "foo.com"],
            category_id=12,
            human_id="HR",
            ip_subnets=["192.168.1.0/24", "2001:db8::/48"],
            name="HR",
            port_protocols=["tcp/443", "udp/10000-20000"],
            support_domains=["example.com", "foo.com"],
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.resource_library.applications.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostnames=["example.com", "foo.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.resource_library.applications.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostnames=["example.com", "foo.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.resource_library.applications.with_raw_response.create(
                account_id="",
                hostnames=["example.com", "foo.com"],
            )

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.resource_library.applications.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ip_subnets=["192.168.1.0/24", "2001:db8::/48"],
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.resource_library.applications.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ip_subnets=["192.168.1.0/24", "2001:db8::/48"],
            category_id=12,
            hostnames=["example.com", "foo.com"],
            human_id="HR",
            name="HR",
            port_protocols=["tcp/443", "udp/10000-20000"],
            support_domains=["example.com", "foo.com"],
        )
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.resource_library.applications.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ip_subnets=["192.168.1.0/24", "2001:db8::/48"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.resource_library.applications.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ip_subnets=["192.168.1.0/24", "2001:db8::/48"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationCreateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.resource_library.applications.with_raw_response.create(
                account_id="",
                ip_subnets=["192.168.1.0/24", "2001:db8::/48"],
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.resource_library.applications.update(
            id=498,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.resource_library.applications.update(
            id=498,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostnames=["example.com", "foo.com"],
            ip_subnets=["192.168.1.0/24", "2001:db8::/48"],
            port_protocols=["tcp/443", "udp/10000-20000"],
            support_domains=["example.com", "foo.com"],
        )
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.resource_library.applications.with_raw_response.update(
            id=498,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.resource_library.applications.with_streaming_response.update(
            id=498,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationUpdateResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.resource_library.applications.with_raw_response.update(
                id=498,
                account_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.resource_library.applications.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncCursorPaginationAfter[ApplicationListResponse], application, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.resource_library.applications.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cursor="cursor",
            fields="fields",
            filter="filter",
            limit=0,
            lookup="xx",
            offset=0,
            order_by="order_by",
            search="xx",
        )
        assert_matches_type(AsyncCursorPaginationAfter[ApplicationListResponse], application, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.resource_library.applications.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(AsyncCursorPaginationAfter[ApplicationListResponse], application, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.resource_library.applications.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(AsyncCursorPaginationAfter[ApplicationListResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.resource_library.applications.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.resource_library.applications.delete(
            id=498,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(object, application, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.resource_library.applications.with_raw_response.delete(
            id=498,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(object, application, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.resource_library.applications.with_streaming_response.delete(
            id=498,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(object, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.resource_library.applications.with_raw_response.delete(
                id=498,
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        application = await async_client.zero_trust.resource_library.applications.get(
            id=498,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ApplicationGetResponse], application, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.resource_library.applications.with_raw_response.get(
            id=498,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(Optional[ApplicationGetResponse], application, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.resource_library.applications.with_streaming_response.get(
            id=498,
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(Optional[ApplicationGetResponse], application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.resource_library.applications.with_raw_response.get(
                id=498,
                account_id="",
            )
