from django.contrib import admin

# Register your models here.
from core.models import *


class SectionTranslationInline(admin.TabularInline):
    model = SectionTranslation
    raw_id_fields = ("section",)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    inlines = [
        SectionTranslationInline,
    ]


class SubsectionTranslationInline(admin.TabularInline):
    model = SubsectionTranslation
    raw_id_fields = ("subsection",)


@admin.register(Subsection)
class SubsectionAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    inlines = [
        SubsectionTranslationInline,
    ]


class WordTranslationInline(admin.TabularInline):
    model = WordTranslation
    raw_id_fields = ("word",)


class CloseSenseWordInline(admin.TabularInline):
    model = CloseSenseWord
    raw_id_fields = ("word",)
    fk_name = "word"


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    inlines = [
        WordTranslationInline,
        CloseSenseWordInline,
    ]
