# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.pagination import SyncV4PagePagination, AsyncV4PagePagination
from cloudflare.types.zero_trust.dex import (
    CommandListResponse,
    CommandCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCommands:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        command = client.zero_trust.dex.commands.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            commands=[
                {
                    "command_type": "pcap",
                    "device_id": "device_id",
                    "user_email": "user_email",
                }
            ],
        )
        assert_matches_type(Optional[CommandCreateResponse], command, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.dex.commands.with_raw_response.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            commands=[
                {
                    "command_type": "pcap",
                    "device_id": "device_id",
                    "user_email": "user_email",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = response.parse()
        assert_matches_type(Optional[CommandCreateResponse], command, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.dex.commands.with_streaming_response.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            commands=[
                {
                    "command_type": "pcap",
                    "device_id": "device_id",
                    "user_email": "user_email",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = response.parse()
            assert_matches_type(Optional[CommandCreateResponse], command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dex.commands.with_raw_response.create(
                account_id="",
                commands=[
                    {
                        "command_type": "pcap",
                        "device_id": "device_id",
                        "user_email": "user_email",
                    }
                ],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        command = client.zero_trust.dex.commands.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            page=1,
            per_page=50,
        )
        assert_matches_type(SyncV4PagePagination[Optional[CommandListResponse]], command, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        command = client.zero_trust.dex.commands.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            page=1,
            per_page=50,
            command_type="command_type",
            device_id="device_id",
            from_=parse_datetime("2023-08-20T20:45:00Z"),
            status="PENDING_EXEC",
            to=parse_datetime("2023-08-24T20:45:00Z"),
            user_email="user_email",
        )
        assert_matches_type(SyncV4PagePagination[Optional[CommandListResponse]], command, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.dex.commands.with_raw_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            page=1,
            per_page=50,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = response.parse()
        assert_matches_type(SyncV4PagePagination[Optional[CommandListResponse]], command, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.dex.commands.with_streaming_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            page=1,
            per_page=50,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = response.parse()
            assert_matches_type(SyncV4PagePagination[Optional[CommandListResponse]], command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dex.commands.with_raw_response.list(
                account_id="",
                page=1,
                per_page=50,
            )


class TestAsyncCommands:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        command = await async_client.zero_trust.dex.commands.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            commands=[
                {
                    "command_type": "pcap",
                    "device_id": "device_id",
                    "user_email": "user_email",
                }
            ],
        )
        assert_matches_type(Optional[CommandCreateResponse], command, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dex.commands.with_raw_response.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            commands=[
                {
                    "command_type": "pcap",
                    "device_id": "device_id",
                    "user_email": "user_email",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = await response.parse()
        assert_matches_type(Optional[CommandCreateResponse], command, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dex.commands.with_streaming_response.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            commands=[
                {
                    "command_type": "pcap",
                    "device_id": "device_id",
                    "user_email": "user_email",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = await response.parse()
            assert_matches_type(Optional[CommandCreateResponse], command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dex.commands.with_raw_response.create(
                account_id="",
                commands=[
                    {
                        "command_type": "pcap",
                        "device_id": "device_id",
                        "user_email": "user_email",
                    }
                ],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        command = await async_client.zero_trust.dex.commands.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            page=1,
            per_page=50,
        )
        assert_matches_type(AsyncV4PagePagination[Optional[CommandListResponse]], command, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        command = await async_client.zero_trust.dex.commands.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            page=1,
            per_page=50,
            command_type="command_type",
            device_id="device_id",
            from_=parse_datetime("2023-08-20T20:45:00Z"),
            status="PENDING_EXEC",
            to=parse_datetime("2023-08-24T20:45:00Z"),
            user_email="user_email",
        )
        assert_matches_type(AsyncV4PagePagination[Optional[CommandListResponse]], command, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dex.commands.with_raw_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            page=1,
            per_page=50,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = await response.parse()
        assert_matches_type(AsyncV4PagePagination[Optional[CommandListResponse]], command, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dex.commands.with_streaming_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
            page=1,
            per_page=50,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = await response.parse()
            assert_matches_type(AsyncV4PagePagination[Optional[CommandListResponse]], command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dex.commands.with_raw_response.list(
                account_id="",
                page=1,
                per_page=50,
            )
