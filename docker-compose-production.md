# Create nginx.conf

```bash
cat > nginx.conf << 'EOF'
events {}
http {
    server {
        listen 80;
        location / {
            proxy_pass http://lease-notice-generator:5000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
    }
}
EOF
```


# Create docker-compose.yml

```bash
services:
  lease-notice-generator:
    image: zjxteusa/lease-notice-generator:latest
    container_name: lease-notice-app
    expose:
      - "5000"
    environment:
      - FLASK_ENV=production
    restart: unless-stopped

  nginx:
    image: nginx:alpine
    container_name: lease-notice-nginx
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - lease-notice-generator
    restart: unless-stopped

```