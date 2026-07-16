# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.zero_trust.casb.posture.findings import (
    InstanceGetResponse,
    InstanceListResponse,
    InstanceExportResponse,
    InstanceArchiveResponse,
    InstanceUnarchiveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInstances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        instance = client.zero_trust.casb.posture.findings.instances.list(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(SyncV4PagePaginationArray[InstanceListResponse], instance, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        instance = client.zero_trust.casb.posture.findings.instances.list(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            archived=True,
            asset_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            cursor="cursor",
            direction="asc",
            finding_instance_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            max_affliction_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_affliction_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            order="affliction_date",
            page=0,
            per_page=0,
            remediation_statuses=["none"],
            search="search",
        )
        assert_matches_type(SyncV4PagePaginationArray[InstanceListResponse], instance, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.findings.instances.with_raw_response.list(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[InstanceListResponse], instance, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.findings.instances.with_streaming_response.list(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[InstanceListResponse], instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.findings.instances.with_raw_response.list(
                finding_id="U3RhaW5sZXNzIHJvY2tz",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finding_id` but received ''"):
            client.zero_trust.casb.posture.findings.instances.with_raw_response.list(
                finding_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
            )

    @parametrize
    def test_method_archive(self, client: Cloudflare) -> None:
        instance = client.zero_trust.casb.posture.findings.instances.archive(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            check_instances=["497f6eca-6276-4993-bfeb-53cbbbba6f08"],
        )
        assert_matches_type(Optional[InstanceArchiveResponse], instance, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.findings.instances.with_raw_response.archive(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            check_instances=["497f6eca-6276-4993-bfeb-53cbbbba6f08"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(Optional[InstanceArchiveResponse], instance, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.findings.instances.with_streaming_response.archive(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            check_instances=["497f6eca-6276-4993-bfeb-53cbbbba6f08"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(Optional[InstanceArchiveResponse], instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_archive(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.findings.instances.with_raw_response.archive(
                finding_id="U3RhaW5sZXNzIHJvY2tz",
                account_id="",
                check_instances=["497f6eca-6276-4993-bfeb-53cbbbba6f08"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finding_id` but received ''"):
            client.zero_trust.casb.posture.findings.instances.with_raw_response.archive(
                finding_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
                check_instances=["497f6eca-6276-4993-bfeb-53cbbbba6f08"],
            )

    @parametrize
    def test_method_export(self, client: Cloudflare) -> None:
        instance = client.zero_trust.casb.posture.findings.instances.export(
            storage_namespace_id="00000000-0000-0000-0000-000000000001-00000000-0000-0000-0000-000000000002",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(Optional[InstanceExportResponse], instance, path=["response"])

    @parametrize
    def test_method_export_with_all_params(self, client: Cloudflare) -> None:
        instance = client.zero_trust.casb.posture.findings.instances.export(
            storage_namespace_id="00000000-0000-0000-0000-000000000001-00000000-0000-0000-0000-000000000002",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            archived=False,
            max_affliction_date=parse_datetime("2024-01-01T00:00:00Z"),
            min_affliction_date=parse_datetime("2023-01-01T00:00:00Z"),
            orders=[
                {
                    "direction": "asc",
                    "name": "asset.name",
                }
            ],
            search="sensitive data",
        )
        assert_matches_type(Optional[InstanceExportResponse], instance, path=["response"])

    @parametrize
    def test_raw_response_export(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.findings.instances.with_raw_response.export(
            storage_namespace_id="00000000-0000-0000-0000-000000000001-00000000-0000-0000-0000-000000000002",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(Optional[InstanceExportResponse], instance, path=["response"])

    @parametrize
    def test_streaming_response_export(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.findings.instances.with_streaming_response.export(
            storage_namespace_id="00000000-0000-0000-0000-000000000001-00000000-0000-0000-0000-000000000002",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(Optional[InstanceExportResponse], instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_export(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.findings.instances.with_raw_response.export(
                storage_namespace_id="00000000-0000-0000-0000-000000000001-00000000-0000-0000-0000-000000000002",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `storage_namespace_id` but received ''"):
            client.zero_trust.casb.posture.findings.instances.with_raw_response.export(
                storage_namespace_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        instance = client.zero_trust.casb.posture.findings.instances.get(
            instance_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            finding_id="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(Optional[InstanceGetResponse], instance, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.findings.instances.with_raw_response.get(
            instance_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            finding_id="U3RhaW5sZXNzIHJvY2tz",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(Optional[InstanceGetResponse], instance, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.findings.instances.with_streaming_response.get(
            instance_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            finding_id="U3RhaW5sZXNzIHJvY2tz",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(Optional[InstanceGetResponse], instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.findings.instances.with_raw_response.get(
                instance_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                finding_id="U3RhaW5sZXNzIHJvY2tz",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finding_id` but received ''"):
            client.zero_trust.casb.posture.findings.instances.with_raw_response.get(
                instance_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
                finding_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            client.zero_trust.casb.posture.findings.instances.with_raw_response.get(
                instance_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
                finding_id="U3RhaW5sZXNzIHJvY2tz",
            )

    @parametrize
    def test_method_unarchive(self, client: Cloudflare) -> None:
        instance = client.zero_trust.casb.posture.findings.instances.unarchive(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            check_instances=["497f6eca-6276-4993-bfeb-53cbbbba6f08"],
        )
        assert_matches_type(Optional[InstanceUnarchiveResponse], instance, path=["response"])

    @parametrize
    def test_raw_response_unarchive(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.findings.instances.with_raw_response.unarchive(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            check_instances=["497f6eca-6276-4993-bfeb-53cbbbba6f08"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = response.parse()
        assert_matches_type(Optional[InstanceUnarchiveResponse], instance, path=["response"])

    @parametrize
    def test_streaming_response_unarchive(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.findings.instances.with_streaming_response.unarchive(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            check_instances=["497f6eca-6276-4993-bfeb-53cbbbba6f08"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = response.parse()
            assert_matches_type(Optional[InstanceUnarchiveResponse], instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_unarchive(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.findings.instances.with_raw_response.unarchive(
                finding_id="U3RhaW5sZXNzIHJvY2tz",
                account_id="",
                check_instances=["497f6eca-6276-4993-bfeb-53cbbbba6f08"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finding_id` but received ''"):
            client.zero_trust.casb.posture.findings.instances.with_raw_response.unarchive(
                finding_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
                check_instances=["497f6eca-6276-4993-bfeb-53cbbbba6f08"],
            )


class TestAsyncInstances:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.zero_trust.casb.posture.findings.instances.list(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(AsyncV4PagePaginationArray[InstanceListResponse], instance, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.zero_trust.casb.posture.findings.instances.list(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            archived=True,
            asset_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            cursor="cursor",
            direction="asc",
            finding_instance_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            max_affliction_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_affliction_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            order="affliction_date",
            page=0,
            per_page=0,
            remediation_statuses=["none"],
            search="search",
        )
        assert_matches_type(AsyncV4PagePaginationArray[InstanceListResponse], instance, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.findings.instances.with_raw_response.list(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[InstanceListResponse], instance, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.findings.instances.with_streaming_response.list(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[InstanceListResponse], instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.findings.instances.with_raw_response.list(
                finding_id="U3RhaW5sZXNzIHJvY2tz",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finding_id` but received ''"):
            await async_client.zero_trust.casb.posture.findings.instances.with_raw_response.list(
                finding_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
            )

    @parametrize
    async def test_method_archive(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.zero_trust.casb.posture.findings.instances.archive(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            check_instances=["497f6eca-6276-4993-bfeb-53cbbbba6f08"],
        )
        assert_matches_type(Optional[InstanceArchiveResponse], instance, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.findings.instances.with_raw_response.archive(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            check_instances=["497f6eca-6276-4993-bfeb-53cbbbba6f08"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(Optional[InstanceArchiveResponse], instance, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.findings.instances.with_streaming_response.archive(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            check_instances=["497f6eca-6276-4993-bfeb-53cbbbba6f08"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(Optional[InstanceArchiveResponse], instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_archive(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.findings.instances.with_raw_response.archive(
                finding_id="U3RhaW5sZXNzIHJvY2tz",
                account_id="",
                check_instances=["497f6eca-6276-4993-bfeb-53cbbbba6f08"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finding_id` but received ''"):
            await async_client.zero_trust.casb.posture.findings.instances.with_raw_response.archive(
                finding_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
                check_instances=["497f6eca-6276-4993-bfeb-53cbbbba6f08"],
            )

    @parametrize
    async def test_method_export(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.zero_trust.casb.posture.findings.instances.export(
            storage_namespace_id="00000000-0000-0000-0000-000000000001-00000000-0000-0000-0000-000000000002",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(Optional[InstanceExportResponse], instance, path=["response"])

    @parametrize
    async def test_method_export_with_all_params(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.zero_trust.casb.posture.findings.instances.export(
            storage_namespace_id="00000000-0000-0000-0000-000000000001-00000000-0000-0000-0000-000000000002",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            archived=False,
            max_affliction_date=parse_datetime("2024-01-01T00:00:00Z"),
            min_affliction_date=parse_datetime("2023-01-01T00:00:00Z"),
            orders=[
                {
                    "direction": "asc",
                    "name": "asset.name",
                }
            ],
            search="sensitive data",
        )
        assert_matches_type(Optional[InstanceExportResponse], instance, path=["response"])

    @parametrize
    async def test_raw_response_export(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.findings.instances.with_raw_response.export(
            storage_namespace_id="00000000-0000-0000-0000-000000000001-00000000-0000-0000-0000-000000000002",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(Optional[InstanceExportResponse], instance, path=["response"])

    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.findings.instances.with_streaming_response.export(
            storage_namespace_id="00000000-0000-0000-0000-000000000001-00000000-0000-0000-0000-000000000002",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(Optional[InstanceExportResponse], instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_export(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.findings.instances.with_raw_response.export(
                storage_namespace_id="00000000-0000-0000-0000-000000000001-00000000-0000-0000-0000-000000000002",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `storage_namespace_id` but received ''"):
            await async_client.zero_trust.casb.posture.findings.instances.with_raw_response.export(
                storage_namespace_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.zero_trust.casb.posture.findings.instances.get(
            instance_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            finding_id="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(Optional[InstanceGetResponse], instance, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.findings.instances.with_raw_response.get(
            instance_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            finding_id="U3RhaW5sZXNzIHJvY2tz",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(Optional[InstanceGetResponse], instance, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.findings.instances.with_streaming_response.get(
            instance_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            finding_id="U3RhaW5sZXNzIHJvY2tz",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(Optional[InstanceGetResponse], instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.findings.instances.with_raw_response.get(
                instance_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                finding_id="U3RhaW5sZXNzIHJvY2tz",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finding_id` but received ''"):
            await async_client.zero_trust.casb.posture.findings.instances.with_raw_response.get(
                instance_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
                finding_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `instance_id` but received ''"):
            await async_client.zero_trust.casb.posture.findings.instances.with_raw_response.get(
                instance_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
                finding_id="U3RhaW5sZXNzIHJvY2tz",
            )

    @parametrize
    async def test_method_unarchive(self, async_client: AsyncCloudflare) -> None:
        instance = await async_client.zero_trust.casb.posture.findings.instances.unarchive(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            check_instances=["497f6eca-6276-4993-bfeb-53cbbbba6f08"],
        )
        assert_matches_type(Optional[InstanceUnarchiveResponse], instance, path=["response"])

    @parametrize
    async def test_raw_response_unarchive(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.findings.instances.with_raw_response.unarchive(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            check_instances=["497f6eca-6276-4993-bfeb-53cbbbba6f08"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        instance = await response.parse()
        assert_matches_type(Optional[InstanceUnarchiveResponse], instance, path=["response"])

    @parametrize
    async def test_streaming_response_unarchive(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.findings.instances.with_streaming_response.unarchive(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            check_instances=["497f6eca-6276-4993-bfeb-53cbbbba6f08"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            instance = await response.parse()
            assert_matches_type(Optional[InstanceUnarchiveResponse], instance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_unarchive(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.findings.instances.with_raw_response.unarchive(
                finding_id="U3RhaW5sZXNzIHJvY2tz",
                account_id="",
                check_instances=["497f6eca-6276-4993-bfeb-53cbbbba6f08"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finding_id` but received ''"):
            await async_client.zero_trust.casb.posture.findings.instances.with_raw_response.unarchive(
                finding_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
                check_instances=["497f6eca-6276-4993-bfeb-53cbbbba6f08"],
            )
