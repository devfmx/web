"""Admin module for Testimonials."""

from django.contrib import admin

from .models import Testimonial, Press


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

@admin.register(Press)
class PressAdmin(admin.ModelAdmin):

    """Press Model Admin."""

    list_display = (
        'id',
        'press_name',
        'link',
        'showImage',
    )
