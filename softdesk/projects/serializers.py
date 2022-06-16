from projects.models import Comment, Contributor, Issue, Project
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    """
    Project Serializer
    """

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "type",
            "author",
        ]


class ContributorSerializer(serializers.ModelSerializer):
    """
    Contributor Serializer
    """

    class Meta:
        model = Contributor
        fields = [
            "user",
            "project",
            "permission",
            "role",
        ]


class IssueSerializer(serializers.ModelSerializer):
    """
    Issue Serializer
    """

    class Meta:
        model = Issue
        fields = [
            "id",
            "title",
            "description",
            "tag",
            "priority",
            "project",
            "status",
            "author",
            "assignee",
            "created_time",
        ]
        read_only_fields = [
            "id",
            "project",
            "author",
            "created_time",
        ]

class CommentSerializer(serializers.ModelSerializer):
    """
    Comment Serializer
    """

    class Meta:
        model = Comment
        fields = [
            "description",
            "author",
            "issue",
            "created_time",
        ]
