this file structure follow up:- 
-------------------------------------------------------------------------------------------------
fastapi-demo-products-with-ui/
│
├── app/                      # Main application package
│   ├── main.py               # App entry point
│   │
│   ├── core/                 # Core app configs & security
│   │   ├── config.py         # Environment variables
│   │   ├── security.py       # Auth / JWT / password utils
│   │   └── settings.py       # App settings
│   │
│   ├── db/                   # Database related files
│   │   ├── session.py        # DB session (engine, get_db)
│   │   ├── base.py           # Base for models
│   │   └── init_db.py        # DB initialization
│   │
│   ├── models/               # SQLAlchemy models
│   │   ├── __init__.py
│   │   └── product.py
│   │
│   ├── schemas/              # Pydantic schemas
│   │   ├── __init__.py
│   │   └── product.py
│   │
│   ├── crud/                 # DB operations
│   │   ├── __init__.py
│   │   └── product.py
│   │
│   ├── api/                  # API routes
│   │   ├── __init__.py
│   │   ├── deps.py           # Dependencies (auth, db)
│   │   ├── __init__.py
│   │   └── product.py
│   │
│   ├── services/             # Business logic layer
│   │   └── product_service.py
│   │
│   └── utils/                # Helpers
│       └── common.py
│
├── venv/                     # Virtual environment
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md

-----------------------------------------------------------------------------------

commands for the requirements completely install:-
-----------------------------------------------------------------------------------

it's commands use in the python fastapi projects

pip install fastapi -- it's all python projects

python -m venv venv -- virual environment

.\venv\Scripts\Activate.ps1 --- it's for activate the file / folder for easy run the program

pip install fastapi uvicorn -- install the fastapi and uvicorn

python.exe -m pip install --upgrade pip -- it's for pip upgrade

pip install sqlalchemy psycopg2 -- sqlalchemy install for PostgreSQL adapter for Python

pip install python-dotenv -- .env file install

python -m uvicorn app.main:app --reload -- another way to run program

-----------------------------------------------------------------------------------------------

Steps how it's working in the file folder by code
---------------------------------------------------------------------------------------
working :- Request → main.py → router → service → crud → model → database → response
Not working :-  Request
 → main.py
 → router
 → service
 → crud
 → ❌ ERROR OCCURS HERE
        |
        v
 → exceptions.py (Exception Handler)
 → logger.error()
 → FileHandler → logs/app.log
 → JSON Error Response

 -----------------------------------------------------------------------------------------------

Deployment github to vercel step by step
------------------------------------------
1) git init
2) git add .
3) git commit -m "fastapi project"
4) git branch -M main
5) git remote add origin https://github.com/vikas-11-dixena/fastapi_project.git
6) git push -u origin main
7) git status
8) git add readme.txt


cloud Database create kr ne ke bad ki querry
--------------------------------------------
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price NUMERIC(10,2) NOT NULL,
    quantity INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO products (name, description, price, quantity) VALUES
('iPhone 12', 'Apple iPhone 12 with A14 Bionic chip', 54999.00, 25),
('iPhone 12 Pro', 'Apple iPhone 12 Pro with triple‑camera system', 79999.00, 15),
('iPhone 13', 'Apple iPhone 13 with improved battery life', 62999.00, 30),
('iPhone 13 Pro', 'Apple iPhone 13 Pro with ProMotion display', 99999.00, 12),
('iPhone 14', 'Apple iPhone 14 with advanced dual‑camera system', 69999.00, 20),
('iPhone 14 Pro', 'Apple iPhone 14 Pro with Dynamic Island', 119999.00, 10),
('AirPods Pro', 'Apple AirPods Pro with active noise cancellation', 24999.00, 40),
('Apple Watch Series 8', 'Smartwatch with health and fitness tracking', 45999.00, 18),
('MacBook Air M1', 'Apple MacBook Air with M1 chip', 89999.00, 8),
('iPad Air 5th Gen', 'Apple iPad Air with M1 chip', 55999.00, 14);

select * from products;