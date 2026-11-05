from __future__ import annotations

import httpx
import pytest

from cloudflare import Cloudflare, AsyncCloudflare


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize(
    "model_name,expected_suffix",
    [
        ("@cf/meta/llama-3.1-8b-instruct", "@cf/meta/llama-3.1-8b-instruct"),
        ("@cf/black-forest-labs/flux-1-schnell", "@cf/black-forest-labs/flux-1-schnell"),
        ("@cf/model?query#fragment%", "@cf/model%3Fquery%23fragment%25"),
        ("model", "model"),
    ],
)
async def test_model_path_preserves_slashes(asynchronous: bool, model_name: str, expected_suffix: str) -> None:
    expected_path = f"/client/v4/accounts/account%2Fid/ai/run/{expected_suffix}".encode()

    def handle(request: httpx.Request) -> httpx.Response:
        assert request.url.raw_path == expected_path
        assert not request.url.query
        assert not request.url.fragment
        return httpx.Response(200, json={"success": True, "result": {"response": "ok"}})

    transport = httpx.MockTransport(handle)
    if asynchronous:
        async with AsyncCloudflare(
            api_token="test-token", http_client=httpx.AsyncClient(transport=transport)
        ) as client:
            await client.ai.run(model_name, account_id="account/id", prompt="Hello")
    else:
        with Cloudflare(api_token="test-token", http_client=httpx.Client(transport=transport)) as sync_client:
            sync_client.ai.run(model_name, account_id="account/id", prompt="Hello")


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("model_name", ["@cf/../model", "@cf/./model"])
async def test_model_path_rejects_dot_segments(asynchronous: bool, model_name: str) -> None:
    def handle(_request: httpx.Request) -> httpx.Response:
        pytest.fail("A dot-segment model must be rejected before an HTTP request is sent")

    transport = httpx.MockTransport(handle)
    if asynchronous:
        async with AsyncCloudflare(
            api_token="test-token", http_client=httpx.AsyncClient(transport=transport)
        ) as client:
            with pytest.raises(ValueError, match="dot-segment"):
                await client.ai.run(model_name, account_id="account", prompt="Hello")
    else:
        with Cloudflare(api_token="test-token", http_client=httpx.Client(transport=transport)) as sync_client:
            with pytest.raises(ValueError, match="dot-segment"):
                sync_client.ai.run(model_name, account_id="account", prompt="Hello")
