# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.gateway import (
    PacfileGetResponse,
    PacfileListResponse,
    PacfileCreateResponse,
    PacfileUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPacfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        pacfile = client.zero_trust.gateway.pacfiles.create(
            account_id="699d98642c564d2e855e9661899b7252",
            contents='function FindProxyForURL(url, host) { return "DIRECT"; }',
            name="Devops team",
        )
        assert_matches_type(Optional[PacfileCreateResponse], pacfile, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        pacfile = client.zero_trust.gateway.pacfiles.create(
            account_id="699d98642c564d2e855e9661899b7252",
            contents='function FindProxyForURL(url, host) { return "DIRECT"; }',
            name="Devops team",
            description="PAC file for Devops team",
            slug="pac_devops",
        )
        assert_matches_type(Optional[PacfileCreateResponse], pacfile, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.pacfiles.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            contents='function FindProxyForURL(url, host) { return "DIRECT"; }',
            name="Devops team",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pacfile = response.parse()
        assert_matches_type(Optional[PacfileCreateResponse], pacfile, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.pacfiles.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            contents='function FindProxyForURL(url, host) { return "DIRECT"; }',
            name="Devops team",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pacfile = response.parse()
            assert_matches_type(Optional[PacfileCreateResponse], pacfile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.pacfiles.with_raw_response.create(
                account_id="",
                contents='function FindProxyForURL(url, host) { return "DIRECT"; }',
                name="Devops team",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        pacfile = client.zero_trust.gateway.pacfiles.update(
            pacfile_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            contents='function FindProxyForURL(url, host) { return "DIRECT"; }',
            description="PAC file for Devops team",
            name="Devops team",
        )
        assert_matches_type(Optional[PacfileUpdateResponse], pacfile, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.pacfiles.with_raw_response.update(
            pacfile_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            contents='function FindProxyForURL(url, host) { return "DIRECT"; }',
            description="PAC file for Devops team",
            name="Devops team",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pacfile = response.parse()
        assert_matches_type(Optional[PacfileUpdateResponse], pacfile, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.pacfiles.with_streaming_response.update(
            pacfile_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            contents='function FindProxyForURL(url, host) { return "DIRECT"; }',
            description="PAC file for Devops team",
            name="Devops team",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pacfile = response.parse()
            assert_matches_type(Optional[PacfileUpdateResponse], pacfile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.pacfiles.with_raw_response.update(
                pacfile_id="ed35569b41ce4d1facfe683550f54086",
                account_id="",
                contents='function FindProxyForURL(url, host) { return "DIRECT"; }',
                description="PAC file for Devops team",
                name="Devops team",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pacfile_id` but received ''"):
            client.zero_trust.gateway.pacfiles.with_raw_response.update(
                pacfile_id="",
                account_id="699d98642c564d2e855e9661899b7252",
                contents='function FindProxyForURL(url, host) { return "DIRECT"; }',
                description="PAC file for Devops team",
                name="Devops team",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        pacfile = client.zero_trust.gateway.pacfiles.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(SyncSinglePage[PacfileListResponse], pacfile, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.pacfiles.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pacfile = response.parse()
        assert_matches_type(SyncSinglePage[PacfileListResponse], pacfile, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.pacfiles.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pacfile = response.parse()
            assert_matches_type(SyncSinglePage[PacfileListResponse], pacfile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.pacfiles.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        pacfile = client.zero_trust.gateway.pacfiles.delete(
            pacfile_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(object, pacfile, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.pacfiles.with_raw_response.delete(
            pacfile_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pacfile = response.parse()
        assert_matches_type(object, pacfile, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.pacfiles.with_streaming_response.delete(
            pacfile_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pacfile = response.parse()
            assert_matches_type(object, pacfile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.pacfiles.with_raw_response.delete(
                pacfile_id="ed35569b41ce4d1facfe683550f54086",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pacfile_id` but received ''"):
            client.zero_trust.gateway.pacfiles.with_raw_response.delete(
                pacfile_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        pacfile = client.zero_trust.gateway.pacfiles.get(
            pacfile_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[PacfileGetResponse], pacfile, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.pacfiles.with_raw_response.get(
            pacfile_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pacfile = response.parse()
        assert_matches_type(Optional[PacfileGetResponse], pacfile, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.pacfiles.with_streaming_response.get(
            pacfile_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pacfile = response.parse()
            assert_matches_type(Optional[PacfileGetResponse], pacfile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.pacfiles.with_raw_response.get(
                pacfile_id="ed35569b41ce4d1facfe683550f54086",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pacfile_id` but received ''"):
            client.zero_trust.gateway.pacfiles.with_raw_response.get(
                pacfile_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncPacfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        pacfile = await async_client.zero_trust.gateway.pacfiles.create(
            account_id="699d98642c564d2e855e9661899b7252",
            contents='function FindProxyForURL(url, host) { return "DIRECT"; }',
            name="Devops team",
        )
        assert_matches_type(Optional[PacfileCreateResponse], pacfile, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        pacfile = await async_client.zero_trust.gateway.pacfiles.create(
            account_id="699d98642c564d2e855e9661899b7252",
            contents='function FindProxyForURL(url, host) { return "DIRECT"; }',
            name="Devops team",
            description="PAC file for Devops team",
            slug="pac_devops",
        )
        assert_matches_type(Optional[PacfileCreateResponse], pacfile, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.pacfiles.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            contents='function FindProxyForURL(url, host) { return "DIRECT"; }',
            name="Devops team",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pacfile = await response.parse()
        assert_matches_type(Optional[PacfileCreateResponse], pacfile, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.pacfiles.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            contents='function FindProxyForURL(url, host) { return "DIRECT"; }',
            name="Devops team",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pacfile = await response.parse()
            assert_matches_type(Optional[PacfileCreateResponse], pacfile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.pacfiles.with_raw_response.create(
                account_id="",
                contents='function FindProxyForURL(url, host) { return "DIRECT"; }',
                name="Devops team",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        pacfile = await async_client.zero_trust.gateway.pacfiles.update(
            pacfile_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            contents='function FindProxyForURL(url, host) { return "DIRECT"; }',
            description="PAC file for Devops team",
            name="Devops team",
        )
        assert_matches_type(Optional[PacfileUpdateResponse], pacfile, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.pacfiles.with_raw_response.update(
            pacfile_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            contents='function FindProxyForURL(url, host) { return "DIRECT"; }',
            description="PAC file for Devops team",
            name="Devops team",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pacfile = await response.parse()
        assert_matches_type(Optional[PacfileUpdateResponse], pacfile, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.pacfiles.with_streaming_response.update(
            pacfile_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            contents='function FindProxyForURL(url, host) { return "DIRECT"; }',
            description="PAC file for Devops team",
            name="Devops team",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pacfile = await response.parse()
            assert_matches_type(Optional[PacfileUpdateResponse], pacfile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.pacfiles.with_raw_response.update(
                pacfile_id="ed35569b41ce4d1facfe683550f54086",
                account_id="",
                contents='function FindProxyForURL(url, host) { return "DIRECT"; }',
                description="PAC file for Devops team",
                name="Devops team",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pacfile_id` but received ''"):
            await async_client.zero_trust.gateway.pacfiles.with_raw_response.update(
                pacfile_id="",
                account_id="699d98642c564d2e855e9661899b7252",
                contents='function FindProxyForURL(url, host) { return "DIRECT"; }',
                description="PAC file for Devops team",
                name="Devops team",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        pacfile = await async_client.zero_trust.gateway.pacfiles.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(AsyncSinglePage[PacfileListResponse], pacfile, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.pacfiles.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pacfile = await response.parse()
        assert_matches_type(AsyncSinglePage[PacfileListResponse], pacfile, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.pacfiles.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pacfile = await response.parse()
            assert_matches_type(AsyncSinglePage[PacfileListResponse], pacfile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.pacfiles.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        pacfile = await async_client.zero_trust.gateway.pacfiles.delete(
            pacfile_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(object, pacfile, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.pacfiles.with_raw_response.delete(
            pacfile_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pacfile = await response.parse()
        assert_matches_type(object, pacfile, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.pacfiles.with_streaming_response.delete(
            pacfile_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pacfile = await response.parse()
            assert_matches_type(object, pacfile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.pacfiles.with_raw_response.delete(
                pacfile_id="ed35569b41ce4d1facfe683550f54086",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pacfile_id` but received ''"):
            await async_client.zero_trust.gateway.pacfiles.with_raw_response.delete(
                pacfile_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        pacfile = await async_client.zero_trust.gateway.pacfiles.get(
            pacfile_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[PacfileGetResponse], pacfile, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.pacfiles.with_raw_response.get(
            pacfile_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pacfile = await response.parse()
        assert_matches_type(Optional[PacfileGetResponse], pacfile, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.pacfiles.with_streaming_response.get(
            pacfile_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pacfile = await response.parse()
            assert_matches_type(Optional[PacfileGetResponse], pacfile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.pacfiles.with_raw_response.get(
                pacfile_id="ed35569b41ce4d1facfe683550f54086",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pacfile_id` but received ''"):
            await async_client.zero_trust.gateway.pacfiles.with_raw_response.get(
                pacfile_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )
