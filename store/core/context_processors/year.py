from datetime import datetime


def get_current_year(request):
    """
    Добавляет переменную с текущим годом в подвал шаблона products.html.
    """
    return {
        'year': datetime.today().year
    }
