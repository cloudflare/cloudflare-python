# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.zero_trust.access.infrastructure import (
    TargetGetResponse,
    TargetListResponse,
    TargetCreateResponse,
    TargetUpdateResponse,
    TargetBulkUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTargets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        target = client.zero_trust.access.infrastructure.targets.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostname="infra-access-target",
            ip={},
        )
        assert_matches_type(Optional[TargetCreateResponse], target, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        target = client.zero_trust.access.infrastructure.targets.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostname="infra-access-target",
            ip={
                "ipv4": {
                    "ip_addr": "187.26.29.249",
                    "virtual_network_id": "c77b744e-acc8-428f-9257-6878c046ed55",
                },
                "ipv6": {
                    "ip_addr": "64c0:64e8:f0b4:8dbf:7104:72b0:ec8f:f5e0",
                    "virtual_network_id": "c77b744e-acc8-428f-9257-6878c046ed55",
                },
            },
        )
        assert_matches_type(Optional[TargetCreateResponse], target, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.infrastructure.targets.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostname="infra-access-target",
            ip={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = response.parse()
        assert_matches_type(Optional[TargetCreateResponse], target, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.access.infrastructure.targets.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostname="infra-access-target",
            ip={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = response.parse()
            assert_matches_type(Optional[TargetCreateResponse], target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.infrastructure.targets.with_raw_response.create(
                account_id="",
                hostname="infra-access-target",
                ip={},
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        target = client.zero_trust.access.infrastructure.targets.update(
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostname="infra-access-target",
            ip={},
        )
        assert_matches_type(Optional[TargetUpdateResponse], target, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        target = client.zero_trust.access.infrastructure.targets.update(
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostname="infra-access-target",
            ip={
                "ipv4": {
                    "ip_addr": "187.26.29.249",
                    "virtual_network_id": "c77b744e-acc8-428f-9257-6878c046ed55",
                },
                "ipv6": {
                    "ip_addr": "64c0:64e8:f0b4:8dbf:7104:72b0:ec8f:f5e0",
                    "virtual_network_id": "c77b744e-acc8-428f-9257-6878c046ed55",
                },
            },
        )
        assert_matches_type(Optional[TargetUpdateResponse], target, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.infrastructure.targets.with_raw_response.update(
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostname="infra-access-target",
            ip={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = response.parse()
        assert_matches_type(Optional[TargetUpdateResponse], target, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.access.infrastructure.targets.with_streaming_response.update(
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostname="infra-access-target",
            ip={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = response.parse()
            assert_matches_type(Optional[TargetUpdateResponse], target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.infrastructure.targets.with_raw_response.update(
                target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                hostname="infra-access-target",
                ip={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `target_id` but received ''"):
            client.zero_trust.access.infrastructure.targets.with_raw_response.update(
                target_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                hostname="infra-access-target",
                ip={},
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        target = client.zero_trust.access.infrastructure.targets.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[TargetListResponse], target, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        target = client.zero_trust.access.infrastructure.targets.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            direction="asc",
            hostname="hostname",
            hostname_contains="hostname_contains",
            ip_like="ip_like",
            ip_v4="ip_v4",
            ip_v6="ip_v6",
            ips=["string"],
            ipv4_end="ipv4_end",
            ipv4_start="ipv4_start",
            ipv6_end="ipv6_end",
            ipv6_start="ipv6_start",
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            order="hostname",
            page=1,
            per_page=1,
            target_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            virtual_network_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncV4PagePaginationArray[TargetListResponse], target, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.infrastructure.targets.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[TargetListResponse], target, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.access.infrastructure.targets.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[TargetListResponse], target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.infrastructure.targets.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        target = client.zero_trust.access.infrastructure.targets.delete(
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert target is None

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.infrastructure.targets.with_raw_response.delete(
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = response.parse()
        assert target is None

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.access.infrastructure.targets.with_streaming_response.delete(
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = response.parse()
            assert target is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.infrastructure.targets.with_raw_response.delete(
                target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `target_id` but received ''"):
            client.zero_trust.access.infrastructure.targets.with_raw_response.delete(
                target_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_bulk_delete(self, client: Cloudflare) -> None:
        target = client.zero_trust.access.infrastructure.targets.bulk_delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert target is None

    @parametrize
    def test_raw_response_bulk_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.infrastructure.targets.with_raw_response.bulk_delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = response.parse()
        assert target is None

    @parametrize
    def test_streaming_response_bulk_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.access.infrastructure.targets.with_streaming_response.bulk_delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = response.parse()
            assert target is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.infrastructure.targets.with_raw_response.bulk_delete(
                account_id="",
            )

    @parametrize
    def test_method_bulk_update(self, client: Cloudflare) -> None:
        target = client.zero_trust.access.infrastructure.targets.bulk_update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "hostname": "infra-access-target",
                    "ip": {},
                }
            ],
        )
        assert_matches_type(TargetBulkUpdateResponse, target, path=["response"])

    @parametrize
    def test_raw_response_bulk_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.infrastructure.targets.with_raw_response.bulk_update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "hostname": "infra-access-target",
                    "ip": {},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = response.parse()
        assert_matches_type(TargetBulkUpdateResponse, target, path=["response"])

    @parametrize
    def test_streaming_response_bulk_update(self, client: Cloudflare) -> None:
        with client.zero_trust.access.infrastructure.targets.with_streaming_response.bulk_update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "hostname": "infra-access-target",
                    "ip": {},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = response.parse()
            assert_matches_type(TargetBulkUpdateResponse, target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_bulk_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.infrastructure.targets.with_raw_response.bulk_update(
                account_id="",
                body=[
                    {
                        "hostname": "infra-access-target",
                        "ip": {},
                    }
                ],
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        target = client.zero_trust.access.infrastructure.targets.get(
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[TargetGetResponse], target, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.infrastructure.targets.with_raw_response.get(
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = response.parse()
        assert_matches_type(Optional[TargetGetResponse], target, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.access.infrastructure.targets.with_streaming_response.get(
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = response.parse()
            assert_matches_type(Optional[TargetGetResponse], target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.infrastructure.targets.with_raw_response.get(
                target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `target_id` but received ''"):
            client.zero_trust.access.infrastructure.targets.with_raw_response.get(
                target_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncTargets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        target = await async_client.zero_trust.access.infrastructure.targets.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostname="infra-access-target",
            ip={},
        )
        assert_matches_type(Optional[TargetCreateResponse], target, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        target = await async_client.zero_trust.access.infrastructure.targets.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostname="infra-access-target",
            ip={
                "ipv4": {
                    "ip_addr": "187.26.29.249",
                    "virtual_network_id": "c77b744e-acc8-428f-9257-6878c046ed55",
                },
                "ipv6": {
                    "ip_addr": "64c0:64e8:f0b4:8dbf:7104:72b0:ec8f:f5e0",
                    "virtual_network_id": "c77b744e-acc8-428f-9257-6878c046ed55",
                },
            },
        )
        assert_matches_type(Optional[TargetCreateResponse], target, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.infrastructure.targets.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostname="infra-access-target",
            ip={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = await response.parse()
        assert_matches_type(Optional[TargetCreateResponse], target, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.infrastructure.targets.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostname="infra-access-target",
            ip={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = await response.parse()
            assert_matches_type(Optional[TargetCreateResponse], target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.infrastructure.targets.with_raw_response.create(
                account_id="",
                hostname="infra-access-target",
                ip={},
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        target = await async_client.zero_trust.access.infrastructure.targets.update(
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostname="infra-access-target",
            ip={},
        )
        assert_matches_type(Optional[TargetUpdateResponse], target, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        target = await async_client.zero_trust.access.infrastructure.targets.update(
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostname="infra-access-target",
            ip={
                "ipv4": {
                    "ip_addr": "187.26.29.249",
                    "virtual_network_id": "c77b744e-acc8-428f-9257-6878c046ed55",
                },
                "ipv6": {
                    "ip_addr": "64c0:64e8:f0b4:8dbf:7104:72b0:ec8f:f5e0",
                    "virtual_network_id": "c77b744e-acc8-428f-9257-6878c046ed55",
                },
            },
        )
        assert_matches_type(Optional[TargetUpdateResponse], target, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.infrastructure.targets.with_raw_response.update(
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostname="infra-access-target",
            ip={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = await response.parse()
        assert_matches_type(Optional[TargetUpdateResponse], target, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.infrastructure.targets.with_streaming_response.update(
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            hostname="infra-access-target",
            ip={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = await response.parse()
            assert_matches_type(Optional[TargetUpdateResponse], target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.infrastructure.targets.with_raw_response.update(
                target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                hostname="infra-access-target",
                ip={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `target_id` but received ''"):
            await async_client.zero_trust.access.infrastructure.targets.with_raw_response.update(
                target_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                hostname="infra-access-target",
                ip={},
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        target = await async_client.zero_trust.access.infrastructure.targets.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[TargetListResponse], target, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        target = await async_client.zero_trust.access.infrastructure.targets.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            created_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            direction="asc",
            hostname="hostname",
            hostname_contains="hostname_contains",
            ip_like="ip_like",
            ip_v4="ip_v4",
            ip_v6="ip_v6",
            ips=["string"],
            ipv4_end="ipv4_end",
            ipv4_start="ipv4_start",
            ipv6_end="ipv6_end",
            ipv6_start="ipv6_start",
            modified_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            modified_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            order="hostname",
            page=1,
            per_page=1,
            target_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            virtual_network_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncV4PagePaginationArray[TargetListResponse], target, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.infrastructure.targets.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[TargetListResponse], target, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.infrastructure.targets.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[TargetListResponse], target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.infrastructure.targets.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        target = await async_client.zero_trust.access.infrastructure.targets.delete(
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert target is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.infrastructure.targets.with_raw_response.delete(
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = await response.parse()
        assert target is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.infrastructure.targets.with_streaming_response.delete(
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = await response.parse()
            assert target is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.infrastructure.targets.with_raw_response.delete(
                target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `target_id` but received ''"):
            await async_client.zero_trust.access.infrastructure.targets.with_raw_response.delete(
                target_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        target = await async_client.zero_trust.access.infrastructure.targets.bulk_delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert target is None

    @parametrize
    async def test_raw_response_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.infrastructure.targets.with_raw_response.bulk_delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = await response.parse()
        assert target is None

    @parametrize
    async def test_streaming_response_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.infrastructure.targets.with_streaming_response.bulk_delete(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = await response.parse()
            assert target is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.infrastructure.targets.with_raw_response.bulk_delete(
                account_id="",
            )

    @parametrize
    async def test_method_bulk_update(self, async_client: AsyncCloudflare) -> None:
        target = await async_client.zero_trust.access.infrastructure.targets.bulk_update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "hostname": "infra-access-target",
                    "ip": {},
                }
            ],
        )
        assert_matches_type(TargetBulkUpdateResponse, target, path=["response"])

    @parametrize
    async def test_raw_response_bulk_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.infrastructure.targets.with_raw_response.bulk_update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "hostname": "infra-access-target",
                    "ip": {},
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = await response.parse()
        assert_matches_type(TargetBulkUpdateResponse, target, path=["response"])

    @parametrize
    async def test_streaming_response_bulk_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.infrastructure.targets.with_streaming_response.bulk_update(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "hostname": "infra-access-target",
                    "ip": {},
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = await response.parse()
            assert_matches_type(TargetBulkUpdateResponse, target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_bulk_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.infrastructure.targets.with_raw_response.bulk_update(
                account_id="",
                body=[
                    {
                        "hostname": "infra-access-target",
                        "ip": {},
                    }
                ],
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        target = await async_client.zero_trust.access.infrastructure.targets.get(
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[TargetGetResponse], target, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.infrastructure.targets.with_raw_response.get(
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        target = await response.parse()
        assert_matches_type(Optional[TargetGetResponse], target, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.infrastructure.targets.with_streaming_response.get(
            target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            target = await response.parse()
            assert_matches_type(Optional[TargetGetResponse], target, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.infrastructure.targets.with_raw_response.get(
                target_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `target_id` but received ''"):
            await async_client.zero_trust.access.infrastructure.targets.with_raw_response.get(
                target_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
