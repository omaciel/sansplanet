from django.db import models
from django.conf import settings

# Social Networks
TWITTER = 'twitter'
IDENTICA = 'identi.ca'

SOCIAL_NETWORKS_NAMES = (
    (TWITTER, 'Twitter'),
    (IDENTICA, 'Identi.ca'),
)

SOCIAL_NETWORKS_URLS = {
    TWITTER: 'http://twitter.com/',
    IDENTICA: 'http://identi.ca/',
}

class SocialNetwork(models.Model):
    network_name = models.CharField(
        "Network Name", max_length=50, choices=SOCIAL_NETWORKS_NAMES
    )

    user_name = models.CharField(
        "User Name", max_length=50, null=False, blank=False
    )

    url = models.URLField(
        "Network URL", null=True, blank=True
    )

    icon = models.ImageField(
        "Network Icon", null=True, blank=True, upload_to='icons'
    )

    def __unicode__(self):
        return self.url

    def save(self):
        self.url = SOCIAL_NETWORKS_URLS[self.network_name] + self.user_name
        super(SocialNetwork, self).save()

class Author(models.Model):
    author_name = models.CharField(
        "Author Name", max_length=50, blank=True
    )

    author_email = models.EmailField(
        "Email", blank=True
    )

    biography = models.TextField(
        "Short biography about the author.", null=True, blank=True
    )

    gotchi = models.ImageField(
        "Avatar",
        null=True, blank=True, upload_to=settings.AVATAR_LOCATION,
        help_text="URL to an image file (.jpg, .png, ...) of a hackergotchi"
    )

    network = models.ManyToManyField(
        SocialNetwork, null=True, blank=True
    )

    def __unicode__(self):
        return self.author_name

    class Meta:
        ordering = ('-author_name',)

class Feed(models.Model):
    author = models.ForeignKey(
        Author, null=False, blank=False
    )

    feed_title = models.CharField(
        "Feed Title", max_length=200, blank=True
    )

    site_url = models.URLField(
        "Site URL", blank=True, help_text="URL for the web site"
    )

    feed_url = models.URLField(
        "Feed URL", unique=True, help_text="URL for the news feed"
    )

    is_active = models.BooleanField(
        default=True, help_text="If disabled, this feed will not longer be updated."
    )

    # http://feedparser.org/docs/http-etag.html
    etag = models.CharField(max_length=50, blank=True)
    last_modified = models.DateTimeField(null=True, blank=True)
    last_checked = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'feed'
        verbose_name_plural = 'feeds'
        ordering = ('-author', '-feed_title',)

    def __unicode__(self):
        return u'%s (%s)' % (self.feed_title, self.author.author_name)

    def save(self):
        super(Feed, self).save()

class Post(models.Model):
    feed = models.ForeignKey(
        Feed, verbose_name='feed', null=False, blank=False
    )

    title = models.CharField(
        "Title", max_length=255
    )

    link = models.URLField("Link")

    content = models.TextField(
        "Content", blank=True
    )

    date_created = models.DateTimeField(
        "Date Created", null=True, blank=True
    )

    date_modified = models.DateTimeField(
        "Date Modified", null=True, blank=True
    )

    guid = models.CharField(
        "GUID", max_length=200, db_index=True
    )

    comments = models.URLField(
        "Comments", blank=True
    )

    is_visible = models.BooleanField(
        default=True, help_text="Should this post be visible?"
    )

    #tags = models.ManyToManyField(Tag, verbose_name=_('tags'))

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ('-date_modified',)
        unique_together = (('feed', 'guid'),)

    def __unicode__(self):
        return self.title

    def save(self):
        super(Post, self).save()

    def get_absolute_url(self):
        return self.link
