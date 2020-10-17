from django.db import models
from django.contrib.auth import get_user_model


class Ticket(models.Model):
    """A ticket is a request or issue that requires work."""
    subject = models.TextField()
    requester = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='requester')
    assignee = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='assignee')


class Comment(models.Model):
    """A comment can be made on a ticket to log work, notify the requester, etc. A comment can be private or public."""
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    body = models.TextField()

    # If a comment is private, it should only be visible to agents and admins.
    private = models.BooleanField(default=False)
