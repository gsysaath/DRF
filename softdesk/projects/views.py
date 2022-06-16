from projects.models import Comment, Contributor, Issue, Project
from projects.permissions import (CommentAccessPolicy, ContributorAccessPolicy,
                                  IssueAccessPolicy, ProjectAccessPolicy)
from projects.serializers import (CommentSerializer, ContributorSerializer,
                                  IssueSerializer, ProjectSerializer)
from rest_access_policy.access_view_set_mixin import AccessViewSetMixin
from rest_framework.viewsets import ModelViewSet


class ProjectViewSet(AccessViewSetMixin, ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    access_policy = ProjectAccessPolicy


class ContributorViewSet(AccessViewSetMixin, ModelViewSet):
    serializer_class = ContributorSerializer
    access_policy = ContributorAccessPolicy

    def get_queryset(self):
        return Contributor.objects.filter(project=self.kwargs["project_pk"])


class IssueViewSet(AccessViewSetMixin, ModelViewSet):
    serializer_class = IssueSerializer
    access_policy = IssueAccessPolicy

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs["project_pk"])


class CommentViewSet(AccessViewSetMixin, ModelViewSet):
    serializer_class = CommentSerializer
    access_policy = CommentAccessPolicy

    def get_queryset(self):
        return Comment.objects.filter(
            issue=self.kwargs["issue_pk"],
            issue__project=self.kwargs["project_pk"],
        )
