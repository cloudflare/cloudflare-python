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
    FindingTypeGetResponse,
    FindingTypeListResponse,
    FindingTypeCreateResponse,
    FindingTypeUpdateResponse,
    FindingTypeValidateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFindingTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        finding_type = client.zero_trust.casb.posture.finding_types.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            applies_to_all_integrations=True,
            asset_class="GoogleWorkspaceFile",
            asset_vendor="GOOGLE_WORKSPACE",
            description="Detects files shared with too many users",
            expression='default result := "pass"\n\nresult := "fail" if input.asset.publicLinkDisabled == false\n',
            name="Excessive File Sharing",
            severity="High",
        )
        assert_matches_type(Optional[FindingTypeCreateResponse], finding_type, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        finding_type = client.zero_trust.casb.posture.finding_types.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            applies_to_all_integrations=True,
            asset_class="GoogleWorkspaceFile",
            asset_vendor="GOOGLE_WORKSPACE",
            description="Detects files shared with too many users",
            expression='default result := "pass"\n\nresult := "fail" if input.asset.publicLinkDisabled == false\n',
            name="Excessive File Sharing",
            severity="High",
            integration_ids=["550e8400-e29b-41d4-a716-446655440000"],
        )
        assert_matches_type(Optional[FindingTypeCreateResponse], finding_type, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.finding_types.with_raw_response.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            applies_to_all_integrations=True,
            asset_class="GoogleWorkspaceFile",
            asset_vendor="GOOGLE_WORKSPACE",
            description="Detects files shared with too many users",
            expression='default result := "pass"\n\nresult := "fail" if input.asset.publicLinkDisabled == false\n',
            name="Excessive File Sharing",
            severity="High",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding_type = response.parse()
        assert_matches_type(Optional[FindingTypeCreateResponse], finding_type, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.finding_types.with_streaming_response.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            applies_to_all_integrations=True,
            asset_class="GoogleWorkspaceFile",
            asset_vendor="GOOGLE_WORKSPACE",
            description="Detects files shared with too many users",
            expression='default result := "pass"\n\nresult := "fail" if input.asset.publicLinkDisabled == false\n',
            name="Excessive File Sharing",
            severity="High",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding_type = response.parse()
            assert_matches_type(Optional[FindingTypeCreateResponse], finding_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.finding_types.with_raw_response.create(
                account_id="",
                applies_to_all_integrations=True,
                asset_class="GoogleWorkspaceFile",
                asset_vendor="GOOGLE_WORKSPACE",
                description="Detects files shared with too many users",
                expression='default result := "pass"\n\nresult := "fail" if input.asset.publicLinkDisabled == false\n',
                name="Excessive File Sharing",
                severity="High",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        finding_type = client.zero_trust.casb.posture.finding_types.update(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            applies_to_all_integrations=True,
        )
        assert_matches_type(Optional[FindingTypeUpdateResponse], finding_type, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        finding_type = client.zero_trust.casb.posture.finding_types.update(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            applies_to_all_integrations=True,
            description="Detects files shared with too many users",
            integration_ids=["550e8400-e29b-41d4-a716-446655440000"],
            name="Excessive File Sharing",
            severity="High",
        )
        assert_matches_type(Optional[FindingTypeUpdateResponse], finding_type, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.finding_types.with_raw_response.update(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            applies_to_all_integrations=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding_type = response.parse()
        assert_matches_type(Optional[FindingTypeUpdateResponse], finding_type, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.finding_types.with_streaming_response.update(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            applies_to_all_integrations=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding_type = response.parse()
            assert_matches_type(Optional[FindingTypeUpdateResponse], finding_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.finding_types.with_raw_response.update(
                finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                applies_to_all_integrations=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finding_type_id` but received ''"):
            client.zero_trust.casb.posture.finding_types.with_raw_response.update(
                finding_type_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
                applies_to_all_integrations=True,
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        finding_type = client.zero_trust.casb.posture.finding_types.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(SyncV4PagePaginationArray[FindingTypeListResponse], finding_type, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        finding_type = client.zero_trust.casb.posture.finding_types.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            direction="asc",
            max_updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            order="created",
            origins=["system"],
            page=0,
            per_page=0,
            quarantined=True,
            search="search",
            severities=["high"],
            types=["Content"],
            vendors=["GOOGLE_WORKSPACE"],
        )
        assert_matches_type(SyncV4PagePaginationArray[FindingTypeListResponse], finding_type, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.finding_types.with_raw_response.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding_type = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[FindingTypeListResponse], finding_type, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.finding_types.with_streaming_response.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding_type = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[FindingTypeListResponse], finding_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.finding_types.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        finding_type = client.zero_trust.casb.posture.finding_types.delete(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert finding_type is None

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.finding_types.with_raw_response.delete(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding_type = response.parse()
        assert finding_type is None

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.finding_types.with_streaming_response.delete(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding_type = response.parse()
            assert finding_type is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.finding_types.with_raw_response.delete(
                finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finding_type_id` but received ''"):
            client.zero_trust.casb.posture.finding_types.with_raw_response.delete(
                finding_type_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        finding_type = client.zero_trust.casb.posture.finding_types.get(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(Optional[FindingTypeGetResponse], finding_type, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.finding_types.with_raw_response.get(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding_type = response.parse()
        assert_matches_type(Optional[FindingTypeGetResponse], finding_type, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.finding_types.with_streaming_response.get(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding_type = response.parse()
            assert_matches_type(Optional[FindingTypeGetResponse], finding_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.finding_types.with_raw_response.get(
                finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finding_type_id` but received ''"):
            client.zero_trust.casb.posture.finding_types.with_raw_response.get(
                finding_type_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
            )

    @parametrize
    def test_method_validate(self, client: Cloudflare) -> None:
        finding_type = client.zero_trust.casb.posture.finding_types.validate(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            applies_to_all_integrations=True,
            asset_class="GoogleWorkspaceFile",
            asset_vendor="GOOGLE_WORKSPACE",
            description="Detects files shared with too many users",
            expression='default result := "pass"\n\nresult := "fail" if input.asset.publicLinkDisabled == false\n',
            name="Excessive File Sharing",
            severity="High",
        )
        assert_matches_type(Optional[FindingTypeValidateResponse], finding_type, path=["response"])

    @parametrize
    def test_method_validate_with_all_params(self, client: Cloudflare) -> None:
        finding_type = client.zero_trust.casb.posture.finding_types.validate(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            applies_to_all_integrations=True,
            asset_class="GoogleWorkspaceFile",
            asset_vendor="GOOGLE_WORKSPACE",
            description="Detects files shared with too many users",
            expression='default result := "pass"\n\nresult := "fail" if input.asset.publicLinkDisabled == false\n',
            name="Excessive File Sharing",
            severity="High",
            integration_ids=["550e8400-e29b-41d4-a716-446655440000"],
        )
        assert_matches_type(Optional[FindingTypeValidateResponse], finding_type, path=["response"])

    @parametrize
    def test_raw_response_validate(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.finding_types.with_raw_response.validate(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            applies_to_all_integrations=True,
            asset_class="GoogleWorkspaceFile",
            asset_vendor="GOOGLE_WORKSPACE",
            description="Detects files shared with too many users",
            expression='default result := "pass"\n\nresult := "fail" if input.asset.publicLinkDisabled == false\n',
            name="Excessive File Sharing",
            severity="High",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding_type = response.parse()
        assert_matches_type(Optional[FindingTypeValidateResponse], finding_type, path=["response"])

    @parametrize
    def test_streaming_response_validate(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.finding_types.with_streaming_response.validate(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            applies_to_all_integrations=True,
            asset_class="GoogleWorkspaceFile",
            asset_vendor="GOOGLE_WORKSPACE",
            description="Detects files shared with too many users",
            expression='default result := "pass"\n\nresult := "fail" if input.asset.publicLinkDisabled == false\n',
            name="Excessive File Sharing",
            severity="High",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding_type = response.parse()
            assert_matches_type(Optional[FindingTypeValidateResponse], finding_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_validate(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.finding_types.with_raw_response.validate(
                account_id="",
                applies_to_all_integrations=True,
                asset_class="GoogleWorkspaceFile",
                asset_vendor="GOOGLE_WORKSPACE",
                description="Detects files shared with too many users",
                expression='default result := "pass"\n\nresult := "fail" if input.asset.publicLinkDisabled == false\n',
                name="Excessive File Sharing",
                severity="High",
            )


class TestAsyncFindingTypes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        finding_type = await async_client.zero_trust.casb.posture.finding_types.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            applies_to_all_integrations=True,
            asset_class="GoogleWorkspaceFile",
            asset_vendor="GOOGLE_WORKSPACE",
            description="Detects files shared with too many users",
            expression='default result := "pass"\n\nresult := "fail" if input.asset.publicLinkDisabled == false\n',
            name="Excessive File Sharing",
            severity="High",
        )
        assert_matches_type(Optional[FindingTypeCreateResponse], finding_type, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        finding_type = await async_client.zero_trust.casb.posture.finding_types.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            applies_to_all_integrations=True,
            asset_class="GoogleWorkspaceFile",
            asset_vendor="GOOGLE_WORKSPACE",
            description="Detects files shared with too many users",
            expression='default result := "pass"\n\nresult := "fail" if input.asset.publicLinkDisabled == false\n',
            name="Excessive File Sharing",
            severity="High",
            integration_ids=["550e8400-e29b-41d4-a716-446655440000"],
        )
        assert_matches_type(Optional[FindingTypeCreateResponse], finding_type, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.finding_types.with_raw_response.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            applies_to_all_integrations=True,
            asset_class="GoogleWorkspaceFile",
            asset_vendor="GOOGLE_WORKSPACE",
            description="Detects files shared with too many users",
            expression='default result := "pass"\n\nresult := "fail" if input.asset.publicLinkDisabled == false\n',
            name="Excessive File Sharing",
            severity="High",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding_type = await response.parse()
        assert_matches_type(Optional[FindingTypeCreateResponse], finding_type, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.finding_types.with_streaming_response.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            applies_to_all_integrations=True,
            asset_class="GoogleWorkspaceFile",
            asset_vendor="GOOGLE_WORKSPACE",
            description="Detects files shared with too many users",
            expression='default result := "pass"\n\nresult := "fail" if input.asset.publicLinkDisabled == false\n',
            name="Excessive File Sharing",
            severity="High",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding_type = await response.parse()
            assert_matches_type(Optional[FindingTypeCreateResponse], finding_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.finding_types.with_raw_response.create(
                account_id="",
                applies_to_all_integrations=True,
                asset_class="GoogleWorkspaceFile",
                asset_vendor="GOOGLE_WORKSPACE",
                description="Detects files shared with too many users",
                expression='default result := "pass"\n\nresult := "fail" if input.asset.publicLinkDisabled == false\n',
                name="Excessive File Sharing",
                severity="High",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        finding_type = await async_client.zero_trust.casb.posture.finding_types.update(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            applies_to_all_integrations=True,
        )
        assert_matches_type(Optional[FindingTypeUpdateResponse], finding_type, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        finding_type = await async_client.zero_trust.casb.posture.finding_types.update(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            applies_to_all_integrations=True,
            description="Detects files shared with too many users",
            integration_ids=["550e8400-e29b-41d4-a716-446655440000"],
            name="Excessive File Sharing",
            severity="High",
        )
        assert_matches_type(Optional[FindingTypeUpdateResponse], finding_type, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.finding_types.with_raw_response.update(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            applies_to_all_integrations=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding_type = await response.parse()
        assert_matches_type(Optional[FindingTypeUpdateResponse], finding_type, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.finding_types.with_streaming_response.update(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            applies_to_all_integrations=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding_type = await response.parse()
            assert_matches_type(Optional[FindingTypeUpdateResponse], finding_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.finding_types.with_raw_response.update(
                finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                applies_to_all_integrations=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finding_type_id` but received ''"):
            await async_client.zero_trust.casb.posture.finding_types.with_raw_response.update(
                finding_type_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
                applies_to_all_integrations=True,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        finding_type = await async_client.zero_trust.casb.posture.finding_types.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(AsyncV4PagePaginationArray[FindingTypeListResponse], finding_type, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        finding_type = await async_client.zero_trust.casb.posture.finding_types.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            direction="asc",
            max_updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            order="created",
            origins=["system"],
            page=0,
            per_page=0,
            quarantined=True,
            search="search",
            severities=["high"],
            types=["Content"],
            vendors=["GOOGLE_WORKSPACE"],
        )
        assert_matches_type(AsyncV4PagePaginationArray[FindingTypeListResponse], finding_type, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.finding_types.with_raw_response.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding_type = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[FindingTypeListResponse], finding_type, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.finding_types.with_streaming_response.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding_type = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[FindingTypeListResponse], finding_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.finding_types.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        finding_type = await async_client.zero_trust.casb.posture.finding_types.delete(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert finding_type is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.finding_types.with_raw_response.delete(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding_type = await response.parse()
        assert finding_type is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.finding_types.with_streaming_response.delete(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding_type = await response.parse()
            assert finding_type is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.finding_types.with_raw_response.delete(
                finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finding_type_id` but received ''"):
            await async_client.zero_trust.casb.posture.finding_types.with_raw_response.delete(
                finding_type_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        finding_type = await async_client.zero_trust.casb.posture.finding_types.get(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(Optional[FindingTypeGetResponse], finding_type, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.finding_types.with_raw_response.get(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding_type = await response.parse()
        assert_matches_type(Optional[FindingTypeGetResponse], finding_type, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.finding_types.with_streaming_response.get(
            finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding_type = await response.parse()
            assert_matches_type(Optional[FindingTypeGetResponse], finding_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.finding_types.with_raw_response.get(
                finding_type_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `finding_type_id` but received ''"):
            await async_client.zero_trust.casb.posture.finding_types.with_raw_response.get(
                finding_type_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
            )

    @parametrize
    async def test_method_validate(self, async_client: AsyncCloudflare) -> None:
        finding_type = await async_client.zero_trust.casb.posture.finding_types.validate(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            applies_to_all_integrations=True,
            asset_class="GoogleWorkspaceFile",
            asset_vendor="GOOGLE_WORKSPACE",
            description="Detects files shared with too many users",
            expression='default result := "pass"\n\nresult := "fail" if input.asset.publicLinkDisabled == false\n',
            name="Excessive File Sharing",
            severity="High",
        )
        assert_matches_type(Optional[FindingTypeValidateResponse], finding_type, path=["response"])

    @parametrize
    async def test_method_validate_with_all_params(self, async_client: AsyncCloudflare) -> None:
        finding_type = await async_client.zero_trust.casb.posture.finding_types.validate(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            applies_to_all_integrations=True,
            asset_class="GoogleWorkspaceFile",
            asset_vendor="GOOGLE_WORKSPACE",
            description="Detects files shared with too many users",
            expression='default result := "pass"\n\nresult := "fail" if input.asset.publicLinkDisabled == false\n',
            name="Excessive File Sharing",
            severity="High",
            integration_ids=["550e8400-e29b-41d4-a716-446655440000"],
        )
        assert_matches_type(Optional[FindingTypeValidateResponse], finding_type, path=["response"])

    @parametrize
    async def test_raw_response_validate(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.finding_types.with_raw_response.validate(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            applies_to_all_integrations=True,
            asset_class="GoogleWorkspaceFile",
            asset_vendor="GOOGLE_WORKSPACE",
            description="Detects files shared with too many users",
            expression='default result := "pass"\n\nresult := "fail" if input.asset.publicLinkDisabled == false\n',
            name="Excessive File Sharing",
            severity="High",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        finding_type = await response.parse()
        assert_matches_type(Optional[FindingTypeValidateResponse], finding_type, path=["response"])

    @parametrize
    async def test_streaming_response_validate(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.finding_types.with_streaming_response.validate(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            applies_to_all_integrations=True,
            asset_class="GoogleWorkspaceFile",
            asset_vendor="GOOGLE_WORKSPACE",
            description="Detects files shared with too many users",
            expression='default result := "pass"\n\nresult := "fail" if input.asset.publicLinkDisabled == false\n',
            name="Excessive File Sharing",
            severity="High",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            finding_type = await response.parse()
            assert_matches_type(Optional[FindingTypeValidateResponse], finding_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_validate(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.finding_types.with_raw_response.validate(
                account_id="",
                applies_to_all_integrations=True,
                asset_class="GoogleWorkspaceFile",
                asset_vendor="GOOGLE_WORKSPACE",
                description="Detects files shared with too many users",
                expression='default result := "pass"\n\nresult := "fail" if input.asset.publicLinkDisabled == false\n',
                name="Excessive File Sharing",
                severity="High",
            )
