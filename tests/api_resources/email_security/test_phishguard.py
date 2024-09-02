# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.types.email_security import PhishguardListResponse

from cloudflare.pagination import SyncSinglePage, AsyncSinglePage

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.email_security import phishguard_list_params
from cloudflare._utils import parse_date
from cloudflare._utils import parse_date
from cloudflare._utils import parse_date
from cloudflare._utils import parse_date
from cloudflare._utils import parse_date
from cloudflare._utils import parse_date
from cloudflare._utils import parse_date
from cloudflare._utils import parse_date
from cloudflare._utils import parse_date
from cloudflare._utils import parse_date
from cloudflare._utils import parse_date
from cloudflare._utils import parse_date
from cloudflare._utils import parse_date
from cloudflare._utils import parse_date
from cloudflare._utils import parse_date
from cloudflare._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhishguard:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        phishguard = client.email_security.phishguard.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            from_date=parse_date("2019-12-27"),
            to_date=parse_date("2019-12-27"),
        )
        assert_matches_type(SyncSinglePage[PhishguardListResponse], phishguard, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.email_security.phishguard.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            from_date=parse_date("2019-12-27"),
            to_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phishguard = response.parse()
        assert_matches_type(SyncSinglePage[PhishguardListResponse], phishguard, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.email_security.phishguard.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            from_date=parse_date("2019-12-27"),
            to_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phishguard = response.parse()
            assert_matches_type(SyncSinglePage[PhishguardListResponse], phishguard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.phishguard.with_raw_response.list(
                account_id="",
                from_date=parse_date("2019-12-27"),
                to_date=parse_date("2019-12-27"),
            )


class TestAsyncPhishguard:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        phishguard = await async_client.email_security.phishguard.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            from_date=parse_date("2019-12-27"),
            to_date=parse_date("2019-12-27"),
        )
        assert_matches_type(AsyncSinglePage[PhishguardListResponse], phishguard, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.phishguard.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            from_date=parse_date("2019-12-27"),
            to_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phishguard = await response.parse()
        assert_matches_type(AsyncSinglePage[PhishguardListResponse], phishguard, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.phishguard.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            from_date=parse_date("2019-12-27"),
            to_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phishguard = await response.parse()
            assert_matches_type(AsyncSinglePage[PhishguardListResponse], phishguard, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.phishguard.with_raw_response.list(
                account_id="",
                from_date=parse_date("2019-12-27"),
                to_date=parse_date("2019-12-27"),
            )
