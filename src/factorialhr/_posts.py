import datetime
import typing
from collections.abc import Mapping

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class Comment(pydantic.BaseModel):
    """Model for posts_comment."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Identifier of the comment
    id: int = pydantic.Field(description='Identifier of the comment')
    #: Identifier of the post
    post_id: int = pydantic.Field(description='Identifier of the post')
    #: Author identifier refers to the employee access, you can get the employee from the employee endpoint
    author_id: int = pydantic.Field(
        description='Author identifier refers to the employee access, you can get the employee from the employee endpoint',  # noqa: E501
    )
    #: Text of the comment
    text: str = pydantic.Field(description='Text of the comment')
    #: Date of the comment
    created_at: datetime.datetime = pydantic.Field(description='Date of the comment')


class Group(pydantic.BaseModel):
    """Model for posts_group."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Identifier of the group
    id: int = pydantic.Field(description='Identifier of the group')
    #: Title of the group
    title: str = pydantic.Field(description='Title of the group')
    #: Description of the group
    description: str = pydantic.Field(description='Description of the group')
    #: Identifier of the company
    company_id: int = pydantic.Field(description='Identifier of the company')
    #: Whether the group is archived
    archived: bool | None = pydantic.Field(default=None, description='Whether the group is archived')
    #: Date when the group was created
    created_at: datetime.datetime | None = pydantic.Field(default=None, description='Date when the group was created')
    #: Date when the group was updated
    updated_at: datetime.datetime | None = pydantic.Field(default=None, description='Date when the group was updated')


class Post(pydantic.BaseModel):
    """Model for posts_post."""

    model_config = pydantic.ConfigDict(frozen=True)

    #: Identifier of the post
    id: int = pydantic.Field(description='Identifier of the post')
    #: Title of the post
    title: str = pydantic.Field(description='Title of the post')
    #: Description of the post
    description: str = pydantic.Field(description='Description of the post')
    #: Group identifier of the post
    post_group_id: int = pydantic.Field(description='Group identifier of the post')
    #: Allow comments and reactions on the post
    allow_comments_and_reactions: bool | None = pydantic.Field(
        default=None,
        description='Allow comments and reactions on the post',
    )
    #: Date when the post was published
    published_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when the post was published',
    )
    #: Date when the post was created
    created_at: datetime.datetime = pydantic.Field(description='Date when the post was created')
    #: Date when the post was updated
    updated_at: datetime.datetime = pydantic.Field(description='Date when the post was updated')
    #: Number of visits of the post
    visits_count: int | None = pydantic.Field(default=None, description='Number of visits of the post')
    #: URL of the cover image
    cover_image_url: str | None = pydantic.Field(default=None, description='URL of the cover image')
    #: Number of comments on the post
    comments_count: int | None = pydantic.Field(default=None, description='Number of comments on the post')
    #: Author identifier of the post
    author_id: int | None = pydantic.Field(default=None, description='Author identifier of the post')


