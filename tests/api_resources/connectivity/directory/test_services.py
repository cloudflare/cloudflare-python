# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.connectivity.directory import (
    ServiceGetResponse,
    ServiceListResponse,
    ServiceCreateResponse,
    ServiceUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Cloudflare) -> None:
        service = client.connectivity.directory.services.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="web-app",
            type="http",
        )
        assert_matches_type(Optional[ServiceCreateResponse], service, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Cloudflare) -> None:
        service = client.connectivity.directory.services.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="web-app",
            type="http",
            http_port=8080,
            https_port=8443,
            tls_settings={"cert_verification_mode": "verify_full"},
        )
        assert_matches_type(Optional[ServiceCreateResponse], service, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:
        response = client.connectivity.directory.services.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="web-app",
            type="http",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(Optional[ServiceCreateResponse], service, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloudflare) -> None:
        with client.connectivity.directory.services.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="web-app",
            type="http",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(Optional[ServiceCreateResponse], service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.connectivity.directory.services.with_raw_response.create(
                account_id="",
                host={
                    "ipv4": "10.0.0.1",
                    "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
                },
                name="web-app",
                type="http",
            )

    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        service = client.connectivity.directory.services.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="postgres-db",
            type="tcp",
        )
        assert_matches_type(Optional[ServiceCreateResponse], service, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Cloudflare) -> None:
        service = client.connectivity.directory.services.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="postgres-db",
            type="tcp",
            app_protocol="postgresql",
            tcp_port=5432,
            tls_settings={"cert_verification_mode": "verify_full"},
        )
        assert_matches_type(Optional[ServiceCreateResponse], service, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:
        response = client.connectivity.directory.services.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="postgres-db",
            type="tcp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(Optional[ServiceCreateResponse], service, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloudflare) -> None:
        with client.connectivity.directory.services.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="postgres-db",
            type="tcp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(Optional[ServiceCreateResponse], service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.connectivity.directory.services.with_raw_response.create(
                account_id="",
                host={
                    "ipv4": "10.0.0.1",
                    "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
                },
                name="postgres-db",
                type="tcp",
            )

    @parametrize
    def test_method_update_overload_1(self, client: Cloudflare) -> None:
        service = client.connectivity.directory.services.update(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="web-app",
            type="http",
        )
        assert_matches_type(Optional[ServiceUpdateResponse], service, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Cloudflare) -> None:
        service = client.connectivity.directory.services.update(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="web-app",
            type="http",
            http_port=8080,
            https_port=8443,
            tls_settings={"cert_verification_mode": "verify_full"},
        )
        assert_matches_type(Optional[ServiceUpdateResponse], service, path=["response"])

    @parametrize
    def test_raw_response_update_overload_1(self, client: Cloudflare) -> None:
        response = client.connectivity.directory.services.with_raw_response.update(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="web-app",
            type="http",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(Optional[ServiceUpdateResponse], service, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_1(self, client: Cloudflare) -> None:
        with client.connectivity.directory.services.with_streaming_response.update(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="web-app",
            type="http",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(Optional[ServiceUpdateResponse], service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.connectivity.directory.services.with_raw_response.update(
                service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                host={
                    "ipv4": "10.0.0.1",
                    "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
                },
                name="web-app",
                type="http",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_id` but received ''"):
            client.connectivity.directory.services.with_raw_response.update(
                service_id="",
                account_id="account_id",
                host={
                    "ipv4": "10.0.0.1",
                    "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
                },
                name="web-app",
                type="http",
            )

    @parametrize
    def test_method_update_overload_2(self, client: Cloudflare) -> None:
        service = client.connectivity.directory.services.update(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="postgres-db",
            type="tcp",
        )
        assert_matches_type(Optional[ServiceUpdateResponse], service, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Cloudflare) -> None:
        service = client.connectivity.directory.services.update(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="postgres-db",
            type="tcp",
            app_protocol="postgresql",
            tcp_port=5432,
            tls_settings={"cert_verification_mode": "verify_full"},
        )
        assert_matches_type(Optional[ServiceUpdateResponse], service, path=["response"])

    @parametrize
    def test_raw_response_update_overload_2(self, client: Cloudflare) -> None:
        response = client.connectivity.directory.services.with_raw_response.update(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="postgres-db",
            type="tcp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(Optional[ServiceUpdateResponse], service, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_2(self, client: Cloudflare) -> None:
        with client.connectivity.directory.services.with_streaming_response.update(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="postgres-db",
            type="tcp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(Optional[ServiceUpdateResponse], service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.connectivity.directory.services.with_raw_response.update(
                service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                host={
                    "ipv4": "10.0.0.1",
                    "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
                },
                name="postgres-db",
                type="tcp",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_id` but received ''"):
            client.connectivity.directory.services.with_raw_response.update(
                service_id="",
                account_id="account_id",
                host={
                    "ipv4": "10.0.0.1",
                    "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
                },
                name="postgres-db",
                type="tcp",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        service = client.connectivity.directory.services.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[ServiceListResponse], service, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        service = client.connectivity.directory.services.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=1,
            type="tcp",
        )
        assert_matches_type(SyncV4PagePaginationArray[ServiceListResponse], service, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.connectivity.directory.services.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[ServiceListResponse], service, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.connectivity.directory.services.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[ServiceListResponse], service, path=["response"])

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
        assert_matches_type(Optional[ServiceGetResponse], service, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.connectivity.directory.services.with_raw_response.get(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(Optional[ServiceGetResponse], service, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.connectivity.directory.services.with_streaming_response.get(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(Optional[ServiceGetResponse], service, path=["response"])

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
    async def test_method_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        service = await async_client.connectivity.directory.services.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="web-app",
            type="http",
        )
        assert_matches_type(Optional[ServiceCreateResponse], service, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        service = await async_client.connectivity.directory.services.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="web-app",
            type="http",
            http_port=8080,
            https_port=8443,
            tls_settings={"cert_verification_mode": "verify_full"},
        )
        assert_matches_type(Optional[ServiceCreateResponse], service, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.connectivity.directory.services.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="web-app",
            type="http",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(Optional[ServiceCreateResponse], service, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.connectivity.directory.services.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="web-app",
            type="http",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(Optional[ServiceCreateResponse], service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.connectivity.directory.services.with_raw_response.create(
                account_id="",
                host={
                    "ipv4": "10.0.0.1",
                    "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
                },
                name="web-app",
                type="http",
            )

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        service = await async_client.connectivity.directory.services.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="postgres-db",
            type="tcp",
        )
        assert_matches_type(Optional[ServiceCreateResponse], service, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        service = await async_client.connectivity.directory.services.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="postgres-db",
            type="tcp",
            app_protocol="postgresql",
            tcp_port=5432,
            tls_settings={"cert_verification_mode": "verify_full"},
        )
        assert_matches_type(Optional[ServiceCreateResponse], service, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.connectivity.directory.services.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="postgres-db",
            type="tcp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(Optional[ServiceCreateResponse], service, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.connectivity.directory.services.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="postgres-db",
            type="tcp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(Optional[ServiceCreateResponse], service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.connectivity.directory.services.with_raw_response.create(
                account_id="",
                host={
                    "ipv4": "10.0.0.1",
                    "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
                },
                name="postgres-db",
                type="tcp",
            )

    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        service = await async_client.connectivity.directory.services.update(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="web-app",
            type="http",
        )
        assert_matches_type(Optional[ServiceUpdateResponse], service, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        service = await async_client.connectivity.directory.services.update(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="web-app",
            type="http",
            http_port=8080,
            https_port=8443,
            tls_settings={"cert_verification_mode": "verify_full"},
        )
        assert_matches_type(Optional[ServiceUpdateResponse], service, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.connectivity.directory.services.with_raw_response.update(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="web-app",
            type="http",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(Optional[ServiceUpdateResponse], service, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.connectivity.directory.services.with_streaming_response.update(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="web-app",
            type="http",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(Optional[ServiceUpdateResponse], service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.connectivity.directory.services.with_raw_response.update(
                service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                host={
                    "ipv4": "10.0.0.1",
                    "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
                },
                name="web-app",
                type="http",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_id` but received ''"):
            await async_client.connectivity.directory.services.with_raw_response.update(
                service_id="",
                account_id="account_id",
                host={
                    "ipv4": "10.0.0.1",
                    "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
                },
                name="web-app",
                type="http",
            )

    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        service = await async_client.connectivity.directory.services.update(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="postgres-db",
            type="tcp",
        )
        assert_matches_type(Optional[ServiceUpdateResponse], service, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        service = await async_client.connectivity.directory.services.update(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="postgres-db",
            type="tcp",
            app_protocol="postgresql",
            tcp_port=5432,
            tls_settings={"cert_verification_mode": "verify_full"},
        )
        assert_matches_type(Optional[ServiceUpdateResponse], service, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.connectivity.directory.services.with_raw_response.update(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="postgres-db",
            type="tcp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(Optional[ServiceUpdateResponse], service, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.connectivity.directory.services.with_streaming_response.update(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            host={
                "ipv4": "10.0.0.1",
                "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
            },
            name="postgres-db",
            type="tcp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(Optional[ServiceUpdateResponse], service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.connectivity.directory.services.with_raw_response.update(
                service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                host={
                    "ipv4": "10.0.0.1",
                    "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
                },
                name="postgres-db",
                type="tcp",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `service_id` but received ''"):
            await async_client.connectivity.directory.services.with_raw_response.update(
                service_id="",
                account_id="account_id",
                host={
                    "ipv4": "10.0.0.1",
                    "network": {"tunnel_id": "0191dce4-9ab4-7fce-b660-8e5dec5172da"},
                },
                name="postgres-db",
                type="tcp",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        service = await async_client.connectivity.directory.services.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[ServiceListResponse], service, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        service = await async_client.connectivity.directory.services.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=1,
            type="tcp",
        )
        assert_matches_type(AsyncV4PagePaginationArray[ServiceListResponse], service, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.connectivity.directory.services.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[ServiceListResponse], service, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.connectivity.directory.services.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[ServiceListResponse], service, path=["response"])

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
        assert_matches_type(Optional[ServiceGetResponse], service, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.connectivity.directory.services.with_raw_response.get(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(Optional[ServiceGetResponse], service, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.connectivity.directory.services.with_streaming_response.get(
            service_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(Optional[ServiceGetResponse], service, path=["response"])

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
