from django.contrib import admin
from .models import Course, Question, Certificate, Lesson, Payment
from .models import BlogPost

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    # Explicitly showing fields helps ensure the new dropdown appears in the Course view too
    fields = ('text', 'option_1', 'option_2', 'option_3', 'option_4', 'correct_option', 'related_lesson')

class QuestionAdmin(admin.ModelAdmin):
    # NEW: This allows you to audit your questions quickly
    list_display = ('text', 'course', 'related_lesson')
    list_filter = ('course',)
    search_fields = ('text',)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'category', 'duration_minutes')
    list_editable = ('priority', 'category') # Allows quick editing without opening the record
    inlines = [LessonInline, QuestionInline]

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('cert_id', 'user', 'course', 'issued_at')
    readonly_fields = ('cert_id', 'issued_at')
    search_fields = ('user__username', 'cert_id')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'amount', 'date', 'stripe_charge_id')
    list_filter = ('date', 'course')
    search_fields = ('user__username', 'stripe_charge_id')
    readonly_fields = ('date',)

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published', 'created_at']
    list_editable = ['published']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']

# Register your models
admin.site.register(Course, CourseAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Question, QuestionAdmin) # Updated to use the custom class
admin.site.register(Lesson)
admin.site.register(BlogPost, BlogPostAdmin)