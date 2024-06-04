# Pitwall Card Data API

This is a Django REST Framework project for storing and validating card data. The API allows users to create, retrieve, and list card entries while ensuring that users can only access their own data. It also includes validation for card numbers and CCVs.

## Features

- **User Authentication**: Only authenticated users can access the API.
- **Card Validation**: Validates card numbers and CCVs before storing them.
- **User-specific Data**: Users can only see and manage their own card data.
- **Browsable API**: Easy-to-use interface for testing endpoints in the browser.
- **Performance Testing**: Includes tests to ensure validation speed is within acceptable limits.

## API Endpoints

- **Create Card**: `POST /cards/`
- **List Cards**: `GET /cards/`

## Admin User Credentials

- username: admin
- Password: admin
