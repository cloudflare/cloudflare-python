# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.secondary_dns import (
    OutgoingGetResponse,
    OutgoingCreateResponse,
    OutgoingDeleteResponse,
    OutgoingUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOutgoing:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        outgoing = client.secondary_dns.outgoing.create(
            "269d8f4853475ca241c4e730be286b20",
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )
        assert_matches_type(OutgoingCreateResponse, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.secondary_dns.outgoing.with_raw_response.create(
            "269d8f4853475ca241c4e730be286b20",
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = response.parse()
        assert_matches_type(OutgoingCreateResponse, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.secondary_dns.outgoing.with_streaming_response.create(
            "269d8f4853475ca241c4e730be286b20",
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = response.parse()
            assert_matches_type(OutgoingCreateResponse, outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        outgoing = client.secondary_dns.outgoing.update(
            "269d8f4853475ca241c4e730be286b20",
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )
        assert_matches_type(OutgoingUpdateResponse, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.secondary_dns.outgoing.with_raw_response.update(
            "269d8f4853475ca241c4e730be286b20",
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = response.parse()
        assert_matches_type(OutgoingUpdateResponse, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.secondary_dns.outgoing.with_streaming_response.update(
            "269d8f4853475ca241c4e730be286b20",
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = response.parse()
            assert_matches_type(OutgoingUpdateResponse, outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        outgoing = client.secondary_dns.outgoing.delete(
            "269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(OutgoingDeleteResponse, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.secondary_dns.outgoing.with_raw_response.delete(
            "269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = response.parse()
        assert_matches_type(OutgoingDeleteResponse, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.secondary_dns.outgoing.with_streaming_response.delete(
            "269d8f4853475ca241c4e730be286b20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = response.parse()
            assert_matches_type(OutgoingDeleteResponse, outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_disable(self, client: Cloudflare) -> None:
        outgoing = client.secondary_dns.outgoing.disable(
            "269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(str, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_disable(self, client: Cloudflare) -> None:
        response = client.secondary_dns.outgoing.with_raw_response.disable(
            "269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = response.parse()
        assert_matches_type(str, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_disable(self, client: Cloudflare) -> None:
        with client.secondary_dns.outgoing.with_streaming_response.disable(
            "269d8f4853475ca241c4e730be286b20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = response.parse()
            assert_matches_type(str, outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_enable(self, client: Cloudflare) -> None:
        outgoing = client.secondary_dns.outgoing.enable(
            "269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(str, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_enable(self, client: Cloudflare) -> None:
        response = client.secondary_dns.outgoing.with_raw_response.enable(
            "269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = response.parse()
        assert_matches_type(str, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_enable(self, client: Cloudflare) -> None:
        with client.secondary_dns.outgoing.with_streaming_response.enable(
            "269d8f4853475ca241c4e730be286b20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = response.parse()
            assert_matches_type(str, outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_force_notify(self, client: Cloudflare) -> None:
        outgoing = client.secondary_dns.outgoing.force_notify(
            "269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(str, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_force_notify(self, client: Cloudflare) -> None:
        response = client.secondary_dns.outgoing.with_raw_response.force_notify(
            "269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = response.parse()
        assert_matches_type(str, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_force_notify(self, client: Cloudflare) -> None:
        with client.secondary_dns.outgoing.with_streaming_response.force_notify(
            "269d8f4853475ca241c4e730be286b20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = response.parse()
            assert_matches_type(str, outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        outgoing = client.secondary_dns.outgoing.get(
            "269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(OutgoingGetResponse, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.secondary_dns.outgoing.with_raw_response.get(
            "269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = response.parse()
        assert_matches_type(OutgoingGetResponse, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.secondary_dns.outgoing.with_streaming_response.get(
            "269d8f4853475ca241c4e730be286b20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = response.parse()
            assert_matches_type(OutgoingGetResponse, outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOutgoing:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        outgoing = await async_client.secondary_dns.outgoing.create(
            "269d8f4853475ca241c4e730be286b20",
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )
        assert_matches_type(OutgoingCreateResponse, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secondary_dns.outgoing.with_raw_response.create(
            "269d8f4853475ca241c4e730be286b20",
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = await response.parse()
        assert_matches_type(OutgoingCreateResponse, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secondary_dns.outgoing.with_streaming_response.create(
            "269d8f4853475ca241c4e730be286b20",
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = await response.parse()
            assert_matches_type(OutgoingCreateResponse, outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        outgoing = await async_client.secondary_dns.outgoing.update(
            "269d8f4853475ca241c4e730be286b20",
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )
        assert_matches_type(OutgoingUpdateResponse, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secondary_dns.outgoing.with_raw_response.update(
            "269d8f4853475ca241c4e730be286b20",
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = await response.parse()
        assert_matches_type(OutgoingUpdateResponse, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secondary_dns.outgoing.with_streaming_response.update(
            "269d8f4853475ca241c4e730be286b20",
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = await response.parse()
            assert_matches_type(OutgoingUpdateResponse, outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        outgoing = await async_client.secondary_dns.outgoing.delete(
            "269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(OutgoingDeleteResponse, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secondary_dns.outgoing.with_raw_response.delete(
            "269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = await response.parse()
        assert_matches_type(OutgoingDeleteResponse, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secondary_dns.outgoing.with_streaming_response.delete(
            "269d8f4853475ca241c4e730be286b20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = await response.parse()
            assert_matches_type(OutgoingDeleteResponse, outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_disable(self, async_client: AsyncCloudflare) -> None:
        outgoing = await async_client.secondary_dns.outgoing.disable(
            "269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(str, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_disable(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secondary_dns.outgoing.with_raw_response.disable(
            "269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = await response.parse()
        assert_matches_type(str, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_disable(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secondary_dns.outgoing.with_streaming_response.disable(
            "269d8f4853475ca241c4e730be286b20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = await response.parse()
            assert_matches_type(str, outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_enable(self, async_client: AsyncCloudflare) -> None:
        outgoing = await async_client.secondary_dns.outgoing.enable(
            "269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(str, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_enable(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secondary_dns.outgoing.with_raw_response.enable(
            "269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = await response.parse()
        assert_matches_type(str, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_enable(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secondary_dns.outgoing.with_streaming_response.enable(
            "269d8f4853475ca241c4e730be286b20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = await response.parse()
            assert_matches_type(str, outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_force_notify(self, async_client: AsyncCloudflare) -> None:
        outgoing = await async_client.secondary_dns.outgoing.force_notify(
            "269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(str, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_force_notify(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secondary_dns.outgoing.with_raw_response.force_notify(
            "269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = await response.parse()
        assert_matches_type(str, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_force_notify(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secondary_dns.outgoing.with_streaming_response.force_notify(
            "269d8f4853475ca241c4e730be286b20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = await response.parse()
            assert_matches_type(str, outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        outgoing = await async_client.secondary_dns.outgoing.get(
            "269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(OutgoingGetResponse, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secondary_dns.outgoing.with_raw_response.get(
            "269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        outgoing = await response.parse()
        assert_matches_type(OutgoingGetResponse, outgoing, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secondary_dns.outgoing.with_streaming_response.get(
            "269d8f4853475ca241c4e730be286b20",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            outgoing = await response.parse()
            assert_matches_type(OutgoingGetResponse, outgoing, path=["response"])

        assert cast(Any, response.is_closed) is True
