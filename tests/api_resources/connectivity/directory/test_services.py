# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        service = client.connectivity.directory.services.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host={},
            name="name",
            type="http",
        )
        assert service is None

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        service = client.connectivity.directory.services.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host={
                "hostname": "hostname",
                "ipv4": "ipv4",
                "ipv6": "ipv6",
                "network": {},
                "resolver_network": {},
            },
            name="name",
            type="http",
            http_port=1,
            https_port=1,
        )
        assert service is None

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.connectivity.directory.services.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host={},
            name="name",
            type="http",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert service is None

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.connectivity.directory.services.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host={},
            name="name",
            type="http",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert service is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.connectivity.directory.services.with_raw_response.create(
                account_id="",
                host={},
                name="name",
                type="http",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        service = client.connectivity.directory.services.update(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            host={},
            name="name",
            type="http",
        )
        assert service is None

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        service = client.connectivity.directory.services.update(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            host={
                "hostname": "hostname",
                "ipv4": "ipv4",
                "ipv6": "ipv6",
                "network": {},
                "resolver_network": {},
            },
            name="name",
            type="http",
            http_port=1,
            https_port=1,
        )
        assert service is None

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.connectivity.directory.services.with_raw_response.update(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            host={},
            name="name",
            type="http",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert service is None

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.connectivity.directory.services.with_streaming_response.update(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            host={},
            name="name",
            type="http",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert service is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.connectivity.directory.services.with_raw_response.update(
                service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                host={},
                name="name",
                type="http",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_id` but received ''"):
            client.connectivity.directory.services.with_raw_response.update(
                service_id="",
                account_id="account_id",
                host={},
                name="name",
                type="http",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        service = client.connectivity.directory.services.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert service is None

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        service = client.connectivity.directory.services.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=1,
            type="http",
        )
        assert service is None

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.connectivity.directory.services.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert service is None

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.connectivity.directory.services.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert service is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.connectivity.directory.services.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        service = client.connectivity.directory.services.delete(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert service is None

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.connectivity.directory.services.with_raw_response.delete(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert service is None

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.connectivity.directory.services.with_streaming_response.delete(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert service is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.connectivity.directory.services.with_raw_response.delete(
                service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_id` but received ''"):
            client.connectivity.directory.services.with_raw_response.delete(
                service_id="",
                account_id="account_id",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        service = client.connectivity.directory.services.get(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert service is None

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.connectivity.directory.services.with_raw_response.get(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert service is None

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.connectivity.directory.services.with_streaming_response.get(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert service is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.connectivity.directory.services.with_raw_response.get(
                service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_id` but received ''"):
            client.connectivity.directory.services.with_raw_response.get(
                service_id="",
                account_id="account_id",
            )


class TestAsyncServices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        service = await async_client.connectivity.directory.services.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host={},
            name="name",
            type="http",
        )
        assert service is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        service = await async_client.connectivity.directory.services.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host={
                "hostname": "hostname",
                "ipv4": "ipv4",
                "ipv6": "ipv6",
                "network": {},
                "resolver_network": {},
            },
            name="name",
            type="http",
            http_port=1,
            https_port=1,
        )
        assert service is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.connectivity.directory.services.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host={},
            name="name",
            type="http",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert service is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.connectivity.directory.services.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host={},
            name="name",
            type="http",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert service is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.connectivity.directory.services.with_raw_response.create(
                account_id="",
                host={},
                name="name",
                type="http",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        service = await async_client.connectivity.directory.services.update(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            host={},
            name="name",
            type="http",
        )
        assert service is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        service = await async_client.connectivity.directory.services.update(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            host={
                "hostname": "hostname",
                "ipv4": "ipv4",
                "ipv6": "ipv6",
                "network": {},
                "resolver_network": {},
            },
            name="name",
            type="http",
            http_port=1,
            https_port=1,
        )
        assert service is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.connectivity.directory.services.with_raw_response.update(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            host={},
            name="name",
            type="http",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert service is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.connectivity.directory.services.with_streaming_response.update(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            host={},
            name="name",
            type="http",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert service is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.connectivity.directory.services.with_raw_response.update(
                service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                host={},
                name="name",
                type="http",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_id` but received ''"):
            await async_client.connectivity.directory.services.with_raw_response.update(
                service_id="",
                account_id="account_id",
                host={},
                name="name",
                type="http",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        service = await async_client.connectivity.directory.services.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert service is None

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        service = await async_client.connectivity.directory.services.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=1,
            type="http",
        )
        assert service is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.connectivity.directory.services.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert service is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.connectivity.directory.services.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert service is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.connectivity.directory.services.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        service = await async_client.connectivity.directory.services.delete(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert service is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.connectivity.directory.services.with_raw_response.delete(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert service is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.connectivity.directory.services.with_streaming_response.delete(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert service is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.connectivity.directory.services.with_raw_response.delete(
                service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_id` but received ''"):
            await async_client.connectivity.directory.services.with_raw_response.delete(
                service_id="",
                account_id="account_id",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        service = await async_client.connectivity.directory.services.get(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert service is None

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.connectivity.directory.services.with_raw_response.get(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert service is None

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.connectivity.directory.services.with_streaming_response.get(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert service is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.connectivity.directory.services.with_raw_response.get(
                service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_id` but received ''"):
            await async_client.connectivity.directory.services.with_raw_response.get(
                service_id="",
                account_id="account_id",
            )
