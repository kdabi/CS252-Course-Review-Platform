from decimal import Decimal                                                                                                                                                                                         
import uuid
from django import template
from ..models import Rating, UserRating
from .. import app_settings

register = template.Library()

@register.inclusion_tag('star_ratings/avg_widget.html', takes_context=True)
def avg_ratings(context, item, icon_height=app_settings.STAR_RATINGS_STAR_HEIGHT, icon_width=app_settings.STAR_RATINGS_STAR_WIDTH, read_only=False):
    request = context.get('request')

    if request is None:
        raise Exception('Make sure you have "django.core.context_processors.request" in "TEMPLATE_CONTEXT_PROCESSORS"')

    rating = Rating.objects.for_instance(item)
    user = request.user.is_authenticated() and request.user or None

    if request.user.is_authenticated() or app_settings.STAR_RATINGS_ANONYMOUS:
        user_rating = UserRating.objects.for_instance_by_user(item, user=user)
    else:
        user_rating = None

    stars = [i for i in range(1, app_settings.STAR_RATINGS_RANGE + 1)]#range(1, int(rating.average)+1)]#app_settings.STAR_RATINGS_RANGE + 1)]
    avg_star = [i for i in range(1, int(rating.average)+1)]#app_settings.STAR_RATINGS_RANGE + 1)]

    return {
        'rating': rating,
        'request': request,
        'user': request.user,
        'user_rating': user_rating,
        'stars': stars,#list[int(rating.average)],
        'star_count': avg_star,#app_settings.STAR_RATINGS_RANGE,
        'percentage': 100 * (rating.average / Decimal(app_settings.STAR_RATINGS_RANGE)),
        'icon_height': icon_height,
        'icon_width': icon_width,
        'id': 'dsr{}'.format(uuid.uuid4().hex),
        'anonymous_ratings': app_settings.STAR_RATINGS_ANONYMOUS,
        'read_only': read_only,
        'editable': not read_only and (request.user.is_authenticated() or app_settings.STAR_RATINGS_ANONYMOUS)
    }
