# 📦 MTIT-Assignment-2-Microservices

## 📖 Project Description
This project is developed as part of the **IT4020 – Modern Topics in IT (MTIT) Assignment 2**.  
The objective of this assignment is to design and implement a **Microservices Architecture** for a real-world business domain, along with an **API Gateway** to manage and route requests efficiently.

The system demonstrates how multiple independent microservices can work together to form a scalable and maintainable backend solution.

---

## 🎯 Key Features
- ✅ Implementation of **4 independent microservices**
- ✅ Centralized **API Gateway**
- ✅ RESTful API design using FastAPI
- ✅ Auto-generated **Swagger API documentation**
- ✅ Routing through API Gateway to avoid multiple port exposure
- ✅ Clean and modular project structure

---

## 🏥 Selected Domain
**Hospital Management System**

---

## 🧩 Microservices Overview

| Service | Description |
|--------|------------|
| Patient Service | Manages patient details |
| Doctor Service | Handles doctor information |
| Appointment Service | Manages appointments between patients and doctors |
| Billing Service | Handles billing and payment details |

---

## 🌐 API Gateway
The API Gateway acts as a **single entry point** for all client requests and routes them to the appropriate microservices.


---

## ⚙️ Technologies Used
- **FastAPI (Python)**
- **Uvicorn**
- **REST APIs**
- **Swagger UI**

---

## 🚀 How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/your-username/mtit-assignment-2-microservices.git
cd mtit-assignment-2-microservices

cd patient-service
uvicorn main:app --port 8001 --reload
cd doctor-service
uvicorn main:app --port 8002 --reload
cd appointment-service
uvicorn main:app --port 8003 --reload
cd billing-service
uvicorn main:app --port 8004 --reload

cd api-gateway
uvicorn main:app --port 8080 --reload
```
| Member   | Contribution        |
| -------- | ------------------- |
| Member 1 | Patient Service     |
| Member 2 | Doctor Service      |
| Member 3 | Appointment Service |
| Member 4 | Billing Service     |
