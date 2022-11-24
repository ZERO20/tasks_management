# Endpoints Doc


## Users
Api users
___
### Create ###
- **URL:** `/users/api/v1/users/`
- **Method:** `POST`
- **Code:** `201`
- **Body request:**
    ```json
    {
        "first_name": "Julio",
        "last_name": "Morales",
        "email": "julio@email.com",
        "username": "julio",
        "password": "Julio1234$"
    }
    ```
- **Response:**
    ```json
    {
        "id": 2,
        "first_name": "Julio",
        "last_name": "Morales",
        "email": "julio@email.com",
        "username": "julio"
    }
    ```

### Get access JWT ###
- **URL:** `/users/api/v1/token/request/`
- **Method:** `POST`
- **Code:** `200`
- **Body request:**
    ```json
    {
        "username": "julio",
        "password": "Julio1234$"
    }
    ```
- **Response:**
    ```json
    {
        "refresh": "eyJhbGciOiJIUzI1NiI....", // refresh token
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpX...." // access token
    }
    ```

### Refresh access JWT ###
- **URL:** `/users/api/v1/token/refresh/`
- **Method:** `POST`
- **Code:** `200`
- **Body request:**
    ```json
    {
        "refresh": "eyJhbGciOiJIUzI1NiI..." // refresh token
    }
    ```
- **Response:**
    ```json
    {
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ..."
    }
    ```

## Tasks
Api tasks

### Create ###
- **URL:** `/tasks/api/v1/tasks/`
- **Method:** `POST`
- **Code:** `201`
- **Headers :**
    ```
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiIsIn...'
    ```
- **Body request:**
    ```json
    {
        "name": "Task 1",
        "description": "Task #1",
        "status": "complete" // optional, by default is incomplete
    }
    ```
- **Response:**
    ```json
    {
        "id": 1,
        "name": "Task 1",
        "description": "Task #1",
        "status": "incomplete",
        "created_at": "2022-11-24T19:54:32.562623Z"
    }
    ```

### List ###
- **URL:** `/tasks/api/v1/tasks/`
- **Method:** `GET`
- **Code:** `200`
- **Headers :**
    ```
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiIsIn...'
    ```
- **Query params:**
    - name: search by name
    - description: search by name
    - size: page size
    - page: page number
- **Response:**
    ```json
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "name": "Task 1",
                "description": "Task #1",
                "status": "incomplete",
                "created_at": "2022-11-24T19:54:32.562623Z"
            }
        ]
    }
    ```
- **By default the page size is 25**

### Update ###
- **URL:** `/tasks/api/v1/tasks/{id}/`
- **Method:** `PUT`
- **Code:** `200`
- **Headers :**
    ```
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiIsIn...'
    ```
- **Body request:**
    ```json
    {
        "name": "Task #1",
        "description": "This is the task #1"
        "status": "complete" // optional, by default is incomplete
    }
    ```
- **Response:**
    ```json
    {
        "id": 1,
        "name": "Task #1",
        "description": "This is the task #1",
        "status": "incomplete",
        "created_at": "2022-11-24T19:54:32.562623Z"
    }
    ```

### Change status ###
- **URL:** `/tasks/api/v1/tasks/{id}/update/status/`
- **Method:** `PUT`
- **Code:** `200`
- **Headers :**
    ```
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiIsIn...'
    ```
- **Body request:**
    ```json
    {
        "status": "complete"
    }
    ```
- **Response:**
    ```json
    {
        "id": 1,
        "name": "Task #1",
        "description": "This is the task #1",
        "status": "complete",
        "created_at": "2022-11-24T19:54:32.562623Z"
    }
    ```

### Partial update ###
- **URL:** `/tasks/api/v1/tasks/{id}/`
- **Method:** `PATCH`
- **Code:** `200`
- **Headers :**
    ```
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiIsIn...'
    ```
- **Body request:**
    ```json
    {
        "name": "Task 1" // name, description, status
    }
    ```
- **Response:**
    ```json
    {
        "id": 1,
        "name": "Task 1",
        "description": "This is the task #1",
        "status": "complete",
        "created_at": "2022-11-24T19:54:32.562623Z"
    }
    ```

### Delete ###
- **URL:** `/tasks/api/v1/tasks/{id}/`
- **Method:** `DELETE`
- **Code:** `204`
- **Headers :**
    ```
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiIsIn...'
    ```
