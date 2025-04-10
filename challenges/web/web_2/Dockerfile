FROM node:18-alpine

WORKDIR /app
COPY . .

RUN npm install -g http-server

EXPOSE 8000
CMD ["http-server", "-a", "0.0.0.0", "-p", "8000"]
