# Payments Service API

**Version:** 1.0.0

API for creating, retrieving, and managing payment transactions.

## Base URL

`https://api.example.dev/v1`

---

# Endpoints

## GET /payments

**Summary:** List payments

**Description:** Returns a list of payment transactions.

### Responses

- **200** — Payments retrieved successfully.


---

## POST /payments

**Summary:** Create payment

**Description:** Creates a new payment transaction.

### Request Body

Request body required.

### Responses

- **201** — Payment created successfully.
- **400** — Invalid request payload.


---

## GET /payments/{paymentId}

**Summary:** Retrieve payment

**Description:** Returns details for a specific payment.

### Parameters

- **paymentId** (path)


### Responses

- **200** — Payment retrieved successfully.
- **404** — Payment not found.


---
