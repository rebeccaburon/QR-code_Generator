# QR-code_Generator
 The repository contains backend + frontend to generate a QR-code for specific IDs

# Project Overview
This project is developed as part of my **final exam project** in the Computer Science (Datamatiker) program.  
The goal is to design and implement a **demonstration module** for the CERoS platform, enabling:

The module makes it possible to:


-  Generate QR codes for selected QC-batches  
- Automatically encode URLs with batch-specific parameters
- Display the generated QR-code inside the application  

- Scanning of QR codes using mobile device

- Automatic retrieval of related sample data and status information

The module consists of both **backend** and **frontend** components.


# Technologies

## Frontend
- **Streamlit 1.46.1**
- **Responsive HTML + CSS**

## Backend
- **Python 3.11+**
- **qrcode 8.2** 
- **Pillow 11.3.0**
- **Custom utility modules** 


    


## Database
- **PostgreSQL**
### Connection handled
- **psycopg2-binary 2.9.11** 
- **python-dotenv 1.2.1**