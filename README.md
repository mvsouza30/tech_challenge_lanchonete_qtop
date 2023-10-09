# tech_challenge_lanchonete_qtop

Como iniciar o sistema:
DB

aplicar o secrets:
kubectl apply -f qtop-secret.yaml

executar o deployment do banco de dados:
kubectl apply -f qtop-db-api.yaml

executar o service do banco de dados:
kubectl apply -f svc-db-qtop.yaml

executar o hpa do banco de dados:
kubectl apply -f db-hpa.yaml


APP
executar o deployment do app:
kubectl apply -f qtop-app-api.yamll

executar o service do app:
kubectl apply -f svc-app-qtop.yaml

executar o hpa do app:
kubectl apply -f app-hpa.yaml
