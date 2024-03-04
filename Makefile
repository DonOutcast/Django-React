.PHONY: build
build:
	@docker-compose up --build

.PHONY: makemigrations
makemigrations: ## Make migrations
	@docker-compose exec backend ./manage.py makemigrations

.PHONY: migrate
migrate:
	@docker-compose exec backend ./manage.py migrate

.PHONY: create_supser_user
create_super_user:
	@docker-compose exec backend ./manage.py create_super_user
.PHONY: stop
stop:
	@docker-compose stop

.PHONY: run
run: build makemigrations migrate create_super_user
