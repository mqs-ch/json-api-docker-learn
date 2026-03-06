import requests
from collections import Counter


def fetch_data(url, timeout=10):
    """Получить данные с API, вернуть список словарей."""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # выбросит исключение при HTTP ошибке
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе {url}: {e}")
        return []
    except requests.exceptions.Timeout:
        print(f"Превышен таймаут при запросе {url}: {e}")
        return []

def main():
    
    try:
        # Базовый URL
        base_url = "https://jsonplaceholder.typicode.com"

        # Загружаем данные
        print("1. Запрашиваю пользователей...")
        users = fetch_data(f"{base_url}/users")
        print("   Пользователи получены." if users else "   Ошибка или пусто.")

        print("2. Запрашиваю посты...")
        posts = fetch_data(f"{base_url}/posts")
        print("   Посты получены." if posts else "   Ошибка или пусто.")

        #print("3. Запрашиваю комментарии...")
        #comments = fetch_data(f"{base_url}/comments")
        #print("   Комментарии получены." if comments else "   Ошибка или пусто.")

    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем. Завершение.")
        return

    if not users or not posts: #or not comments:
        print("Не удалось загрузить все данные. Завершение.")
        return
    
    

    # --- Статистика ---

    # Сколько постов у каждого пользователя
    user_post_count = Counter(post['userId'] for post in posts)

    # Сколько комментариев у каждого поста
    #post_comment_count = Counter(comment['postId'] for comment in comments)

    # Общие показатели
    total_posts = len(posts)
    #total_comments = len(comments)
    total_users = len(users)

    # Среднее количество комментариев на пост
    #avg_comments_per_post = total_comments / total_posts if total_posts else 0

    # Посты без комментариев
    #posts_with_comments = set(post_comment_count.keys())
    #posts_without_comments = [post for post in posts if post['id'] not in posts_with_comments]
    #posts_without_comments_count = len(posts_without_comments)

    # --- Вывод результатов ---
    print("========== СТАТИСТИКА JSONPLACEHOLDER ==========")
    print(f"Всего пользователей: {total_users}")
    print(f"Всего постов: {total_posts}")
    #print(f"Всего комментариев: {total_comments}")
    #print(f"Среднее количество комментариев на пост: {avg_comments_per_post:.2f}")
    #print(f"Постов без комментариев: {posts_without_comments_count}")

    print("\n--- Топ-5 пользователей по количеству постов ---")
    # Свяжем userId с именем пользователя
    user_names = {user['id']: user['name'] for user in users}
    for user_id, count in user_post_count.most_common(5):
        name = user_names.get(user_id, f"User {user_id}")
        print(f"{name}: {count} постов")

    # Дополнительно: вывести детали по пользователям
    #print("\n--- Детализация по пользователям ---")
    #for user_id, count in sorted(user_post_count.items(), key=lambda x: x[1], reverse=True):
    #    name = user_names.get(user_id, f"User {user_id}")
    #    print(f"{name}: {count} постов, всего комментариев к его постам: {sum(post_comment_count[post['id']] for post in posts if post['userId'] == user_id)}")

if __name__ == "__main__":
    main()