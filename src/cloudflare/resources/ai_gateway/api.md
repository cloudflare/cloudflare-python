# AIGateway

Types:

```python
from cloudflare.types.ai_gateway import (
    AIGatewayCreateResponse,
    AIGatewayUpdateResponse,
    AIGatewayListResponse,
    AIGatewayDeleteResponse,
    AIGatewayGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/ai-gateway/gateways">client.ai_gateway.<a href="./src/cloudflare/resources/ai_gateway/ai_gateway.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/ai_gateway/ai_gateway_create_params.py">params</a>) -> <a href="./src/cloudflare/types/ai_gateway/ai_gateway_create_response.py">AIGatewayCreateResponse</a></code>
- <code title="put /accounts/{account_id}/ai-gateway/gateways/{id}">client.ai_gateway.<a href="./src/cloudflare/resources/ai_gateway/ai_gateway.py">update</a>(id, \*, account_id, \*\*<a href="src/cloudflare/types/ai_gateway/ai_gateway_update_params.py">params</a>) -> <a href="./src/cloudflare/types/ai_gateway/ai_gateway_update_response.py">AIGatewayUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/ai-gateway/gateways">client.ai_gateway.<a href="./src/cloudflare/resources/ai_gateway/ai_gateway.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/ai_gateway/ai_gateway_list_params.py">params</a>) -> <a href="./src/cloudflare/types/ai_gateway/ai_gateway_list_response.py">SyncV4PagePaginationArray[AIGatewayListResponse]</a></code>
- <code title="delete /accounts/{account_id}/ai-gateway/gateways/{id}">client.ai_gateway.<a href="./src/cloudflare/resources/ai_gateway/ai_gateway.py">delete</a>(id, \*, account_id) -> <a href="./src/cloudflare/types/ai_gateway/ai_gateway_delete_response.py">AIGatewayDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/ai-gateway/gateways/{id}">client.ai_gateway.<a href="./src/cloudflare/resources/ai_gateway/ai_gateway.py">get</a>(id, \*, account_id) -> <a href="./src/cloudflare/types/ai_gateway/ai_gateway_get_response.py">AIGatewayGetResponse</a></code>

## EvaluationTypes

Types:

```python
from cloudflare.types.ai_gateway import EvaluationTypeListResponse
```

Methods:

- <code title="get /accounts/{account_id}/ai-gateway/evaluation-types">client.ai_gateway.evaluation_types.<a href="./src/cloudflare/resources/ai_gateway/evaluation_types.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/ai_gateway/evaluation_type_list_params.py">params</a>) -> <a href="./src/cloudflare/types/ai_gateway/evaluation_type_list_response.py">SyncV4PagePaginationArray[EvaluationTypeListResponse]</a></code>

## Logs

Types:

```python
from cloudflare.types.ai_gateway import LogListResponse, LogDeleteResponse, LogGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs">client.ai_gateway.logs.<a href="./src/cloudflare/resources/ai_gateway/logs.py">list</a>(gateway_id, \*, account_id, \*\*<a href="src/cloudflare/types/ai_gateway/log_list_params.py">params</a>) -> <a href="./src/cloudflare/types/ai_gateway/log_list_response.py">SyncV4PagePaginationArray[LogListResponse]</a></code>
- <code title="delete /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs">client.ai_gateway.logs.<a href="./src/cloudflare/resources/ai_gateway/logs.py">delete</a>(gateway_id, \*, account_id, \*\*<a href="src/cloudflare/types/ai_gateway/log_delete_params.py">params</a>) -> <a href="./src/cloudflare/types/ai_gateway/log_delete_response.py">LogDeleteResponse</a></code>
- <code title="patch /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}">client.ai_gateway.logs.<a href="./src/cloudflare/resources/ai_gateway/logs.py">edit</a>(id, \*, account_id, gateway_id, \*\*<a href="src/cloudflare/types/ai_gateway/log_edit_params.py">params</a>) -> object</code>
- <code title="get /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}">client.ai_gateway.logs.<a href="./src/cloudflare/resources/ai_gateway/logs.py">get</a>(id, \*, account_id, gateway_id) -> <a href="./src/cloudflare/types/ai_gateway/log_get_response.py">LogGetResponse</a></code>
- <code title="get /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}/request">client.ai_gateway.logs.<a href="./src/cloudflare/resources/ai_gateway/logs.py">request</a>(id, \*, account_id, gateway_id) -> object</code>
- <code title="get /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/logs/{id}/response">client.ai_gateway.logs.<a href="./src/cloudflare/resources/ai_gateway/logs.py">response</a>(id, \*, account_id, gateway_id) -> object</code>

## Datasets

Types:

