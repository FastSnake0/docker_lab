# ДЗ 4

Задание 4 - создание деплоя для сервися

1. Создание кластера

    `k3d cluster create my-cluster --port "30001:30001@loadbalancer"`

2. Импорт образов в кластер

    `k3d image import dz4-frontend:latest -c test-cluster`
    `k3d image import dz4-backend:latest -c test-cluster`
3. Манифесты
    `kubectl apply -f k8s/`

4. Перезапуск

    `kubectl rollout restart deployment backend`
    `kubectl rollout restart deployment frontend`

Задание 5 - создание ингресса

Добавил `ingress.yaml` и обновил конфиги `kubectl apply -f k8s/`
