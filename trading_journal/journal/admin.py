from django.contrib import admin
from .models import Trade


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = (
        "created_at",
        "exchange",
        "symbol",
        "side",
        "leverage",
        "entry_price",
        "status",
        "realized_pnl",
    )
    list_filter = ("exchange", "side", "status", "created_at")
    search_fields = ("symbol", "comment")
    date_hierarchy = "created_at"
