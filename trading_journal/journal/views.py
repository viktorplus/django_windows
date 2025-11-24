from django.shortcuts import render
from django.db.models import Sum, Count
from .models import Trade


def trades_list(request):
    trades = Trade.objects.all()

    # Закрытые сделки (там, где PnL уже посчитан)
    closed = trades.exclude(realized_pnl__isnull=True)

    total_trades = trades.count()
    total_closed = closed.count()
    total_open = trades.filter(status="OPEN").count()

    wins = closed.filter(realized_pnl__gt=0)
    losses = closed.filter(realized_pnl__lt=0)
    breakevens = closed.filter(realized_pnl=0)

    pnl_sum = closed.aggregate(s=Sum("realized_pnl"))["s"] or 0
    avg_pnl = pnl_sum / total_closed if total_closed > 0 else 0

    win_count = wins.count()
    loss_count = losses.count()

    winrate = (win_count / total_closed * 100) if total_closed > 0 else 0

    best_trade = closed.order_by("-realized_pnl").first()
    worst_trade = closed.order_by("realized_pnl").first()

    # PnL по направлению (LONG / SHORT)
    pnl_by_side = (
        closed
        .values("side")
        .annotate(
            total_pnl=Sum("realized_pnl"),
            count=Count("id"),
        )
        .order_by("side")
    )

    stats = {
        "total_trades": total_trades,
        "total_closed": total_closed,
        "total_open": total_open,
        "wins": win_count,
        "losses": loss_count,
        "breakevens": breakevens.count(),
        "pnl_sum": pnl_sum,
        "avg_pnl": avg_pnl,
        "winrate": winrate,
        "best_trade": best_trade,
        "worst_trade": worst_trade,
        "pnl_by_side": list(pnl_by_side),
    }

    context = {
        "trades": trades,
        "stats": stats,
    }
    return render(request, "trades_list.html", context)
