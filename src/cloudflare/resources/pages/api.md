# Pages

## Projects

Types:

```python
from cloudflare.types.pages import Deployment, Project, Stage
```

Methods:

- <code title="post /accounts/{account_id}/pages/projects">client.pages.projects.<a href="./src/cloudflare/resources/pages/projects/projects.py">create</a>(\*, account_id, \*\*<a href="src/cloudflare/types/pages/project_create_params.py">params</a>) -> <a href="./src/cloudflare/types/pages/project.py">Project</a></code>
- <code title="get /accounts/{account_id}/pages/projects">client.pages.projects.<a href="./src/cloudflare/resources/pages/projects/projects.py">list</a>(\*, account_id, \*\*<a href="src/cloudflare/types/pages/project_list_params.py">params</a>) -> <a href="./src/cloudflare/types/pages/project.py">SyncV4PagePaginationArray[Project]</a></code>
- <code title="delete /accounts/{account_id}/pages/projects/{project_name}">client.pages.projects.<a href="./src/cloudflare/resources/pages/projects/projects.py">delete</a>(project_name, \*, account_id) -> object</code>
- <code title="patch /accounts/{account_id}/pages/projects/{project_name}">client.pages.projects.<a href="./src/cloudflare/resources/pages/projects/projects.py">edit</a>(project_name, \*, account_id, \*\*<a href="src/cloudflare/types/pages/project_edit_params.py">params</a>) -> <a href="./src/cloudflare/types/pages/project.py">Project</a></code>
- <code title="get /accounts/{account_id}/pages/projects/{project_name}">client.pages.projects.<a href="./src/cloudflare/resources/pages/projects/projects.py">get</a>(project_name, \*, account_id) -> <a href="./src/cloudflare/types/pages/project.py">Project</a></code>
- <code title="post /accounts/{account_id}/pages/projects/{project_name}/purge_build_cache">client.pages.projects.<a href="./src/cloudflare/resources/pages/projects/projects.py">purge_build_cache</a>(project_name, \*, account_id) -> object</code>

### Deployments

Methods:

- <code title="post /accounts/{account_id}/pages/projects/{project_name}/deployments">client.pages.projects.deployments.<a href="./src/cloudflare/resources/pages/projects/deployments/deployments.py">create</a>(project_name, \*, account_id, \*\*<a href="src/cloudflare/types/pages/projects/deployment_create_params.py">params</a>) -> <a href="./src/cloudflare/types/pages/deployment.py">Deployment</a></code>
- <code title="get /accounts/{account_id}/pages/projects/{project_name}/deployments">client.pages.projects.deployments.<a href="./src/cloudflare/resources/pages/projects/deployments/deployments.py">list</a>(project_name, \*, account_id, \*\*<a href="src/cloudflare/types/pages/projects/deployment_list_params.py">params</a>) -> <a href="./src/cloudflare/types/pages/deployment.py">SyncV4PagePaginationArray[Deployment]</a></code>
- <code title="delete /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}">client.pages.projects.deployments.<a href="./src/cloudflare/resources/pages/projects/deployments/deployments.py">delete</a>(deployment_id, \*, account_id, project_name, \*\*<a href="src/cloudflare/types/pages/projects/deployment_delete_params.py">params</a>) -> object</code>
- <code title="get /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}">client.pages.projects.deployments.<a href="./src/cloudflare/resources/pages/projects/deployments/deployments.py">get</a>(deployment_id, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/deployment.py">Deployment</a></code>
- <code title="post /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/retry">client.pages.projects.deployments.<a href="./src/cloudflare/resources/pages/projects/deployments/deployments.py">retry</a>(deployment_id, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/deployment.py">Deployment</a></code>
- <code title="post /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/rollback">client.pages.projects.deployments.<a href="./src/cloudflare/resources/pages/projects/deployments/deployments.py">rollback</a>(deployment_id, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/deployment.py">Deployment</a></code>

#### History

##### Logs

Types:

```python
from cloudflare.types.pages.projects.deployments.history import LogGetResponse
```

Methods:

- <code title="get /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/history/logs">client.pages.projects.deployments.history.logs.<a href="./src/cloudflare/resources/pages/projects/deployments/history/logs.py">get</a>(deployment_id, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/projects/deployments/history/log_get_response.py">LogGetResponse</a></code>

### Domains

Types:

```python
from cloudflare.types.pages.projects import (
    DomainCreateResponse,
    DomainListResponse,
    DomainEditResponse,
    DomainGetResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/pages/projects/{project_name}/domains">client.pages.projects.domains.<a href="./src/cloudflare/resources/pages/projects/domains.py">create</a>(project_name, \*, account_id, \*\*<a href="src/cloudflare/types/pages/projects/domain_create_params.py">params</a>) -> <a href="./src/cloudflare/types/pages/projects/domain_create_response.py">DomainCreateResponse</a></code>
- <code title="get /accounts/{account_id}/pages/projects/{project_name}/domains">client.pages.projects.domains.<a href="./src/cloudflare/resources/pages/projects/domains.py">list</a>(project_name, \*, account_id) -> <a href="./src/cloudflare/types/pages/projects/domain_list_response.py">SyncSinglePage[DomainListResponse]</a></code>
- <code title="delete /accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}">client.pages.projects.domains.<a href="./src/cloudflare/resources/pages/projects/domains.py">delete</a>(domain_name, \*, account_id, project_name) -> object</code>
- <code title="patch /accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}">client.pages.projects.domains.<a href="./src/cloudflare/resources/pages/projects/domains.py">edit</a>(domain_name, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/projects/domain_edit_response.py">DomainEditResponse</a></code>
- <code title="get /accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}">client.pages.projects.domains.<a href="./src/cloudflare/resources/pages/projects/domains.py">get</a>(domain_name, \*, account_id, project_name) -> <a href="./src/cloudflare/types/pages/projects/domain_get_response.py">DomainGetResponse</a></code>
