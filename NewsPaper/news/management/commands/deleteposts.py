from django.core.management.base import BaseCommand, CommandError
from ...models import Post, Category


class Command(BaseCommand):
    help = 'Команда deleteposts удаляет все посты из выбранной категории.'
    requires_migrations_checks = True

    def handle(self, *args, **options):
        self.stdout.readable()
        self.stdout.write('Введите название категории, из которой нужно удалить все посты')
        cats = [x.cat_name for x in Category.objects.all()]
        self.stdout.write(f'Имеющиеся категории: {cats}')
        answer = input('Категория: ')
        try:
            Category.objects.get(cat_name=answer)
            Post.objects.filter(post_to_category_rel__cat_name=answer).delete()
            self.stdout.write(f'Все посты из категории {answer} удалены.')
        except Category.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Не найдена категория {answer}'))
