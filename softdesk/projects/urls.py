from django.urls import include, path
from projects.views import (CommentViewSet, ContributorViewSet, IssueViewSet,
                            ProjectViewSet)
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register(r"projects", ProjectViewSet, basename="projects")

contributors_router = routers.NestedSimpleRouter(router, r"projects", lookup="project")
contributors_router.register(
    r"users", ContributorViewSet, basename="project-contributors"
)

issues_router = routers.NestedSimpleRouter(router, r"projects", lookup="project")
issues_router.register(r"issues", IssueViewSet, basename="project-issues")

comments_router = routers.NestedSimpleRouter(issues_router, r"issues", lookup="issue")
comments_router.register(r"comments", CommentViewSet, basename="project-issue-comments")

urlpatterns = [
    path(r"", include(router.urls)),
    path(r"", include(contributors_router.urls)),
    path(r"", include(issues_router.urls)),
    path(r"", include(comments_router.urls)),
]

print(issues_router.urls)