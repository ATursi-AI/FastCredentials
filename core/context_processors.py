from .models import Course

def global_course_list(request):
    return {
        'all_courses': Course.objects.all().order_by('title')
    }
