import datetime
import typing
from collections.abc import Mapping

import pydantic

from factorialhr._client import Endpoint, ListApiResponse, MetaApiResponse


class Comment(pydantic.BaseModel):
    """Model for posts_comment."""

    id: int = pydantic.Field(description='Identifier of the comment')
    post_id: int = pydantic.Field(description='Identifier of the post')
    author_id: int = pydantic.Field(
        description='Author identifier refers to the employee access, you can get the employee from the employee endpoint',  # noqa: E501
    )
    text: str = pydantic.Field(description='Text of the comment')
    created_at: datetime.datetime = pydantic.Field(description='Date of the comment')


class Group(pydantic.BaseModel):
    """Model for posts_group."""

    id: int = pydantic.Field(description='Identifier of the group')
    title: str = pydantic.Field(description='Title of the group')
    description: str = pydantic.Field(description='Description of the group')
    company_id: int = pydantic.Field(description='Identifier of the company')
    archived: bool | None = pydantic.Field(default=None, description='Whether the group is archived')
    created_at: datetime.datetime | None = pydantic.Field(default=None, description='Date when the group was created')
    updated_at: datetime.datetime | None = pydantic.Field(default=None, description='Date when the group was updated')


class Post(pydantic.BaseModel):
    """Model for posts_post."""

    id: int = pydantic.Field(description='Identifier of the post')
    title: str = pydantic.Field(description='Title of the post')
    description: str = pydantic.Field(description='Description of the post')
    post_group_id: int = pydantic.Field(description='Group identifier of the post')
    allow_comments_and_reactions: bool | None = pydantic.Field(
        default=None,
        description='Allow comments and reactions on the post',
    )
    published_at: datetime.datetime | None = pydantic.Field(
        default=None,
        description='Date when the post was published',
    )
    created_at: datetime.datetime = pydantic.Field(description='Date when the post was created')
    updated_at: datetime.datetime = pydantic.Field(description='Date when the post was updated')
    visits_count: int | None = pydantic.Field(default=None, description='Number of visits of the post')
    cover_image_url: str | None = pydantic.Field(default=None, description='URL of the cover image')
    comments_count: int | None = pydantic.Field(default=None, description='Number of comments on the post')
    author_id: int | None = pydantic.Field(default=None, description='Author identifier of the post')


class CommentsEndpoint(Endpoint):
    """Endpoint for posts/comments operations."""

    endpoint = 'posts/comments'

    async def all(self, **kwargs) -> ListApiResponse[Comment]:
        """Get all comments records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Comment, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Comment]:
        """Get comments with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Comment, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, comment_id: int | str, **kwargs) -> Comment:
        """Get a specific comment by ID."""
        data = await self.api.get(self.endpoint, comment_id, **kwargs)
        return pydantic.TypeAdapter(Comment).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Comment:
        """Create a new comment."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Comment).validate_python(response)

    async def update(self, comment_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Comment:
        """Update a comment."""
        response = await self.api.put(self.endpoint, comment_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Comment).validate_python(response)

    async def delete(self, comment_id: int | str, **kwargs) -> Comment:
        """Delete a comment."""
        response = await self.api.delete(self.endpoint, comment_id, **kwargs)
        return pydantic.TypeAdapter(Comment).validate_python(response)


class GroupsEndpoint(Endpoint):
    """Endpoint for posts/groups operations."""

    endpoint = 'posts/groups'

    async def all(self, **kwargs) -> ListApiResponse[Group]:
        """Get all groups records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Group, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Group]:
        """Get groups with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Group, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, group_id: int | str, **kwargs) -> Group:
        """Get a specific group by ID."""
        data = await self.api.get(self.endpoint, group_id, **kwargs)
        return pydantic.TypeAdapter(Group).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Group:
        """Create a new group."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Group).validate_python(response)

    async def update(self, group_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Group:
        """Update a group."""
        response = await self.api.put(self.endpoint, group_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Group).validate_python(response)

    async def delete(self, group_id: int | str, **kwargs) -> Group:
        """Delete a group."""
        response = await self.api.delete(self.endpoint, group_id, **kwargs)
        return pydantic.TypeAdapter(Group).validate_python(response)

    async def archive(self, data: Mapping[str, typing.Any], **kwargs) -> Group:
        """Archive a group."""
        response = await self.api.post(self.endpoint, 'archive', json=data, **kwargs)
        return pydantic.TypeAdapter(Group).validate_python(response)


class PostsEndpoint(Endpoint):
    """Endpoint for posts/posts operations."""

    endpoint = 'posts/posts'

    async def all(self, **kwargs) -> ListApiResponse[Post]:
        """Get all posts records."""
        data = await self.api.get_all(self.endpoint, **kwargs)
        return ListApiResponse(model_type=Post, raw_data=data)

    async def get(self, **kwargs) -> MetaApiResponse[Post]:
        """Get posts with pagination metadata."""
        query_params = kwargs.pop('params', {})
        query_params.setdefault('page', 1)
        response = await self.api.get(self.endpoint, params=query_params, **kwargs)
        return MetaApiResponse(model_type=Post, raw_meta=response['meta'], raw_data=response['data'])

    async def get_by_id(self, post_id: int | str, **kwargs) -> Post:
        """Get a specific post by ID."""
        data = await self.api.get(self.endpoint, post_id, **kwargs)
        return pydantic.TypeAdapter(Post).validate_python(data)

    async def create(self, data: Mapping[str, typing.Any], **kwargs) -> Post:
        """Create a new post."""
        response = await self.api.post(self.endpoint, json=data, **kwargs)
        return pydantic.TypeAdapter(Post).validate_python(response)

    async def update(self, post_id: int | str, data: Mapping[str, typing.Any], **kwargs) -> Post:
        """Update a post."""
        response = await self.api.put(self.endpoint, post_id, json=data, **kwargs)
        return pydantic.TypeAdapter(Post).validate_python(response)

    async def delete(self, post_id: int | str, **kwargs) -> Post:
        """Delete a post."""
        response = await self.api.delete(self.endpoint, post_id, **kwargs)
        return pydantic.TypeAdapter(Post).validate_python(response)
