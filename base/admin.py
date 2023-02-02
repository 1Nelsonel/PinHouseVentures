from django.contrib import admin
from .models import Agent,Location,Property,Propertycategory,Blog,Comment,Profile,PropertyComment,MessageAgent
# ,AgentMessage
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import User

admin.site.register(Agent),
admin.site.register(Location),
admin.site.register(Property),
admin.site.register(Propertycategory)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(PropertyComment)
admin.site.register(MessageAgent)

class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False

class AccountsUserAdmin(AuthUserAdmin):
    def add_view(self, *args, **kwargs):
        self.inlines =[]
        return super(AccountsUserAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.inlines =[ProfileInLine]
        return super(AccountsUserAdmin, self).change_view(*args, **kwargs)
    # inlines = [ProfileInLine]

admin.site.unregister(User)
admin.site.register(User, AccountsUserAdmin)