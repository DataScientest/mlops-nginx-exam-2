start-project:
	@echo "Starting all services..."
	docker compose up -d
	@echo "Services started. Grafana UI: http://localhost:3000"

stop-project:
	@echo "Stopping all services..."
	docker compose down
	@echo "Services stopped."

test:
	@echo "Testing API v1..."
	curl -k -X POST "https://localhost:443/api/v1/predict" \
		-H "Content-Type: application/json" \
		-d '{"sentence": "Oh yeah, that was soooo cool!"}' \
		--user admin:admin \
		--cacert ./deployments/nginx/certs/nginx.crt
	@echo ""
	@echo "Testing API v2..."
	curl -k -X POST "https://localhost:443/api/v2/predict" \
		-H "Content-Type: application/json" \
		-d '{"sentence": "Oh yeah, that was soooo cool!"}' \
		--user admin:admin \
		--cacert ./deployments/nginx/certs/nginx.crt
