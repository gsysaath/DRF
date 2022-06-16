from django.db import models
from rest_framework.permissions import BasePermission
from users.models import User


class Project(models.Model):
    class ProjectType(models.TextChoices):
        BACKEND = ("back-end", "back-end")
        FRONTEND = ("front-end", "front-end")
        IOS = ("ios", "iOS")
        ANDROID = ("android", "Android")

    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    type = models.CharField(
        max_length=255, null=False, blank=False, choices=ProjectType.choices
    )
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)


class Contributor(models.Model):
    class ContributorPermission(models.TextChoices):
        AUTHOR = ("author", "Author")
        NOT_AUTHOR = ("not_author", "Not Author")

    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    project = models.ForeignKey(
        Project, null=False, blank=False, on_delete=models.CASCADE
    )
    permission = models.CharField(
        max_length=255, null=False, blank=False, choices=ContributorPermission.choices
    )
    role = models.CharField(
        max_length=255, null=False, blank=False, default="initial_role"
    )


class Issue(models.Model):
    class IssueStatus(models.TextChoices):
        ON_GOING = ("ON_GOING", "On going")
        FINISHED = ("FINISHED", "Finished")

    class IssuePriority(models.TextChoices):
        LOW = ("LOW", "Low")
        MEDIUM = ("MEDIUM", "Medium")
        HIGH = ("HIGH", "High")

    class IssueTag(models.TextChoices):
        BUG = ("BUG", "BUG")
        TASK = ("TASK", "Task")
        IMPROVEMENT = ("IMPROVEMENT", "Improvement")

    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=True)
    tag = models.CharField(
        max_length=255, null=False, blank=False, choices=IssueTag.choices
    )
    priority = models.CharField(
        max_length=255, null=False, blank=False, choices=IssuePriority.choices
    )
    project = models.ForeignKey(
        Project, null=False, blank=False, on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=255, null=False, blank=False, choices=IssueStatus.choices
    )
    author = models.ForeignKey(
        User,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="comment_author",
    )
    assignee = models.ForeignKey(
        User,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="issue_assignee",
    )
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.CharField(max_length=255, null=False, blank=True)
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, null=False, blank=False, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    # Issues : elle stocke tous les problèmes d'un projet, a
    # insi que leurs statut, priorité, attri
    # butaire (utilisateur auquel le problème est affecté),
    # balise (bug, tâche, amélioration), et d'autres détails
    #  nécessaires mentionnés dans la table. Elle a une relation plusieu
    # rs-à-un avec la table Projects, et une autre relation plusieurs-à
    # -un avec la table Users.
