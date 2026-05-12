# AISecurity

Types:

```python
from cloudflare.types.ai_security import AISecurityUpdateResponse, AISecurityGetResponse
```

Methods:

- <code title="put /zones/{zone_id}/ai-security/settings">client.ai_security.<a href="./src/cloudflare/resources/ai_security/ai_security.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/ai_security/ai_security_update_params.py">params</a>) -> <a href="./src/cloudflare/types/ai_security/ai_security_update_response.py">AISecurityUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/ai-security/settings">client.ai_security.<a href="./src/cloudflare/resources/ai_security/ai_security.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/ai_security/ai_security_get_response.py">AISecurityGetResponse</a></code>

## CustomTopics

Types:

```python
from cloudflare.types.ai_security import CustomTopicUpdateResponse, CustomTopicGetResponse
```

Methods:

- <code title="put /zones/{zone_id}/ai-security/custom-topics">client.ai_security.custom_topics.<a href="./src/cloudflare/resources/ai_security/custom_topics.py">update</a>(\*, zone_id, \*\*<a href="src/cloudflare/types/ai_security/custom_topic_update_params.py">params</a>) -> <a href="./src/cloudflare/types/ai_security/custom_topic_update_response.py">CustomTopicUpdateResponse</a></code>
- <code title="get /zones/{zone_id}/ai-security/custom-topics">client.ai_security.custom_topics.<a href="./src/cloudflare/resources/ai_security/custom_topics.py">get</a>(\*, zone_id) -> <a href="./src/cloudflare/types/ai_security/custom_topic_get_response.py">CustomTopicGetResponse</a></code>
