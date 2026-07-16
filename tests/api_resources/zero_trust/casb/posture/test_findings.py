# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.zero_trust.casb.posture import (
    FindingGetResponse,
    FindingListResponse,
    FindingExportResponse,
    FindingIgnoreResponse,
    FindingUnignoreResponse,
    FindingTuneSeverityResponse,
    FindingResetSeverityResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFindings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        finding = client.zero_trust.casb.posture.findings.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(SyncV4PagePaginationArray[FindingListResponse], finding, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        finding = client.zero_trust.casb.posture.findings.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            cursor="cursor",
            direction="asc",
            finding_type_ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ignored=True,
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            max_affliction_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_affliction_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            observation="Activity",
            order="finding.name",
            page=0,
            per_page=0,
            product="Cloud",
            search="search",
            severity="Critical",
            type="Content",
            vendor="GOOGLE_WORKSPACE",
        )
        assert_matches_type(SyncV4PagePaginationArray[FindingListResponse], finding, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.findings.with_raw_response.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[FindingListResponse], finding, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.findings.with_streaming_response.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[FindingListResponse], finding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.findings.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_export(self, client: Cloudflare) -> None:
        finding = client.zero_trust.casb.posture.findings.export(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(Optional[FindingExportResponse], finding, path=["response"])

    @parametrize
    def test_method_export_with_all_params(self, client: Cloudflare) -> None:
        finding = client.zero_trust.casb.posture.findings.export(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            ignored=True,
            integration_id=["55d7337e-1d0a-49fc-9826-925ba40df035"],
            max_affliction_date=parse_datetime("2019-08-24T14:15:22Z"),
            min_affliction_date=parse_datetime("2018-08-24T14:15:22Z"),
            orders=[
                {
                    "direction": "asc",
                    "name": "instance_count",
                }
            ],
            product="SaaS",
            search="public access",
            severities=["CRITICAL"],
            vendors=["AWS"],
        )
        assert_matches_type(Optional[FindingExportResponse], finding, path=["response"])

    @parametrize
    def test_raw_response_export(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.findings.with_raw_response.export(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding = response.parse()
        assert_matches_type(Optional[FindingExportResponse], finding, path=["response"])

    @parametrize
    def test_streaming_response_export(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.findings.with_streaming_response.export(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding = response.parse()
            assert_matches_type(Optional[FindingExportResponse], finding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_export(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.findings.with_raw_response.export(
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        finding = client.zero_trust.casb.posture.findings.get(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(Optional[FindingGetResponse], finding, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.findings.with_raw_response.get(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding = response.parse()
        assert_matches_type(Optional[FindingGetResponse], finding, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.findings.with_streaming_response.get(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding = response.parse()
            assert_matches_type(Optional[FindingGetResponse], finding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.findings.with_raw_response.get(
                finding_id="U3RhaW5sZXNzIHJvY2tz",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finding_id` but received ''"):
            client.zero_trust.casb.posture.findings.with_raw_response.get(
                finding_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
            )

    @parametrize
    def test_method_ignore(self, client: Cloudflare) -> None:
        finding = client.zero_trust.casb.posture.findings.ignore(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            checks=[
                "MDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAxOjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMgo="
            ],
        )
        assert_matches_type(Optional[FindingIgnoreResponse], finding, path=["response"])

    @parametrize
    def test_raw_response_ignore(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.findings.with_raw_response.ignore(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            checks=[
                "MDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAxOjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMgo="
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding = response.parse()
        assert_matches_type(Optional[FindingIgnoreResponse], finding, path=["response"])

    @parametrize
    def test_streaming_response_ignore(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.findings.with_streaming_response.ignore(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            checks=[
                "MDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAxOjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMgo="
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding = response.parse()
            assert_matches_type(Optional[FindingIgnoreResponse], finding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_ignore(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.findings.with_raw_response.ignore(
                account_id="",
                checks=[
                    "MDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAxOjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMgo="
                ],
            )

    @parametrize
    def test_method_reset_severity(self, client: Cloudflare) -> None:
        finding = client.zero_trust.casb.posture.findings.reset_severity(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(Optional[FindingResetSeverityResponse], finding, path=["response"])

    @parametrize
    def test_raw_response_reset_severity(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.findings.with_raw_response.reset_severity(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding = response.parse()
        assert_matches_type(Optional[FindingResetSeverityResponse], finding, path=["response"])

    @parametrize
    def test_streaming_response_reset_severity(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.findings.with_streaming_response.reset_severity(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding = response.parse()
            assert_matches_type(Optional[FindingResetSeverityResponse], finding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reset_severity(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.findings.with_raw_response.reset_severity(
                finding_id="U3RhaW5sZXNzIHJvY2tz",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finding_id` but received ''"):
            client.zero_trust.casb.posture.findings.with_raw_response.reset_severity(
                finding_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
            )

    @parametrize
    def test_method_tune_severity(self, client: Cloudflare) -> None:
        finding = client.zero_trust.casb.posture.findings.tune_severity(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            new_severity=1,
        )
        assert_matches_type(Optional[FindingTuneSeverityResponse], finding, path=["response"])

    @parametrize
    def test_raw_response_tune_severity(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.findings.with_raw_response.tune_severity(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            new_severity=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding = response.parse()
        assert_matches_type(Optional[FindingTuneSeverityResponse], finding, path=["response"])

    @parametrize
    def test_streaming_response_tune_severity(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.findings.with_streaming_response.tune_severity(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            new_severity=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding = response.parse()
            assert_matches_type(Optional[FindingTuneSeverityResponse], finding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_tune_severity(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.findings.with_raw_response.tune_severity(
                finding_id="U3RhaW5sZXNzIHJvY2tz",
                account_id="",
                new_severity=1,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finding_id` but received ''"):
            client.zero_trust.casb.posture.findings.with_raw_response.tune_severity(
                finding_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
                new_severity=1,
            )

    @parametrize
    def test_method_unignore(self, client: Cloudflare) -> None:
        finding = client.zero_trust.casb.posture.findings.unignore(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            checks=[
                "MDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAxOjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMgo="
            ],
        )
        assert_matches_type(Optional[FindingUnignoreResponse], finding, path=["response"])

    @parametrize
    def test_raw_response_unignore(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.findings.with_raw_response.unignore(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            checks=[
                "MDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAxOjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMgo="
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding = response.parse()
        assert_matches_type(Optional[FindingUnignoreResponse], finding, path=["response"])

    @parametrize
    def test_streaming_response_unignore(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.findings.with_streaming_response.unignore(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            checks=[
                "MDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAxOjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMgo="
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding = response.parse()
            assert_matches_type(Optional[FindingUnignoreResponse], finding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_unignore(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.findings.with_raw_response.unignore(
                account_id="",
                checks=[
                    "MDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAxOjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMgo="
                ],
            )


class TestAsyncFindings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        finding = await async_client.zero_trust.casb.posture.findings.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(AsyncV4PagePaginationArray[FindingListResponse], finding, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        finding = await async_client.zero_trust.casb.posture.findings.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            cursor="cursor",
            direction="asc",
            finding_type_ids="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ignored=True,
            integration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            max_affliction_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_affliction_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            observation="Activity",
            order="finding.name",
            page=0,
            per_page=0,
            product="Cloud",
            search="search",
            severity="Critical",
            type="Content",
            vendor="GOOGLE_WORKSPACE",
        )
        assert_matches_type(AsyncV4PagePaginationArray[FindingListResponse], finding, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.findings.with_raw_response.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[FindingListResponse], finding, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.findings.with_streaming_response.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[FindingListResponse], finding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.findings.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_export(self, async_client: AsyncCloudflare) -> None:
        finding = await async_client.zero_trust.casb.posture.findings.export(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(Optional[FindingExportResponse], finding, path=["response"])

    @parametrize
    async def test_method_export_with_all_params(self, async_client: AsyncCloudflare) -> None:
        finding = await async_client.zero_trust.casb.posture.findings.export(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            ignored=True,
            integration_id=["55d7337e-1d0a-49fc-9826-925ba40df035"],
            max_affliction_date=parse_datetime("2019-08-24T14:15:22Z"),
            min_affliction_date=parse_datetime("2018-08-24T14:15:22Z"),
            orders=[
                {
                    "direction": "asc",
                    "name": "instance_count",
                }
            ],
            product="SaaS",
            search="public access",
            severities=["CRITICAL"],
            vendors=["AWS"],
        )
        assert_matches_type(Optional[FindingExportResponse], finding, path=["response"])

    @parametrize
    async def test_raw_response_export(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.findings.with_raw_response.export(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding = await response.parse()
        assert_matches_type(Optional[FindingExportResponse], finding, path=["response"])

    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.findings.with_streaming_response.export(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding = await response.parse()
            assert_matches_type(Optional[FindingExportResponse], finding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_export(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.findings.with_raw_response.export(
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        finding = await async_client.zero_trust.casb.posture.findings.get(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(Optional[FindingGetResponse], finding, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.findings.with_raw_response.get(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding = await response.parse()
        assert_matches_type(Optional[FindingGetResponse], finding, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.findings.with_streaming_response.get(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding = await response.parse()
            assert_matches_type(Optional[FindingGetResponse], finding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.findings.with_raw_response.get(
                finding_id="U3RhaW5sZXNzIHJvY2tz",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finding_id` but received ''"):
            await async_client.zero_trust.casb.posture.findings.with_raw_response.get(
                finding_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
            )

    @parametrize
    async def test_method_ignore(self, async_client: AsyncCloudflare) -> None:
        finding = await async_client.zero_trust.casb.posture.findings.ignore(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            checks=[
                "MDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAxOjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMgo="
            ],
        )
        assert_matches_type(Optional[FindingIgnoreResponse], finding, path=["response"])

    @parametrize
    async def test_raw_response_ignore(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.findings.with_raw_response.ignore(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            checks=[
                "MDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAxOjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMgo="
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding = await response.parse()
        assert_matches_type(Optional[FindingIgnoreResponse], finding, path=["response"])

    @parametrize
    async def test_streaming_response_ignore(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.findings.with_streaming_response.ignore(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            checks=[
                "MDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAxOjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMgo="
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding = await response.parse()
            assert_matches_type(Optional[FindingIgnoreResponse], finding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_ignore(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.findings.with_raw_response.ignore(
                account_id="",
                checks=[
                    "MDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAxOjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMgo="
                ],
            )

    @parametrize
    async def test_method_reset_severity(self, async_client: AsyncCloudflare) -> None:
        finding = await async_client.zero_trust.casb.posture.findings.reset_severity(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(Optional[FindingResetSeverityResponse], finding, path=["response"])

    @parametrize
    async def test_raw_response_reset_severity(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.findings.with_raw_response.reset_severity(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding = await response.parse()
        assert_matches_type(Optional[FindingResetSeverityResponse], finding, path=["response"])

    @parametrize
    async def test_streaming_response_reset_severity(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.findings.with_streaming_response.reset_severity(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding = await response.parse()
            assert_matches_type(Optional[FindingResetSeverityResponse], finding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reset_severity(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.findings.with_raw_response.reset_severity(
                finding_id="U3RhaW5sZXNzIHJvY2tz",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finding_id` but received ''"):
            await async_client.zero_trust.casb.posture.findings.with_raw_response.reset_severity(
                finding_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
            )

    @parametrize
    async def test_method_tune_severity(self, async_client: AsyncCloudflare) -> None:
        finding = await async_client.zero_trust.casb.posture.findings.tune_severity(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            new_severity=1,
        )
        assert_matches_type(Optional[FindingTuneSeverityResponse], finding, path=["response"])

    @parametrize
    async def test_raw_response_tune_severity(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.findings.with_raw_response.tune_severity(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            new_severity=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding = await response.parse()
        assert_matches_type(Optional[FindingTuneSeverityResponse], finding, path=["response"])

    @parametrize
    async def test_streaming_response_tune_severity(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.findings.with_streaming_response.tune_severity(
            finding_id="U3RhaW5sZXNzIHJvY2tz",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            new_severity=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding = await response.parse()
            assert_matches_type(Optional[FindingTuneSeverityResponse], finding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_tune_severity(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.findings.with_raw_response.tune_severity(
                finding_id="U3RhaW5sZXNzIHJvY2tz",
                account_id="",
                new_severity=1,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finding_id` but received ''"):
            await async_client.zero_trust.casb.posture.findings.with_raw_response.tune_severity(
                finding_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
                new_severity=1,
            )

    @parametrize
    async def test_method_unignore(self, async_client: AsyncCloudflare) -> None:
        finding = await async_client.zero_trust.casb.posture.findings.unignore(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            checks=[
                "MDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAxOjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMgo="
            ],
        )
        assert_matches_type(Optional[FindingUnignoreResponse], finding, path=["response"])

    @parametrize
    async def test_raw_response_unignore(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.findings.with_raw_response.unignore(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            checks=[
                "MDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAxOjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMgo="
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding = await response.parse()
        assert_matches_type(Optional[FindingUnignoreResponse], finding, path=["response"])

    @parametrize
    async def test_streaming_response_unignore(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.findings.with_streaming_response.unignore(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            checks=[
                "MDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAxOjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMgo="
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding = await response.parse()
            assert_matches_type(Optional[FindingUnignoreResponse], finding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_unignore(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.findings.with_raw_response.unignore(
                account_id="",
                checks=[
                    "MDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDAwMDAwMDAxOjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMgo="
                ],
            )