class CommentsEndpoint(Endpoint):
    """Endpoint for posts/comments operations."""

    endpoint = 'posts/comments'

    async def all(self, **kwargs) -> ListApiResponse[Comment]:
        """Get all comments records.

        Official documentation: `posts/comments <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-posts-comments>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Comment]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Comment, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Comment]:
        """Get comments with pagination metadata.

        Official documentation: `posts/comments <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-posts-comments>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Comment]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Comment, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, comment_id: int | str, **kwargs) -> Comment:
        """Get a specific comment by ID.

        Official documentation: `posts/comments <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-posts-comments>`_

        :param comment_id: The unique identifier.
        :type comment_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Comment
        """
        data = await self.api.get(self.endpoint, comment_id, **kwargs)
        return pydantic.TypeAdapter(Comment).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Comment:
        """Create a new comment.

        Official documentation: `posts/comments <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-posts-comments>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Comment
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Comment).validate_python(response)

    async def update(self, comment_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Comment:
        """Update a comment.

        Official documentation: `posts/comments <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-posts-comments>`_

        :param comment_id: The unique identifier of the record to update.
        :type comment_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: Comment
        """
        response = await self.api.put(self.endpoint, comment_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Comment).validate_python(response)

    async def delete(self, comment_id: int | str, **kwargs) -> Comment:
        """Delete a comment.

        Official documentation: `posts/comments <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-posts-comments>`_

        :param comment_id: The unique identifier of the record to delete.
        :type comment_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: Comment
        """
        response = await self.api.delete(self.endpoint, comment_id, **kwargs)
        return pydantic.TypeAdapter(Comment).validate_python(response)


class GroupsEndpoint(Endpoint):
    """Endpoint for posts/groups operations."""

    endpoint = 'posts/groups'

    async def all(self, **kwargs) -> ListApiResponse[Group]:
        """Get all groups records.

        Official documentation: `posts/groups <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-posts-groups>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Group]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Group, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Group]:
        """Get groups with pagination metadata.

        Official documentation: `posts/groups <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-posts-groups>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Group]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Group, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, group_id: int | str, **kwargs) -> Group:
        """Get a specific group by ID.

        Official documentation: `posts/groups <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-posts-groups>`_

        :param group_id: The unique identifier.
        :type group_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Group
        """
        data = await self.api.get(self.endpoint, group_id, **kwargs)
        return pydantic.TypeAdapter(Group).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Group:
        """Create a new group.

        Official documentation: `posts/groups <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-posts-groups>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Group
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Group).validate_python(response)

    async def update(self, group_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Group:
        """Update a group.

        Official documentation: `posts/groups <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-posts-groups>`_

        :param group_id: The unique identifier of the record to update.
        :type group_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: Group
        """
        response = await self.api.put(self.endpoint, group_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Group).validate_python(response)

    async def delete(self, group_id: int | str, **kwargs) -> Group:
        """Delete a group.

        Official documentation: `posts/groups <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-posts-groups>`_

        :param group_id: The unique identifier of the record to delete.
        :type group_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: Group
        """
        response = await self.api.delete(self.endpoint, group_id, **kwargs)
        return pydantic.TypeAdapter(Group).validate_python(response)

    async def archive(self, data: Mapping[str, typing.Any], **kwargs) -> Group:
        """Archive a group.

        Official documentation: `posts/groups <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-posts-groups>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Result.
        :rtype: Group
        """
        response = await self.api.post(self.endpoint, 'archive', json=data, **kwargs)
        return pydantic.TypeAdapter(Group).validate_python(response)


class PostsEndpoint(Endpoint):
    """Endpoint for posts/posts operations."""

    endpoint = 'posts/posts'

    async def all(self, **kwargs) -> ListApiResponse[Post]:
        """Get all posts records.

        Official documentation: `posts/posts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-posts-posts>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing the list of records.
        :rtype: ListApiResponse[Post]
        """
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Post, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Post]:
        """Get posts with pagination metadata.

        Official documentation: `posts/posts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-posts-posts>`_

        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: Response containing records and pagination metadata.
        :rtype: MetaApiResponse[Post]
        """
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Post, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, post_id: int | str, **kwargs) -> Post:
        """Get a specific post by ID.

        Official documentation: `posts/posts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-posts-posts>`_

        :param post_id: The unique identifier.
        :type post_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The record.
        :rtype: Post
        """
        data = await self.api.get(self.endpoint, post_id, **kwargs)
        return pydantic.TypeAdapter(Post).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Post:
        """Create a new post.

        Official documentation: `posts/posts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-posts-posts>`_

        :param data: Payload for the new record (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The created record.
        :rtype: Post
        """
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Post).validate_python(response)

    async def update(self, post_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Post:
        """Update a post.

        Official documentation: `posts/posts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-posts-posts>`_

        :param post_id: The unique identifier of the record to update.
        :type post_id: int | str
        :param data: Payload with fields to update (key-value mapping).
        :type data: Mapping[str, typing.Any]
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The updated record.
        :rtype: Post
        """
        response = await self.api.put(self.endpoint, post_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Post).validate_python(response)

    async def delete(self, post_id: int | str, **kwargs) -> Post:
        """Delete a post.

        Official documentation: `posts/posts <https://apidoc.factorialhr.com/reference/get_api-2026-01-01-resources-posts-posts>`_

        :param post_id: The unique identifier of the record to delete.
        :type post_id: int | str
        :param kwargs: Optional keyword arguments (e.g. ``params`` for query string) forwarded to the HTTP request.
        :type kwargs: optional
        :raises httpx.HTTPStatusError: When the API returns an error status code.
        :return: The deleted record.
        :rtype: Post
        """
        response = await self.api.delete(self.endpoint, post_id, **kwargs)
        return pydantic.TypeAdapter(Post).validate_python(response)
