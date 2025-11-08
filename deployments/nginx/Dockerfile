FROM nginx:latest

# Copie des certificats dans le conteneur
COPY nginx.conf /etc/nginx/nginx.conf
COPY certs/ /etc/nginx/certs/

EXPOSE 80
EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]