```python
from cloudflare.types.ai_gateway import (
    DatasetCreateResponse,
    DatasetUpdateResponse,
    DatasetListResponse,
    DatasetDeleteResponse,
    DatasetGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/datasets">client.ai_gateway.datasets.<a href="./src/cloudflare/resources/ai_gateway/datasets.py">create</a>(gateway_id, \*, account_id, \*\*<a href="src/cloudflare/types/ai_gateway/dataset_create_params.py">params</a>) -> <a href="./src/cloudflare/types/ai_gateway/dataset_create_response.py">DatasetCreateResponse</a></code>
- <code title="put /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/datasets/{id}">client.ai_gateway.datasets.<a href="./src/cloudflare/resources/ai_gateway/datasets.py">update</a>(id, \*, account_id, gateway_id, \*\*<a href="src/cloudflare/types/ai_gateway/dataset_update_params.py">params</a>) -> <a href="./src/cloudflare/types/ai_gateway/dataset_update_response.py">DatasetUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/datasets">client.ai_gateway.datasets.<a href="./src/cloudflare/resources/ai_gateway/datasets.py">list</a>(gateway_id, \*, account_id, \*\*<a href="src/cloudflare/types/ai_gateway/dataset_list_params.py">params</a>) -> <a href="./src/cloudflare/types/ai_gateway/dataset_list_response.py">SyncV4PagePaginationArray[DatasetListResponse]</a></code>
- <code title="delete /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/datasets/{id}">client.ai_gateway.datasets.<a href="./src/cloudflare/resources/ai_gateway/datasets.py">delete</a>(id, \*, account_id, gateway_id) -> <a href="./src/cloudflare/types/ai_gateway/dataset_delete_response.py">DatasetDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/datasets/{id}">client.ai_gateway.datasets.<a href="./src/cloudflare/resources/ai_gateway/datasets.py">get</a>(id, \*, account_id, gateway_id) -> <a href="./src/cloudflare/types/ai_gateway/dataset_get_response.py">DatasetGetResponse</a></code>

## Evaluations

Types:

```python
from cloudflare.types.ai_gateway import (
    EvaluationCreateResponse,
    EvaluationListResponse,
    EvaluationDeleteResponse,
    EvaluationGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations">client.ai_gateway.evaluations.<a href="./src/cloudflare/resources/ai_gateway/evaluations.py">create</a>(gateway_id, \*, account_id, \*\*<a href="src/cloudflare/types/ai_gateway/evaluation_create_params.py">params</a>) -> <a href="./src/cloudflare/types/ai_gateway/evaluation_create_response.py">EvaluationCreateResponse</a></code>
- <code title="get /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations">client.ai_gateway.evaluations.<a href="./src/cloudflare/resources/ai_gateway/evaluations.py">list</a>(gateway_id, \*, account_id, \*\*<a href="src/cloudflare/types/ai_gateway/evaluation_list_params.py">params</a>) -> <a href="./src/cloudflare/types/ai_gateway/evaluation_list_response.py">SyncV4PagePaginationArray[EvaluationListResponse]</a></code>
- <code title="delete /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations/{id}">client.ai_gateway.evaluations.<a href="./src/cloudflare/resources/ai_gateway/evaluations.py">delete</a>(id, \*, account_id, gateway_id) -> <a href="./src/cloudflare/types/ai_gateway/evaluation_delete_response.py">EvaluationDeleteResponse</a></code>
- <code title="get /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/evaluations/{id}">client.ai_gateway.evaluations.<a href="./src/cloudflare/resources/ai_gateway/evaluations.py">get</a>(id, \*, account_id, gateway_id) -> <a href="./src/cloudflare/types/ai_gateway/evaluation_get_response.py">EvaluationGetResponse</a></code>

## DynamicRouting

Types:

```python
from cloudflare.types.ai_gateway import (
    DynamicRoutingCreateResponse,
    DynamicRoutingUpdateResponse,
    DynamicRoutingListResponse,
    DynamicRoutingDeleteResponse,
    DynamicRoutingCreateDeploymentResponse,
    DynamicRoutingCreateVersionResponse,
    DynamicRoutingGetResponse,
    DynamicRoutingGetVersionResponse,
    DynamicRoutingListDeploymentsResponse,
    DynamicRoutingListVersionsResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes">client.ai_gateway.dynamic_routing.<a href="./src/cloudflare/resources/ai_gateway/dynamic_routing.py">create</a>(gateway_id, \*, account_id, \*\*<a href="src/cloudflare/types/ai_gateway/dynamic_routing_create_params.py">params</a>) -> <a href="./src/cloudflare/types/ai_gateway/dynamic_routing_create_response.py">DynamicRoutingCreateResponse</a></code>
- <code title="patch /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}">client.ai_gateway.dynamic_routing.<a href="./src/cloudflare/resources/ai_gateway/dynamic_routing.py">update</a>(id, \*, account_id, gateway_id, \*\*<a href="src/cloudflare/types/ai_gateway/dynamic_routing_update_params.py">params</a>) -> <a href="./src/cloudflare/types/ai_gateway/dynamic_routing_update_response.py">DynamicRoutingUpdateResponse</a></code>
- <code title="get /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes">client.ai_gateway.dynamic_routing.<a href="./src/cloudflare/resources/ai_gateway/dynamic_routing.py">list</a>(gateway_id, \*, account_id) -> <a href="./src/cloudflare/types/ai_gateway/dynamic_routing_list_response.py">DynamicRoutingListResponse</a></code>
- <code title="delete /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}">client.ai_gateway.dynamic_routing.<a href="./src/cloudflare/resources/ai_gateway/dynamic_routing.py">delete</a>(id, \*, account_id, gateway_id) -> <a href="./src/cloudflare/types/ai_gateway/dynamic_routing_delete_response.py">DynamicRoutingDeleteResponse</a></code>
- <code title="post /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/deployments">client.ai_gateway.dynamic_routing.<a href="./src/cloudflare/resources/ai_gateway/dynamic_routing.py">create_deployment</a>(id, \*, account_id, gateway_id, \*\*<a href="src/cloudflare/types/ai_gateway/dynamic_routing_create_deployment_params.py">params</a>) -> <a href="./src/cloudflare/types/ai_gateway/dynamic_routing_create_deployment_response.py">DynamicRoutingCreateDeploymentResponse</a></code>
- <code title="post /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/versions">client.ai_gateway.dynamic_routing.<a href="./src/cloudflare/resources/ai_gateway/dynamic_routing.py">create_version</a>(id, \*, account_id, gateway_id, \*\*<a href="src/cloudflare/types/ai_gateway/dynamic_routing_create_version_params.py">params</a>) -> <a href="./src/cloudflare/types/ai_gateway/dynamic_routing_create_version_response.py">DynamicRoutingCreateVersionResponse</a></code>
- <code title="get /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}">client.ai_gateway.dynamic_routing.<a href="./src/cloudflare/resources/ai_gateway/dynamic_routing.py">get</a>(id, \*, account_id, gateway_id) -> <a href="./src/cloudflare/types/ai_gateway/dynamic_routing_get_response.py">DynamicRoutingGetResponse</a></code>
- <code title="get /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/versions/{version_id}">client.ai_gateway.dynamic_routing.<a href="./src/cloudflare/resources/ai_gateway/dynamic_routing.py">get_version</a>(version_id, \*, account_id, gateway_id, id) -> <a href="./src/cloudflare/types/ai_gateway/dynamic_routing_get_version_response.py">DynamicRoutingGetVersionResponse</a></code>
- <code title="get /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/deployments">client.ai_gateway.dynamic_routing.<a href="./src/cloudflare/resources/ai_gateway/dynamic_routing.py">list_deployments</a>(id, \*, account_id, gateway_id) -> <a href="./src/cloudflare/types/ai_gateway/dynamic_routing_list_deployments_response.py">DynamicRoutingListDeploymentsResponse</a></code>
- <code title="get /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/routes/{id}/versions">client.ai_gateway.dynamic_routing.<a href="./src/cloudflare/resources/ai_gateway/dynamic_routing.py">list_versions</a>(id, \*, account_id, gateway_id) -> <a href="./src/cloudflare/types/ai_gateway/dynamic_routing_list_versions_response.py">DynamicRoutingListVersionsResponse</a></code>

## ProviderConfigs

Types:

```python
from cloudflare.types.ai_gateway import ProviderConfigCreateResponse, ProviderConfigListResponse
```

Methods:

- <code title="post /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/provider_configs">client.ai_gateway.provider_configs.<a href="./src/cloudflare/resources/ai_gateway/provider_configs.py">create</a>(gateway_id, \*, account_id, \*\*<a href="src/cloudflare/types/ai_gateway/provider_config_create_params.py">params</a>) -> <a href="./src/cloudflare/types/ai_gateway/provider_config_create_response.py">ProviderConfigCreateResponse</a></code>
- <code title="get /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/provider_configs">client.ai_gateway.provider_configs.<a href="./src/cloudflare/resources/ai_gateway/provider_configs.py">list</a>(gateway_id, \*, account_id, \*\*<a href="src/cloudflare/types/ai_gateway/provider_config_list_params.py">params</a>) -> <a href="./src/cloudflare/types/ai_gateway/provider_config_list_response.py">SyncV4PagePaginationArray[ProviderConfigListResponse]</a></code>

## URLs

Types:

```python
from cloudflare.types.ai_gateway import URLGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/ai-gateway/gateways/{gateway_id}/url/{provider}">client.ai_gateway.urls.<a href="./src/cloudflare/resources/ai_gateway/urls.py">get</a>(provider, \*, account_id, gateway_id) -> <a href="./src/cloudflare/types/ai_gateway/url_get_response.py">str</a></code>
