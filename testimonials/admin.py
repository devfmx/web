"""Admin module for Testimonials."""

from django.contrib import admin

from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    """Testimonial Model Admin."""

    list_display = (
        'id',
        'person',
        'person_title',
        'testimonial',
        'ViewPicture'
    )
