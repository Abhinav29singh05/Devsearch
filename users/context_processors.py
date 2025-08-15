from .models import Message

def unread_message_count(request):
    if request.user.is_authenticated:
        unread_count = Message.objects.filter(
            recipient=request.user.profile, is_read=False
        ).count()
    else:
        unread_count = 0
    return {'unread_message_count': unread_count}
