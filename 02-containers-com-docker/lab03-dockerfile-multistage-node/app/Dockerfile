# Stage 1 (builder)
FROM node:18 AS builder
WORKDIR /app

COPY package.json ./
RUN npm install

COPY . .

# Stage 2 (runtime enxuto)
FROM node:18-alpine
WORKDIR /app

ENV NODE_ENV=production

# copiar só o que precisa do builder
COPY --from=builder /app /app

EXPOSE 3000
CMD ["npm", "start"]
