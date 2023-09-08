from django.contrib import admin

from .models import Auction, Category, Bid, User, Comment

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display =('username',)



class AuctionAdmin(admin.ModelAdmin):
    list_display = ('owner','title', 'description', 'wanted','date_start','date_end','category')
    list_display_links = ('title', 'description')
    search_fields = ('title', 'wanted','description', 'category')



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('auction','user','text','date')


admin.site.register(Auction, AuctionAdmin)
admin.site.register(Bid)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(User, UserAdmin)
