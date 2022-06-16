from projects.models import Comment, Contributor, Issue, Project
from rest_access_policy.access_policy import AccessPolicy


class ProjectAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["retrieve"],
            "principal": "authenticated",
            "condition": "has_access_to_project",
            "effect": "allow",
        },
        {
            "action": ["retrieve"],
            "principal": "authenticated",
            "condition": "is_project_owner",
            "effect": "allow",
        },
        {
            "action": ["update", "partial_update", "destroy"],
            "principal": "authenticated",
            "condition": "is_project_owner",
            "effect": "allow",
        },
        {
            "action": ["list", "create"],
            "principal": "authenticated",
            "effect": "allow",
        },
    ]

    def has_access_to_project(self, request, view, action):
        """
        Check if user in contributors of the project
        """
        obj = view.get_object()
        assert obj

        contributors_ids = Contributor.objects.filter(project=obj).values_list(
            "user", flat=True
        )
        return request.user.id in contributors_ids

    def is_project_owner(self, request, view, action):
        """
        Check if user is the project owner
        """
        obj = view.get_object()
        assert obj

        return obj.author == request.user


class ContributorAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": [
                "create",
                "update",
                "partial_update",
                "destroy",
                "retrieve",
                "list",
            ],
            "principal": "authenticated",
            "condition": "is_project_owner",
            "effect": "allow",
        },
    ]

    def is_project_owner(self, request, view, action):
        """
        Check if user is the project owner
        """
        obj = view.get_object()
        assert obj

        return obj.project.author == request.user


class IssueAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["create", "list", "retrieve"],
            "principal": "authenticated",
            "condition": "is_contributor",
            "effect": "allow",
        },
        {
            "action": ["create", "list", "retrieve"],
            "principal": "authenticated",
            "condition": "is_author_or_project_author",
            "effect": "allow",
        },
        {
            "action": ["update", "partial_update", "destroy"],
            "principal": "authenticated",
            "condition": "is_author_or_project_author",
            "effect": "allow",
        },
    ]

    def is_contributor(self, request, view, action):
        """
        Check if user is a contributor of the project
        """
        obj = view.get_object()
        assert obj

        contributors_ids = Contributor.objects.filter(project=obj.project).values_list(
            "user", flat=True
        )
        return request.user.id in contributors_ids

    def is_author_or_project_author(request, self, view, action):
        """
        Check if user is issue author or project author
        """
        obj = view.get_object()
        assert obj

        return request.user == (obj.author | obj.project.author)


class CommentAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["create", "list", "retrieve"],
            "principal": "authenticated",
            "condition": "is_contributor",
            "effect": "allow",
        },
        {
            "action": ["update", "partial_update", "destroy"],
            "principal": "authenticated",
            "condition": "is_author_or_project_author",
            "effect": "allow",
        },
    ]

    def is_contributor(self, request, view, action):
        """
        Check if user is a contributor of the project
        """
        obj = view.get_object()
        assert obj

        contributors_ids = Contributor.objects.filter(
            project=obj.issue.project
        ).values_list("user", flat=True)
        return request.user.id in contributors_ids

    def is_author_or_project_author(request, self, view, action):
        """
        Check if user is comment author or project author
        """
        obj = view.get_object()
        assert obj

        return request.user == (obj.author | obj.issue.project.author)
