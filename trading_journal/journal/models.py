from django.db import models


class Trade(models.Model):
    SIDE_CHOICES = [
        ("LONG", "Long"),
        ("SHORT", "Short"),
    ]

    STATUS_CHOICES = [
        ("OPEN", "Открыта"),
        ("CLOSED", "Закрыта"),
    ]

    exchange = models.CharField(
        max_length=50,
        default="Binance",
        verbose_name="Биржа",
    )
    symbol = models.CharField(
        max_length=20,
        verbose_name="Пара (например, BTCUSDT)",
    )
    side = models.CharField(
        max_length=5,
        choices=SIDE_CHOICES,
        verbose_name="Направление",
    )
    leverage = models.PositiveIntegerField(
        default=1,
        verbose_name="Плечо",
    )
    quantity = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        verbose_name="Объём (контракты/монеты)",
    )
    entry_price = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        verbose_name="Цена входа",
    )
    stop_loss = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        null=True,
        blank=True,
        verbose_name="Stop-loss",
    )
    take_profit_1 = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        null=True,
        blank=True,
        verbose_name="TP1",
    )
    take_profit_2 = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        null=True,
        blank=True,
        verbose_name="TP2",
    )
    take_profit_3 = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        null=True,
        blank=True,
        verbose_name="TP3",
    )

    status = models.CharField(
        max_length=6,
        choices=STATUS_CHOICES,
        default="OPEN",
        verbose_name="Статус",
    )
    realized_pnl = models.DecimalField(
        max_digits=20,
        decimal_places=4,
        null=True,
        blank=True,
        verbose_name="Результат (USDT)",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Создано",
    )
    closed_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Закрыто",
    )

    comment = models.TextField(
        blank=True,
        verbose_name="Комментарий",
    )

    def __str__(self):
        return f"{self.symbol} {self.side} @ {self.entry_price}"

    class Meta:
        verbose_name = "Сделка"
        verbose_name_plural = "Сделки"
        ordering = ["-created_at"]
