from django.contrib import admin

from products.admin import BasketAdmin

from .models import User, UserEmailVerification


@admin.register(User)  # Регистрируем вложенный BasketAdmin(admin.TabularInline): из products.admin,
# для отображения на странице пользователя модели корзины пользовате Можно применять если есть ForeignKey сязь
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (BasketAdmin,)
    extra = 0  # extra в дефолтном значении = 3, ставим на 0 так как нам не нужны дополнительные поля


@admin.register(UserEmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'expiration')
    fields = ('code', 'user', 'expiration', 'created')
    readonly_fields = ('created',)
