# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.secondary_dns import (
    TSIGGetResponse,
    TSIGListResponse,
    TSIGCreateResponse,
    TSIGDeleteResponse,
    TSIGUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTSIGs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        tsig = client.secondary_dns.tsigs.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            algo="hmac-sha512.",
            name="tsig.customer.cf.",
            secret="caf79a7804b04337c9c66ccd7bef9190a1e1679b5dd03d8aa10f7ad45e1a9dab92b417896c15d4d007c7c14194538d2a5d0feffdecc5a7f0e1c570cfa700837c",
        )
        assert_matches_type(TSIGCreateResponse, tsig, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.secondary_dns.tsigs.with_raw_response.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            algo="hmac-sha512.",
            name="tsig.customer.cf.",
            secret="caf79a7804b04337c9c66ccd7bef9190a1e1679b5dd03d8aa10f7ad45e1a9dab92b417896c15d4d007c7c14194538d2a5d0feffdecc5a7f0e1c570cfa700837c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tsig = response.parse()
        assert_matches_type(TSIGCreateResponse, tsig, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.secondary_dns.tsigs.with_streaming_response.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            algo="hmac-sha512.",
            name="tsig.customer.cf.",
            secret="caf79a7804b04337c9c66ccd7bef9190a1e1679b5dd03d8aa10f7ad45e1a9dab92b417896c15d4d007c7c14194538d2a5d0feffdecc5a7f0e1c570cfa700837c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tsig = response.parse()
            assert_matches_type(TSIGCreateResponse, tsig, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        tsig = client.secondary_dns.tsigs.update(
            "69cd1e104af3e6ed3cb344f263fd0d5a",
            account_id="01a7362d577a6c3019a474fd6f485823",
            algo="hmac-sha512.",
            name="tsig.customer.cf.",
            secret="caf79a7804b04337c9c66ccd7bef9190a1e1679b5dd03d8aa10f7ad45e1a9dab92b417896c15d4d007c7c14194538d2a5d0feffdecc5a7f0e1c570cfa700837c",
        )
        assert_matches_type(TSIGUpdateResponse, tsig, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.secondary_dns.tsigs.with_raw_response.update(
            "69cd1e104af3e6ed3cb344f263fd0d5a",
            account_id="01a7362d577a6c3019a474fd6f485823",
            algo="hmac-sha512.",
            name="tsig.customer.cf.",
            secret="caf79a7804b04337c9c66ccd7bef9190a1e1679b5dd03d8aa10f7ad45e1a9dab92b417896c15d4d007c7c14194538d2a5d0feffdecc5a7f0e1c570cfa700837c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tsig = response.parse()
        assert_matches_type(TSIGUpdateResponse, tsig, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.secondary_dns.tsigs.with_streaming_response.update(
            "69cd1e104af3e6ed3cb344f263fd0d5a",
            account_id="01a7362d577a6c3019a474fd6f485823",
            algo="hmac-sha512.",
            name="tsig.customer.cf.",
            secret="caf79a7804b04337c9c66ccd7bef9190a1e1679b5dd03d8aa10f7ad45e1a9dab92b417896c15d4d007c7c14194538d2a5d0feffdecc5a7f0e1c570cfa700837c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tsig = response.parse()
            assert_matches_type(TSIGUpdateResponse, tsig, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        tsig = client.secondary_dns.tsigs.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(Optional[TSIGListResponse], tsig, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.secondary_dns.tsigs.with_raw_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tsig = response.parse()
        assert_matches_type(Optional[TSIGListResponse], tsig, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.secondary_dns.tsigs.with_streaming_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tsig = response.parse()
            assert_matches_type(Optional[TSIGListResponse], tsig, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        tsig = client.secondary_dns.tsigs.delete(
            "69cd1e104af3e6ed3cb344f263fd0d5a",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(TSIGDeleteResponse, tsig, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.secondary_dns.tsigs.with_raw_response.delete(
            "69cd1e104af3e6ed3cb344f263fd0d5a",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tsig = response.parse()
        assert_matches_type(TSIGDeleteResponse, tsig, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.secondary_dns.tsigs.with_streaming_response.delete(
            "69cd1e104af3e6ed3cb344f263fd0d5a",
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tsig = response.parse()
            assert_matches_type(TSIGDeleteResponse, tsig, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        tsig = client.secondary_dns.tsigs.get(
            "69cd1e104af3e6ed3cb344f263fd0d5a",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(TSIGGetResponse, tsig, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.secondary_dns.tsigs.with_raw_response.get(
            "69cd1e104af3e6ed3cb344f263fd0d5a",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tsig = response.parse()
        assert_matches_type(TSIGGetResponse, tsig, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.secondary_dns.tsigs.with_streaming_response.get(
            "69cd1e104af3e6ed3cb344f263fd0d5a",
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tsig = response.parse()
            assert_matches_type(TSIGGetResponse, tsig, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTSIGs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        tsig = await async_client.secondary_dns.tsigs.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            algo="hmac-sha512.",
            name="tsig.customer.cf.",
            secret="caf79a7804b04337c9c66ccd7bef9190a1e1679b5dd03d8aa10f7ad45e1a9dab92b417896c15d4d007c7c14194538d2a5d0feffdecc5a7f0e1c570cfa700837c",
        )
        assert_matches_type(TSIGCreateResponse, tsig, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secondary_dns.tsigs.with_raw_response.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            algo="hmac-sha512.",
            name="tsig.customer.cf.",
            secret="caf79a7804b04337c9c66ccd7bef9190a1e1679b5dd03d8aa10f7ad45e1a9dab92b417896c15d4d007c7c14194538d2a5d0feffdecc5a7f0e1c570cfa700837c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tsig = await response.parse()
        assert_matches_type(TSIGCreateResponse, tsig, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secondary_dns.tsigs.with_streaming_response.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            algo="hmac-sha512.",
            name="tsig.customer.cf.",
            secret="caf79a7804b04337c9c66ccd7bef9190a1e1679b5dd03d8aa10f7ad45e1a9dab92b417896c15d4d007c7c14194538d2a5d0feffdecc5a7f0e1c570cfa700837c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tsig = await response.parse()
            assert_matches_type(TSIGCreateResponse, tsig, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        tsig = await async_client.secondary_dns.tsigs.update(
            "69cd1e104af3e6ed3cb344f263fd0d5a",
            account_id="01a7362d577a6c3019a474fd6f485823",
            algo="hmac-sha512.",
            name="tsig.customer.cf.",
            secret="caf79a7804b04337c9c66ccd7bef9190a1e1679b5dd03d8aa10f7ad45e1a9dab92b417896c15d4d007c7c14194538d2a5d0feffdecc5a7f0e1c570cfa700837c",
        )
        assert_matches_type(TSIGUpdateResponse, tsig, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secondary_dns.tsigs.with_raw_response.update(
            "69cd1e104af3e6ed3cb344f263fd0d5a",
            account_id="01a7362d577a6c3019a474fd6f485823",
            algo="hmac-sha512.",
            name="tsig.customer.cf.",
            secret="caf79a7804b04337c9c66ccd7bef9190a1e1679b5dd03d8aa10f7ad45e1a9dab92b417896c15d4d007c7c14194538d2a5d0feffdecc5a7f0e1c570cfa700837c",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tsig = await response.parse()
        assert_matches_type(TSIGUpdateResponse, tsig, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secondary_dns.tsigs.with_streaming_response.update(
            "69cd1e104af3e6ed3cb344f263fd0d5a",
            account_id="01a7362d577a6c3019a474fd6f485823",
            algo="hmac-sha512.",
            name="tsig.customer.cf.",
            secret="caf79a7804b04337c9c66ccd7bef9190a1e1679b5dd03d8aa10f7ad45e1a9dab92b417896c15d4d007c7c14194538d2a5d0feffdecc5a7f0e1c570cfa700837c",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tsig = await response.parse()
            assert_matches_type(TSIGUpdateResponse, tsig, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        tsig = await async_client.secondary_dns.tsigs.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(Optional[TSIGListResponse], tsig, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secondary_dns.tsigs.with_raw_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tsig = await response.parse()
        assert_matches_type(Optional[TSIGListResponse], tsig, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secondary_dns.tsigs.with_streaming_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tsig = await response.parse()
            assert_matches_type(Optional[TSIGListResponse], tsig, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        tsig = await async_client.secondary_dns.tsigs.delete(
            "69cd1e104af3e6ed3cb344f263fd0d5a",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(TSIGDeleteResponse, tsig, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secondary_dns.tsigs.with_raw_response.delete(
            "69cd1e104af3e6ed3cb344f263fd0d5a",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tsig = await response.parse()
        assert_matches_type(TSIGDeleteResponse, tsig, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secondary_dns.tsigs.with_streaming_response.delete(
            "69cd1e104af3e6ed3cb344f263fd0d5a",
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tsig = await response.parse()
            assert_matches_type(TSIGDeleteResponse, tsig, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        tsig = await async_client.secondary_dns.tsigs.get(
            "69cd1e104af3e6ed3cb344f263fd0d5a",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(TSIGGetResponse, tsig, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secondary_dns.tsigs.with_raw_response.get(
            "69cd1e104af3e6ed3cb344f263fd0d5a",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tsig = await response.parse()
        assert_matches_type(TSIGGetResponse, tsig, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secondary_dns.tsigs.with_streaming_response.get(
            "69cd1e104af3e6ed3cb344f263fd0d5a",
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tsig = await response.parse()
            assert_matches_type(TSIGGetResponse, tsig, path=["response"])

        assert cast(Any, response.is_closed) is True
