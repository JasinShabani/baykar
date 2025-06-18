Baykar Aircraft Manufacturing Management System

A full-stack Django-based web application designed for managing the production lifecycle of aircrafts. 
It includes modules for parts tracking, personnel assignment, team management, and full assembly coordination.

⸻

🚀 Features
	•	Aircraft parts management (Wing, Fuselage, Tail, Avionics)
	•	Personnel registration and team assignment
	•	Full aircraft assembly tracking
	•	Swagger API documentation (via drf-yasg)
	•	PostgreSQL database integration
	•	Dockerized for easy setup and deployment
	•	Responsive design using Bootstrap

⸻

🛠️ Tech Stack
	•	Backend: Django 5.0.7, Django REST Framework
	•	Database: PostgreSQL
	•	Frontend: HTML/CSS (Bootstrap 5)
	•	Containerization: Docker & Docker Compose

⸻

📦 Installation & Setup

1. Clone the repository

git clone https://github.com/JasinShabani/baykar.git
cd baykar

2. Create .env (optional if needed for secret keys)

⸻

🐳 Docker Setup

Build & Run the project with Docker:

docker-compose up --build

Rebuild + drop DB:

docker volume rm baykar_postgres_data
docker-compose down --volumes
docker-compose up --build

Run migrations inside the container:

docker-compose exec web python manage.py migrate

(Optional) Create a superuser

docker-compose exec web python manage.py createsuperuser


⸻

🖼️ Screenshots

You can add screenshots like this:

![fbbe3571-1520-477c-a14a-da487e63e070](https://github.com/user-attachments/assets/44b7098f-7abd-4ee5-bf39-ea5e99142977)
![6577f152-6dbd-4fef-85dc-d73c8a8246f3](https://github.com/user-attachments/assets/bf6af060-8100-4d66-aac8-9232faf634a7)
![043de025-173f-4c3e-a6b2-e8ca5da64d4c](https://github.com/user-attachments/assets/043cbaf2-c4e8-4b5c-8c97-b1125700d902)
![41628b8f-e047-4a79-8b20-304e215fe439](https://github.com/user-attachments/assets/b1c65448-58ff-4f10-b44b-a9da518d52e5)
![3292ccf8-a671-47f7-bf15-6170e7c1967e](https://github.com/user-attachments/assets/3bf6a557-d4e3-462d-8061-5402c98c9f39)
![9719efcd-8939-4698-a245-2da1dbc45b0e](https://github.com/user-attachments/assets/b6c8bb7d-7c69-48a8-8880-dd6f65eb1526)
![d19480cc-e5ff-431e-928a-beaeb70412f2](https://github.com/user-attachments/assets/0ec67e27-0978-460c-a99b-d1b8380d1330)


Just place them inside a screenshots/ folder and push to the repo.

⸻

📂 Project Structure

├── personnel/
├── production/
├── assembly/        
├── templates/
├── static/
├── Dockerfile
├── docker-compose.yml
├── manage.py
└── requirements.txt


⸻

🔗 Useful URLs
	•	Swagger Docs: http://localhost:8000/swagger/
	•	Login: http://localhost:8000/login/
	•	Admin Panel: http://localhost:8000/admin/

⸻

✍️ Author

Jasin Shabani - yasinsaban.com
https://www.linkedin.com/in/yasin-sabani-4475897145775486942/

⸻

📃 License

This project is licensed for educational and demonstration purposes only.
